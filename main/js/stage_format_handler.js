
const { dialog } = require('electron');
const fsp = require('fs/promises');
const { glob } = require('glob');
const { Exception } = require('sass');
const path = require('node:path');
const file_handler = require("./file_handler")

class StageFormatHandler {

	constructor() {
		this.loadedStageFormats = []
	}


	/** Add a stage format from .fmt.js file
	 * 
	 * @param {string} filePath Location of .fmt.js file
	 */
	loadStageFormat(filePath) {
		const {StageFormatImpl} = require(filePath);
		const fmt = StageFormatImpl;
		// check that the fmt contains the correct keys
		if (! "id" in fmt) {
			throw new Error("Stage format at " + filePath + " does not contain 'id' property");
		}
		if (! "name" in fmt) {
			fmt.name = fmt.id;
		}
		if (! "description" in fmt)
			fmt.description = "";
		if (! "requirements" in fmt)
			fmt.requirements = []
		// displayFramework and editingFramework may be undefined, but if displayFramework is undefined then so must be editingFramework.
		if ("editingFramework" in fmt && ! "displayFramework" in fmt)
			throw new Error("Stage format at " + filePath + "defines an editing framework by not display framework");
		
		// if there is already a stage format with this id open, then remove the old one
		for (let i = 0; i < this.loadedStageFormats.length; i++) {
			if (this.loadedStageFormats[i].id == fmt.id) {
				this.loadedStageFormats.splice(i, 1);
			}
		}

		this.loadedStageFormats.push(fmt);
	}

	async loadStageFormatsFromDir(dirPath) {

		if (!(await fsp.stat(dirPath)).isDirectory()) {
			throw new Error(dirPath + " is not a directory")
		}

		// search for .fmt.js files
		var globPattern = path.resolve(dirPath, "*.fmt.js");
		// for glob, if we're using windows we need to replace all the path separators with /
		globPattern = globPattern.split(path.sep).join(path.posix.sep);
		const stgFmtFilePaths = await glob(globPattern);

		for (const filePath of stgFmtFilePaths) {
			try {
				this.loadStageFormat(filePath);
			} catch(err) {
				console.error("Unable to load stage format", err.message);
			}
		}
	}


	async loadStageInstance(metadataFilePath, requirementsMetadataFilePaths=[]) {

		// open metadata and data buffer
		const {data, metadata}  = await file_handler.openStageFormat("", "", metadataFilePath);

		const primaryInstance = {
			data: data,
			metadata: metadata,
			metadataFilePath: metadataFilePath
		}
		
		// find the correct display framework
		let stage = this.loadedStageFormats.find((x) => x.id == metadata.format);
		if (typeof stage === "undefined") {
			throw new Error("Stage with id \"" + metadata.format + "\" not found");
		}
		if (typeof stage.displayFramework === "undefined") {
			throw new Error("Stage \"" + stage.id + "\" is defined, but does not have a display framework");
		}


		// open the supplied requirements and check that they match the expected ones
		var requirementInstances = [];
		for (let i = 0; i < stage.requirements.length; i++) {
			const fmt = await file_handler.openStageFormat("", "", requirementsMetadataFilePaths[i]);
			const requirementMetadata = fmt.metadata;
			const requirementBuf = fmt.data;
			if (requirementMetadata.format != stage.requirements[i]) {
				throw new Error("Requirement " + i + " for display framework \"" + stage.id + "\" does not match the expected stage format \"" + stage.requirements[i] + "\" (got \""+requirementMetadata.format+"\")");
			}
			requirementInstances.push({
				data: requirementBuf,
				metadata: requirementMetadata,
				metadataFilePath: requirementsMetadataFilePaths[i]
			})
		}

		// todo could erro check
		return stage.displayFramework(primaryInstance, requirementInstances, this);


	}


