const fsp = require('fs/promises');
const path = require('node:path');
var glob = require("glob");
const { BrowserWindow, app, ipcMain, Notification, dialog } = require('electron');
const { title } = require('process');

// may need to update this if this file is moved
const projectsDir = path.resolve("projects/");

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

	addAbsolutePathsToInstanceMetadata(metadataLoc, metadata);
	
	// The path to the data might be relative to the .stg.json file, so check this
	// const absoluteDataPath = path.resolve(path.dirname(metadataLoc), metadata.datafile);
	// read the actual data file.
	// no encoding is specified so this appears as a buffer object.
	// TODO: again this might throw an error
	const data = await fsp.readFile(metadata.datafileAbs, {flag:"r"})

	return {
		data: data,
		metadata:metadata
	}
}

function addAbsolutePathsToInstanceMetadata(metadataFilePath, metadata) {
	// convert links to absolute paths
	const dir = path.dirname(metadataFilePath);
	metadata.datafileAbs = path.resolve(dir, metadata.datafile);
	metadata.parentStageInstancesAbs = metadata.parentStageInstances.map(p => 
		path.resolve(dir, p)
	)
	metadata.siblingStageInstancesAbs = metadata.siblingStageInstances.map(p => 
		path.resolve(dir, p)
	)
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
 * @param {string} projPath Path to the project folder
 * @returns {Promise<{path:String, metadata:InstanceMetadata}[]>}List of all stage instances for this project and their metadata
 */
async function getListOfStageInstance(projPath) {

	var stageInstances = [];

	// open project info file to find where to search for stage instances
	const infoFileLoc = path.resolve(projPath, "info.json");
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
			/** @type {InstanceMetadata} */
			const metadata = JSON.parse(metadataString);

			addAbsolutePathsToInstanceMetadata(metadataFilePath, metadata)

			stageInstances.push({
				path: metadataFilePath,
				metadata: metadata
			})
		}

	}

	return stageInstances;
}

/**
 * Opens a dialog box and returns a status, either "cancelled", "not_project", or "ok".
 * If "ok", then it also returns a path.
 * This function does not actually open the project, nor does it check to see if any errors would occur.
 * 
 */
async function openProjectFolderDialog() {
	
	const dir = await dialog.showOpenDialog({
		properties: ["openDirectory"],
		defaultPath: projectsDir,
	});

	if (dir.canceled === true) {
		return {status: "cancelled"}
	}

	// check that the dir contains info.json
	const lookFor = path.resolve(dir.filePaths[0], "info.json");
	try {
		await fsp.access(lookFor);
	} catch {
		// display error dialog
		dialog.showErrorBox("Not a project", "This directory does not contain an info.json file.")
		return { status: "not_project"}
	}

	return {status: "ok", path:dir.filePaths[0]}

}

/**
 * Opens a dialog box and returns a status, either "cancelled", "not_project", or "ok".
 * If "ok", then it also returns a path.
 * This function is used for selecting a directory to store an output stage instance created by an algorithm
 * 
 */
async function selectBNOPIOutputStageInstanceLocation() {
	
	const dir = await dialog.showOpenDialog({
		properties: ["openDirectory"],
		defaultPath: projectsDir,
	});

	if (dir.canceled === true) {
		return {status: "cancelled"}
	}

	try {
		await fsp.access(dir.filePaths[0]);
	} catch {
		// display error dialog
		dialog.showErrorBox("Error opening directory")
		return { status: "Error"}
	}

	return {status: "ok", path:dir.filePaths[0]}

}

/**
 * 
 * @returns Returns the path to a metadatafile (of an algorithm)
 */
async function openBNOPIAlg(){
	const file = await dialog.showOpenDialog({
		properties: ["openFile"],
		defaultPath: projectsDir,
		filters: [{name: 'Algorithm metadata files', extensions:['alg.json']}]
	});

	if (file.canceled === true) {
		return {status: "cancelled"}
	}

	try {
		await fsp.access(file.filePaths[0]);
	} catch {
		// display error dialog
		dialog.showErrorBox("Not an algorithm metadata file", "This is not a metadata file for an algorithm")
		return { status: "not_project"}
	}

	var meta = await fsp.readFile(file.filePaths[0], { encoding: "utf-8", flag: "r" });
	meta = JSON.parse(meta);

	return {status: "ok", meta, path:path.dirname(file.filePaths[0])}
}

