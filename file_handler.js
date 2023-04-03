const fsp = require('fs/promises');
const path = require('node:path');
var glob = require("glob");

// may need to update this if this file is moved
const projectsDir = path.resolve("./projects");

/**
 * @param {string} project String ID of the project
 * @param {string} stage String ID of the stage
 * @param {string} metadataLoc Absolute path where the stage metadata file is stored (path to .stg.json file)
 * @returns Object containing data (contents of the file) and metadata e.g. time created, created by what node. Metadata may be stored somewhere else by BNOPI, it's BNOPI's job to figure out where.
 */
async function openStageFormat(project, stage, metadataLoc) {

	// TODO: may want to add checks on project & stage, or remove these as parameters altogether.

	// open metadata file
	// TODO: might throw an error, deal with this later
	const metadata_str = await fsp.readFile(metadataLoc, {encoding: "utf-8", flag: "r"});

	// parse JSON
	// TODO: again this might throw an error
	const metadata = JSON.parse(metadata_str);
	
	// The path to the data might be relative to the .stg.json file, so check this
	const absoluteDataPath = path.resolve(path.dirname(metadataLoc), metadata.datafile);
	// read the actual data file.
	// no encoding is specified so this appears as a buffer object.
	// TODO: again this might throw an error
	const data = await fsp.readFile(absoluteDataPath, {flag:"r"})

	return {
		data: data,
		metadata:metadata
	}
}

/**
 * Function to write a new stage instance. Will be invoked by editing frameworks.
 * Needs to write 2 files in total, the metadata (.stg.json) and the stage instance itself.
 * 
 * @param {string} project String ID of the project
 * @param {string} stage String ID of the stage 
 * @param {string} metadataLoc Where the metadata is stored (path to .stg.json file)
 * @param {Buffer} data Contents of the file
 * @param {Object} metadata Data about the stage instance, including where it should be saved.
 */
async function saveStageFormat(project, stage, metadataLoc, data, metadata) {

	// TODO again, all these functions could cause errors.

	// get path of stage instance
	const dataPath = path.resolve(path.dirname(metadataLoc), metadata.datafile);

	// stringify metadata
	const metadata_str = JSON.stringify(metadata);

	await fsp.writeFile(metadataLoc, metadata_str);
	await fsp.writeFile(dataPath, data);
	
}

/**
 * @param {string} project String ID of the project
 * @returns List of all stage instances for this project and their metadata
 */
async function getListOfStageFormat(project) {

	var stageInstances = [];

	// open project info file to find where to search for stage instances
	const infoFileLoc = path.resolve(projectsDir, "./"+project+"/info.json");
	const projectInfoString = await fsp.readFile(infoFileLoc, { encoding: "utf-8", flag: "r" });
	const projectInfo = JSON.parse(projectInfoString);

	// search each directory that might contain stage instances
	for (const dir of projectInfo.stageInstances) {
		var globPattern = path.resolve(path.dirname(infoFileLoc), dir, "*.stg.json");
		// for glob, if we're using windows we need to replace all the path separators with /
		globPattern = globPattern.split(path.sep).join(path.posix.sep);
		const metadataFilePaths = await glob(globPattern);

		// open each stage metadata file and add contents to stageInstances
		for (const metadataFilePath of metadataFilePaths) {
			const metadataString = await fsp.readFile(metadataFilePath, { encoding: "utf-8", flag: "r" });
			const metadata = JSON.parse(metadataString);

			stageInstances.push({
				path: metadataFilePath,
				metadata: metadata
			})
		}

	}

	return stageInstances;
}



module.exports = { openStageFormat, saveStageFormat, getListOfStageFormat};