	/** Save the contents of the screen by calling an editing framework
	 * Creates a new stage instance, leaving the original intact.
	 * The "generated-by" property must be "USER_EDIT", and the "parent-stage-instances" property must contain only the original stage instance.
	 * 
	 * @param {Object} newMetadata Contents of new .stg.json file
	 */
	async saveStageInstanceAs(projPath, oldMetadataPath, oldRequirementsMetadataPaths,  newMetadata, stops, routes, metadataDir=undefined) {

		const oldMetadata = JSON.parse(await fsp.readFile(oldMetadataPath, { encoding: "utf-8", flag: "r" }));

		if (typeof newMetadata.timeCreated === "undefined") {
			newMetadata.timeCreated = (new Date()).toJSON();
		}

		if (typeof newMetadata.dependencyGraph === "undefined") {
			newMetadata.dependencyGraph = oldMetadata.dependencyGraph;
		}

		if (typeof newMetadata.format === "undefined") {
			newMetadata.format = oldMetadata.format;
		}
		if (newMetadata.format != oldMetadata.format) {
			throw new Error(`Format of stage instance to be saved ("${newMetadata.format}") does not mach the format of the original stage instance ("${oldMetadata.format}") `);
		}

		let stageFormat = this.loadedStageFormats.find((x) => x.id == newMetadata.format);
		if (typeof stageFormat === "undefined") {
			throw new Error("Unable to save stage instance: the stage format \""+newMetadata.format + "\" is not loaded.")
		}

		if (newMetadata.generatedBy != "USER_EDIT") {
			throw new Error("Unable to save stage instance: the \"generatedBy\" property is not \"USER_EDIT\"");
		}

		if (typeof newMetadata.nodeInGraph === "undefined") {
			// null, as this was not created by a node
			newMetadata.nodeInGraph = null;
		}

		// calculate relative path to old metadata file
		var relativePathToOldMetadataFile = path.relative(metadataDir, oldMetadataPath);
		relativePathToOldMetadataFile = relativePathToOldMetadataFile.split(path.sep).join(path.posix.sep);

		if (typeof newMetadata.parentStageInstances === "undefined") {
			newMetadata.parentStageInstances = [relativePathToOldMetadataFile];
		} 

		// decide where to save the metadata file. Use the project's default dir if metadataDir is undefined
		if (typeof metadataDir === "undefined") {
			metadataDir = path.resolve(projPath, JSON.parse(await fsp.readFile(path.resolve(projPath, "info.json"), { encoding: "utf-8", flag: "r" })).stageInstances[0]);
		}

		// check that value of newMetadata.parentStageInstances holds the correct value if it was already set in the input to this function,
		// otherwise throw an error
		if (!Array.isArray(newMetadata.parentStageInstances) ||
			newMetadata.parentStageInstances.length != 1 ||
			path.relative(path.resolve(metadataDir, newMetadata.parentStageInstances[0]), oldMetadataPath) != "") {
			throw new Error(`Unable to save stage instance: the property \"parentStageInstances\" should contain a single item referring to the original version of this file. In this case this should be ["${relativePathToOldMetadataFile}"]; you can omit the parentStageInstances property from newMetadata and this will be added automatically.`);
		}

		// work out where to save the new metadata file
		// give it a name the same as the old one with _USER_EDIT_{N} appended.
		// If the old metadata file already has _USER_EDIT_.., then bump N.
		const stageInstanceDir = metadataDir;
		const oldMetadataBasename = path.basename(oldMetadataPath);
		// find the name _USER_EDIT_{N} using a regular expression
		const expr = /(.+?)(_USER_EDIT_([0-9]+))?\.stg\.json/;
		const match = oldMetadataBasename.match(expr);
		const nameStem = match[1];
		var N = parseInt(match[3]);
		// increase N until there is an available file name
		while (await fsp.access(path.resolve(metadataDir, `${nameStem}_USER_EDIT_${N}.stg.json`))) {
			N++;
		}
		const newMetadataPath = path.resolve(metadataDir, `${nameStem}_USER_EDIT_${N}.stg.json`);
		

		// // give it a name that does not collide with other names
		// // look for all other formats of the form ${FORMAT}_${N}.stg.json
		// var globPattern = path.resolve(path.dirname(stageInstanceDir), newMetadata.format + "_*.stg.json");
		// // for glob, if we're using windows we need to replace all the path separators with /
		// globPattern = globPattern.split(path.sep).join(path.posix.sep);
		// const globOutput = await glob(globPattern);

		// // increase N until there is a non colliding name
		// var N = 1;
		// while (globOutput.includes(path.resolve(stageInstanceDir, newMetadata.format + "_" + N + ".stg.json"))) {
		// 	N++;
		// }
		
		// find the file extension we will use for the data file
		var dataFileExtension = stageFormat.fileExtension;
		if (typeof dataFileExtension === "undefined") {
			dataFileExtension = "dat";
		}

		// work out where to save the actual data file.
		// if undefined, use the same file name and folder as the metadata path.
		if (typeof newMetadata.datafile === "undefined") {
			// remove .stg.json
			const expr = /(.*)\.stg\.json/;
			const nameStem = path.basename(newMetadataPath).match(expr)[1];
			// relative path, and since this is in the same folder as the metadata file we don't need to worry.
			newMetadata.datafile = nameStem + "." + dataFileExtension;
		}

		// open all necessary files for the editing framework

		// original data file.
		const oldData = await fsp.readFile(oldMetadata.datafile);

		// original requirement data files
		var oldRequirementsData = /*oldRequirementsMetadataPaths*/ [];
		for (const oldRequirementMetadataPath of oldRequirementsMetadataPaths) {
			const oldRequirementMetadata = JSON.parse(await fsp.readFile(oldRequirementMetadataPath, { encoding: "utf-8", flag: "r" }));
			const oldRequirementData = fsp.readFile(oldRequirementMetadata.datafile);
			oldRequirementsData.push(oldRequirementData);
		}

		// call the display framework
		const newData = stageFormat.displayFramework(oldData, oldRequirementsData, stops, routes);

		// write the new metadata
		await fsp.writeFile(newMetadataPath, newMetadata);

		// write the new data
		const newDataPath = path.resolve(newMetadataPath, newMetadata.datafile);
		await fsp.writeFile(newDataPath, newData);

	}

	

}

