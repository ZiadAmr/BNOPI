

// check that the file io is working nicely

async function loadStageFormatsConsole() {
	const projectName = await window.electron.inputTextBox("Enter project name (folder name in /projects/): ");

	// function to get a list of stage instances and metadata
	const stageInstancesList = await window.electron.getListOfStageFormat(projectName);

	console.log(stageInstancesList.size() + " stage instances found:")
	console.log(stageInstancesList);
	const instIndex = parseInt(await window.electron.inputTextBox("Enter the index of instance you would like to open: "));

	const listEntry = stageInstancesList[instIndex];
	// listEntry.metadata at this point contains the parsed version of the metadata file, e.g. STOPS_1.stg.json.

	// get metadata and a buffer containing the instance:
	const stageFormatID = listEntry.metadata.format;
	const metadataFileLocation = listEntry.path;

	const openedStageInstance = await window.electron.openStageFormat(projectName, stageFormatID, metadataFileLocation);
	/* Object of the form:
	{
		data: data,
		metadata:metadata
	}
	(we already have the metadata but send it again)
	*/

	console.log(openedStageInstance);


}