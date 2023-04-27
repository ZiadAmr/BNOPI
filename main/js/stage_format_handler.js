
const { dialog } = require('electron');
const fsp = require('fs/promises');
const { glob } = require('glob');
const { Exception } = require('sass');
const path = require('node:path');
const file_handler = require("./file_handler")

/**
 * Instance type passed to display and editing frameworks
 * @typedef {Object} BNOPIInstance
 * @property {Buffer} data
 * @property {InstanceMetadata} metadata
 * @property {string} metadataFilePath
 */

/**
 * Contents of a stage instance metadata file
 * @typedef {Object} InstanceMetadata
 * @property {string} timeCreated
 * @property {string} dependencyGraph
 * @property {string} format
 * @property {string} generatedBy
 * @property {number|null} nodeInGraph
 * @property {string[]} parentStageInstances
 * @property {string[]} siblingStageInstances
 * @property {string} datafile
 */

/**
 * A bus stop in the format used to communicate with the render
 * @typedef {Object} BNOPIStop
 * @property {number} lat
 * @property {number} lon
 * @property {number} id
 * @property {string |undefined} name
 * @property {any} hidden_attrs
 * @property {any} user_attrs
 */

/**
 * Coordinates in the GCS system
 * @typedef {Object} LatLon
 * @property {number} lat
 * @property {number} lon
 */

/**
 * A bus route in the format used to communicate with the renderer
 * @typedef {Object} BNOPIRoute
 * @property {number} id
 * @property {string | undefined} name
 * @property {LatLon[][]} links
 * @property {number[]} stops
 * @property {any} hidden_attrs
 * @property {any} user_attrs
 */

/**
 * Properties of the stage format class, without the display or editing frameworks.
 * @typedef {Object} StageFormatInfo
 * @property {string} name
 * @property {string} id
 * @property {string[]} requirements
 * @property {string} description
 * @property {string} fileExtension
 */


class StageFormatHandler {

	constructor() {
		/**
		 * @type {(typeof StageFormat)[]}
		 */
		this.loadedStageFormats = [];
	}


	/** Add a stage format from .fmt.js file
	 * 
	 * @param {string} filePath Location of .fmt.js file
	 */
	loadStageFormat(filePath) {
		const fmt = require(filePath);
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

	/** Load all the stage formats from the specified directory, and add them to the `StageFormatHandler`
	 * 
	 * @param {string} dirPath 
	 */
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

	/**
	 * Calls display framework for the instance pointed to by `primaryMetadataFilePath`
	 * @param {string} primaryMetadataFilePath 
	 * @param {string[]} requirementsMetadataFilePaths Other stage instances needed for the display framework to return a list of stops and routes
	 * @returns {Promise<{stops: BNOPIStop[], routes: BNOPIRoute[]}>}
	 */
	async loadStageInstance(primaryMetadataFilePath, requirementsMetadataFilePaths=[]) {

		const { primaryInstance, requirementInstances } = await this.openPrimaryAndRequirementInstances(primaryMetadataFilePath, requirementsMetadataFilePaths);

		// todo could erro check
		let stage = this.loadedStageFormats.find((x) => x.id == primaryInstance.metadata.format);
		return stage.displayFramework(primaryInstance, requirementInstances, this);


	}



	/**
	 * Opens a primary instance and requirement stage instances. Checks that the supplied requirement stage instances as expected for the primary stage format. The result of this function is used as input to both display and editing frameworks.
	 * @param {string} primaryMetadataFilePath Path to the metadata file of the primary stage instance
	 * @param {string[]} requirementsMetadataFilePaths Paths to metadata files of the second stage instances, in order of the requirements as specified in the stage format.
     * @returns {Promise<{primaryInstance: BNOPIInstance, requirementInstances: BNOPIInstance[]}>}
	 */
	async openPrimaryAndRequirementInstances(primaryMetadataFilePath, requirementsMetadataFilePaths = []) {
		// open metadata and data buffer
		const { data, metadata } = await file_handler.openStageFormat("", "", primaryMetadataFilePath);

		const primaryInstance = {
			data: data,
			metadata: metadata,
			metadataFilePath: primaryMetadataFilePath
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
				throw new Error("Requirement " + i + " for display framework \"" + stage.id + "\" does not match the expected stage format \"" + stage.requirements[i] + "\" (got \"" + requirementMetadata.format + "\")");
			}
			requirementInstances.push({
				data: requirementBuf,
				metadata: requirementMetadata,
				metadataFilePath: requirementsMetadataFilePaths[i]
			})
		}

		return {primaryInstance: primaryInstance, requirementInstances: requirementInstances};
	}