/**
 * A bus stop in the format used to communicate with the render
 * @typedef {{lat: number; lon: number; id: number; name: string | undefined; hidden_attrs: any; user_attrs: any;}} BNOPIStop
 */

/**
 * A bus rute in the format used to communicate with the renderer
 * @typedef {{id: number; name: string | undefined; points: {lat: number; lon: number;}}} BNOPIRoute
 */


/**
 * Interface for stage formats. Each *.fmt.json* file must export a class StageFormatImpl, with extends this.
 */
class StageFormat {


	static get name() {
		return "Untitled Stage";
	}

	static get id() {
		return "NO_FORMAT"
	}

	static get requirements() {
		return []
	}

	static get description() {
		return "Stage with no name."
	}

	static get fileExtension() {
		return "dat"
	}

	/** Convert a stage instance to bnopi stops and routes.
	 * 
	 * @param {{data: Buffer, metadata:any, metadataFilePath:String}} primaryInstance Data and metadata about the primary instance
	 * @param {{data: Buffer, metadata:any, metadataFilePath:String}[]} requirementInstances Data and metadata about requirement instance.
	 * @param {StageFormatHandler} stageFormatHandler The stage format handler, with method for accessing other stage formats
	 * @returns {{stops:BNOPIStop[], routes:BNOPIRoute[]}}
	 */
	static displayFramework(primaryInstance, requirementInstances, stageFormatHandler) {
		return {stops: [], routes: []}
	}

	/** Convert bnopi stops and routes to a stage instance
	 * 
	 * @param {{data: Buffer, metadata:any, metadataFilePath:String}} primaryInstance Data and metadata about the original primary instance
	 * @param {{data: Buffer, metadata:any, metadataFilePath:String}[]} requirementInstances  Data and metadata about the original requirement instances
	 * @param {BNOPIStop[]} stops All stops that were displaying in the BNOPI interface at the time of save
	 * @param {BNOPIRoute[]} routes All routes that were displaying
	 * @param {StageFormatHandler} stageFormatHandler The stage format handler, with method for accessing other stage formats
	 * @returns {{primaryInstance: (Buffer | undefined), requirementInstances: (Buffer | undefined)[]}} New stage instances to write to disk. If undefined, BNOPI will continue to use the old stage instances.
	 */
	static editingFramework(primaryInstance, requirementInstances, stops, routes, stageFormatHandler) {

		return {primaryInstance: undefined, requirementInstances: []}

	}
}

module.exports = {StageFormatHandler, StageFormat}