/**
 * Display dialog box to create a new project
 * @returns Path where the project directory will be created, or undefined if the user cancelled.
 */
async function createNewProjectDialog() {
	const dir = await dialog.showSaveDialog({
		title:"Create Project", 
		defaultPath:projectsDir,
		buttonLabel:"Create Project",
		properties:["showOverwriteConfirmation"]
	});

	return dir;

}

/**
 * Sets up the folder structure for a new project
 * 
 * @param {string} projpath Path of the new folder that we are going to create
 */
async function createNewProject(projpath) {

	// check that the directory inside which we will create the new folder exists
	// this would normally just resolve to the default projects folder
	const workspaceFolder = path.resolve(projpath, "..");
	const projName = path.basename(projpath);

	try {
		await fsp.access(workspaceFolder)
	} catch (e) {
		dialog.showErrorBox("Access denied", "You do not have access to the folder " + workspaceFolder);
		return { status: "error" }
	}


	// create files
	// maybe better to copy these from an external source? TODO

	// info.json
	const info = JSON.stringify({
		title: projName,
		description: "Project description",
		dependencyGraph: "graph.dg.json",
		stageInstances: ["stage_instances/"]
	});

	// graph.dg.json
	const graph = JSON.stringify({
		// TODO
	});


	// create the project folder and all necessary files
	try {
		await fsp.mkdir(projpath);
	} catch {
		dialog.showErrorBox("Cannot create project", "Unable to create folder " + projpath);
		return { status: "error" }
	}

	await fsp.mkdir(path.resolve(projpath, "stage_instances"))
	await fsp.writeFile(path.resolve(projpath, "info.json"), info);
	await fsp.writeFile(path.resolve(projpath, "graph.dg.json"), graph);

	return {status:"ok"}

}

/** returns contents of the info.json file and adds this project to the recents
 * 
 * @param {string} projPath Location of the project we want to open (usually in the /projects folder)
 */
async function getProjectMetadata(projPath) {

	// TODO error checking

	// get contents of the info.json file
	const metadataLoc = path.resolve(projPath, "info.json");
	const metadataString = await fsp.readFile(metadataLoc, { encoding: "utf-8", flag: "r" });
	const metadata = JSON.parse(metadataString);



	return metadata;

}

/** Get some recently opened projects from recents.txt in appdata
 * 
 * @param {Number} n N most recents to return
 * @returns 
 */
async function getRecents(n = 10) {
	const recentsLoc = path.resolve(app.getPath("userData"), "recents.txt");

	try {
		await fsp.access(recentsLoc);
	} catch {
		return [];
	}

	const recentsTxt = await fsp.readFile(recentsLoc, { encoding: "utf-8", flag: "r" });
	const recents = recentsTxt.split("\n");

	var nMostRecent = [];
	// loop backwards over the recents until we have n distinct projects or the finish the list
	for (const recent of recents.slice().reverse()) {
		if (recent == "") {
			continue;
		}
		if (!nMostRecent.includes(recent)) {
			nMostRecent.push(recent);
		}
		if (nMostRecent.length == n) {
			break;
		}
	}
	return nMostRecent;
}

/** Add the specified path to the recent project file
 * 
 * @param {String} projPath 
 */
async function addToRecents(projPath) {
	const recentsLoc = path.resolve(app.getPath("userData"), "recents.txt");
	await fsp.appendFile(recentsLoc, projPath + "\n");
	return {};
}


async function getAbsolutePathToDatafile(metadataFilePath, metadata) {
	return path.resolve(path.dirname(metadataFilePath), metadata.datafile)
}



module.exports = { openBNOPIAlg, selectBNOPIOutputStageInstanceLocation, openStageFormat, saveStageFormat, getListOfStageInstance: getListOfStageInstance, openProjectFolderDialog, createNewProjectDialog, createNewProject, /*openProject,*/ getRecents, getProjectMetadata, addToRecents, getAbsolutePathToDatafile };