	/**Save the contents of the screen by calling an editing framework.
	 * Creates a new primary stage instance and requirement instances if necessary. Saves these in the same location as the original files.
	 * 
	 * 
	 * @param {string} oldPrimaryMetadataPath 
	 * @param {string[]} oldRequirementsMetadataPaths
	 * @param {BNOPIStop[]} stops 
	 * @param {BNOPIRoute[]} routes 
	 * @returns {Promise<{newestPrimaryMetadataPath: string, newestRequirementsMetadataPaths: string[]}>} Locations of the most up-to-date versions of the requirements, to reflect how some of them may have been updated.
	 */
	async saveStageInstanceAs(oldPrimaryMetadataPath, oldRequirementsMetadataPaths=[], stops, routes) {

		// load all old stage instances
		const { primaryInstance, requirementInstances } = await this.openPrimaryAndRequirementInstances(oldPrimaryMetadataPath, oldRequirementsMetadataPaths);

		// look for the correct stage format
		const stage = this.loadedStageFormats.find((x) => x.id == primaryInstance.metadata.format);

		// call editing framework
		const edits = stage.editingFramework(primaryInstance, requirementInstances, stops, routes, this);
		
		// fix requirementInstances to be a list of oldRequirementsMetadataPaths.length,
		// add nulls in necessary
		if (typeof edits.requirementDatas == "undefined" || edits.requirementDatas === null) {
			edits.requirementDatas = Array(oldRequirementsMetadataPaths.length).fill(null);
		} else {
			while (edits.requirementDatas.length < oldRequirementsMetadataPaths.length) {
				edits.requirementDatas.push(null);
			}
		}
		

		// parent instances of the new files we will create
		const parents = [primaryInstance.metadataFilePath, ...requirementInstances.map(x => x.metadataFilePath)];
		/** @type {string[]} */
		const siblings = []; // add as we go

		// store files we will write to disk
		/** @type {BNOPIInstance | null} */
		var newPrimaryInstance = null;
		/** @type {(BNOPIInstance | null)[]} */
		var newRequirementInstances = [];

		// decide where to save the new stage instance(s)
		if (typeof edits.primaryData != null) {
			newPrimaryInstance = await this.editInstance(primaryInstance, edits.primaryData, "primary");
			newPrimaryInstance.metadata.parentStageInstances = parents;
			siblings.push(newPrimaryInstance.metadataFilePath);

		}


		// now do the same for the requirement instances in case they were edited.
		for (let i = 0; i < oldRequirementsMetadataPaths.length; i++) {
			const newData = edits.requirementDatas[i];
			const oldInstance = requirementInstances[i];
			if (newData == null) {
				newRequirementInstances.push(null);
			} else {
				const newInstance = await this.editInstance(oldInstance, newData, "requirement");
				newInstance.metadata.parentStageInstances = parents;
				newRequirementInstances.push(newInstance);
				siblings.push(newInstance.metadataFilePath);
			}
		}

		// add the siblings property to all the new metadata files - but don't add the current file as a sibling
		// also convert parent instances to relative paths.
		if (newPrimaryInstance != null)
			newPrimaryInstance.metadata.siblingStageInstances = siblings
				// remove itself from the siblings
				.filter(x => x != newPrimaryInstance.metadataFilePath)
				// convert paths to relative
				.map(x => path.relative(path.dirname(newPrimaryInstance.metadataFilePath), x));
			// convert parents to relative paths
			newPrimaryInstance.metadata.parentStageInstances = newPrimaryInstance.metadata.parentStageInstances
				.map(x => path.relative(path.dirname(newPrimaryInstance.metadataFilePath), x));

		for (const requirementInstance of newRequirementInstances) {
			if (requirementInstance != null) {
				requirementInstance.metadata.siblingStageInstances = siblings
					.filter(x => x != requirementInstance.metadataFilePath)
					.map(x => path.relative(path.dirname(requirementInstance.metadataFilePath), x));
				requirementInstance.metadata.parentStageInstances = requirementInstance.metadata.parentStageInstances
					.map(x => path.relative(path.dirname(requirementInstance.metadataFilePath), x));
			}
		}

		// convert parent and sibling metadata paths to relative paths.
		// if (newPrimaryInstance != null)
		// 	for (const pa)
		// for (const requirementInstance of newRequirementInstances) {
		// 	if (requirementInstance != null)
				
		// }

		// write files to disk
		if (newPrimaryInstance != null) {
			await fsp.writeFile(newPrimaryInstance.metadataFilePath, JSON.stringify(newPrimaryInstance.metadata));
			const dataLocAbsolute = path.resolve(path.dirname(newPrimaryInstance.metadataFilePath), newPrimaryInstance.metadata.datafile);
			await fsp.writeFile(dataLocAbsolute, newPrimaryInstance.data);
		}
		for (const ins of newRequirementInstances) {
			if (ins != null) {
				await fsp.writeFile(ins.metadataFilePath, JSON.stringify(ins.metadata));
				const dataLocAbsolute = path.resolve(path.dirname(ins.metadataFilePath), ins.metadata.datafile);
				await fsp.writeFile(dataLocAbsolute, ins.data);
			}
		}

		// return paths to metdata of most recent versions of the files
		/** @type {string} */
		var newestPrimaryMetadataPath;
		if (newPrimaryInstance == null) {
			newestPrimaryMetadataPath = oldPrimaryMetadataPath;
		} else {
			newestPrimaryMetadataPath = newPrimaryInstance.metadataFilePath;
		}
		/** @type {string[]} */
		const newestRequirementsMetadataPaths = []
		for (let i = 0; i < oldRequirementsMetadataPaths.length; i++) {
			if (newRequirementInstances[i] == null) {
				newestRequirementsMetadataPaths.push(oldRequirementsMetadataPaths[i])
			} else {
				newestRequirementsMetadataPaths.push(newRequirementInstances[i].metadataFilePath)
			}
		}
		return {
			newestPrimaryMetadataPath: newestPrimaryMetadataPath,
			newestRequirementsMetadataPaths: newestRequirementsMetadataPaths
		}

	}

