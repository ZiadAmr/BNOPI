
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
		var fmt = require(filePath);
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
		var globPattern = path.resolve(path.dirname(dirPath), "*.fmt.js");
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
		const {metadata, data} = file_handler.openStageFormat("", "", metadataFilePath);
		

		// find the correct display framework
		let stage = this.loadedStageFormats.find((x) => x.id == metadata.stage);
		if (typeof stage === "undefined") {
			throw new Error("Stage with id \"" + metadata.stage + "\" not found");
		}
		if (typeof stage.displayFramework === "undefined") {
			throw new Error("Stage \"" + stage.id + "\" is defined, but does not have a display framework");
		}


		// open the supplied requirements and check that they match the expected ones
		var requirementBufs = [];
		for (let i = 0; i < stage.requirements.length; i++) {
			const { requirementMetadata, requirementBuf } = file_handler.openStageFormat("", "", requirementsMetadataFilePaths[i]);
			if (requirementMetadata.format != stage.requirements[i]) {
				throw new Error("Requirement " + i + " for display framework \"" + stage.id + "\" does not match the expected stage format \"" + stage.requirements[i] + "\" (got \""+requirementMetadata.format+"\")");
			}
			requirementBufs.push(requirementBuf);
		}

		// todo could erro check
		return stage.displayFramework(data, requirementBufs);


	}

	

}

module.exports = {StageFormatHandler}