	/** Creates a new Instance (without writing to disk) of `oldInstance`. Creates new metadata for the new instances and decides where to save the new metadata and new data.
	 * 
	 * @param {BNOPIInstance} oldInstance 
	 * @param {Buffer} newData 
	 * @param {"primary" | "requirement"} editKind Whether `oldInstance` was a primary or requirement instance in the editing framework that created `newData` 
	 * @returns {Promise<BNOPIInstance>}
	 */
	async editInstance(oldInstance, newData, editKind="primary") {

		// string we use for the algorithm that generated this file
		// also in the filename of metadata files
		var alg;
		switch (editKind) {
			case 'primary': alg = "USER_PRIMARY_EDIT"; break;
			case 'requirement': alg = "USER_REQUIREMENT_EDIT"; break
		}

		const metadataDir = path.dirname(oldInstance.metadataFilePath);

		// decide where to save the new metadata file.
		// use the current metadata file name and append _USER_PRIMARY_EDIT_{N}, where N is the lowest possible number such that this file doesn't already exist
		// If the filename already contains _USER_PRIMARY_EDIT_{N}, then replace N with the lowest possible number that is higher than N
		const oldMetadataBasename = path.basename(oldInstance.metadataFilePath);
		// find the name _USER_PRIMARY_EDIT_{N} using a regular expression
		const expr = new RegExp(`(.+?)(_${alg}_([0-9]+))?\\.stg\\.json`)
		// const expr = /(.+?)(_USER_PRIMARY_EDIT_([0-9]+))?\.stg\.json/;
		const match = oldMetadataBasename.match(expr);
		const nameStem = match[1];
		var N = 1;
		if (typeof match[3] != "undefined") {
			N = parseInt(match[3]);
		}
		// increase N until there is an available file name
		var newPathExists = true;
		do {
			try {
				await fsp.access(path.resolve(metadataDir, `${nameStem}_${alg}_${N}.stg.json`))
				N++;
			} catch {
				newPathExists = false;
				// if there was an error then this file does not exist. then we can write to this location
				// bad code. ought to make it not bad
			}
		} while (newPathExists);

		const newMetadataPath = path.resolve(metadataDir, `${nameStem}_${alg}_${N}.stg.json`);


		// create new metadata file
		/** @type {InstanceMetadata} */
		const newMetadata = {};


		// decide where to save the new data.
		// User may have defined this, but if not, use the same file name and folder as the metadata path, with the extension swapped out.
		{
			// remove .stg.json
			const expr = /(.*)\.stg\.json/;
			const nameStem = path.basename(newMetadataPath).match(expr)[1];
			// relative path, and since this is in the same folder as the metadata file we don't need to worry.
			// get the data file extension
			const format = this.loadedStageFormats.find((x) => x.id == oldInstance.metadata.format);
			var fileExtension = "dat";
			if (typeof format == "undefined"){
				// user the format of the old file
				const split = oldInstance.metadata.datafile.split(".");
				if (split.length > 0) {
					fileExtension = split.pop();
				}
			} else {
				fileExtension = format.fileExtension;
			}
			newMetadata.datafile = nameStem + "." + fileExtension;
		}



		// fill in rest of new metadata
		newMetadata.timeCreated = (new Date()).toJSON();
		newMetadata.dependencyGraph = oldInstance.metadata.dependencyGraph;
		newMetadata.format = oldInstance.metadata.format;
		newMetadata.generatedBy = alg;
		newMetadata.nodeInGraph = oldInstance.metadata.nodeInGraph;
		// parent stage instances refer to to stage instances that were used to create this, i.e. the data and requirements
		newMetadata.parentStageInstances = [path.relative(path.dirname(newMetadataPath), oldInstance.metadataFilePath)];
		newMetadata.siblingStageInstances = []; // other stage instances that were generated at the same time (come back to this later)

		return {
			data: newData,
			metadata: newMetadata,
			metadataFilePath: newMetadataPath
		};
	}


	/**
	 * 
	 * @param {string} stageFormatID 
	 * @returns Result of getters from the StageFormat class.
	 */
	getStageFormatInfo(stageFormatID) {
		const stage = this.loadedStageFormats.find((x) => x.id == stageFormatID);
		if (typeof stage == "undefined") {
			return undefined;
		}
		return {
			name: stage.name,
			id: stage.id,
			requirements: stage.requirements,
			description: stage.description,
			fileExtension: stage.fileExtension
		}

	}
}


/**
 * Interface for stage formats. Each *.fmt.json* file must export a class which extends this.
 */
class StageFormat {

	/**
	 * Name that is displayed in the properties tab in the GUI
	 * @type {string}
	 */
	static get name() {
		return "Untitled Stage";
	}

	/**
	 * How this stage format is referred to elsewhere
	 * @type {string}
	 */
	static get id() {
		return "NO_FORMAT"
	}

	/**
	 * Formats of any other instances that are required for the display and editing frameworks.
	 * @type {string[]}
	 */
	static get requirements() {
		return []
	}

	/**
	 * Description that is displayed in the properties tab in the GUI
	 * @type {string}
	 */
	static get description() {
		return "Stage with no name."
	}

	/**
	 * File extension for stage instances of this format
	 * @type {string}
	 */
	static get fileExtension() {
		return "dat"
	}

	/** Converts a stage instance to bnopi stops and routes.
	 * 
	 * @param {BNOPIInstance} primaryInstance Data and metadata about the primary instance
	 * @param {BNOPIInstance[]} requirementInstances Data and metadata about requirement instance.
	 * @param {StageFormatHandler} stageFormatHandler The stage format handler, with methods for accessing other stage formats
	 * @returns {{stops:BNOPIStop[], routes:BNOPIRoute[]}}
	 */
	static displayFramework(primaryInstance, requirementInstances, stageFormatHandler) {
		return {stops: [], routes: []}
	}

	/** Converts bnopi stops and routes to a stage instance
	 * 
	 * @param {BNOPIInstance} primaryInstance Data and metadata about the original primary instance
	 * @param {BNOPIInstance[]} requirementInstances  Data and metadata about the original requirement instances
	 * @param {BNOPIStop[]} stops All stops that were displaying in the BNOPI interface at the time of save
	 * @param {BNOPIRoute[]} routes All routes that were displaying
	 * @param {StageFormatHandler} stageFormatHandler The stage format handler, with method for accessing other stage formats
	 * @returns {{primaryData: (Buffer | null), requirementDatas: (Buffer | null)[] | null | undefined}} New stage instances to write to disk. If undefined or null, BNOPI will continue to use the old stage instances.
	 */
	static editingFramework(primaryInstance, requirementInstances, stops, routes, stageFormatHandler) {

		return {primaryData: null, requirementDatas: null}

	}
}

module.exports = {StageFormatHandler, StageFormat}
