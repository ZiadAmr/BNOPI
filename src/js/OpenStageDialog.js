import React, { useState, useEffect } from 'react';
import { List, ListItem, ListItemButton, ListItemText, Typography, ListItemIcon, IconButton, Tooltip, Dialog, DialogContent, DialogTitle, FormControl, InputLabel, NativeSelect, DialogActions, Button } from '@mui/material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPenNib, faBusSimple, faTrash, faFileLines } from '@fortawesome/free-solid-svg-icons';




/** Get a list of options for each requirement.
 * 
 * @param {string} mdPath Path to metadata file for query stage insatnce
 */
function getRequirementInstanceList(mdPath) {
	// 1. if there are any requirements, get the user to select those too. (speech bubble)
	// first look for the requirement in the metadata file. Recurr until one is found.	
	// do dfs.

	// find the number of requirements and the format of each
	/** @type {{path: string, metadata: InstanceMetadata, stageFormatInfo: StageFormatInfo|undefined}} */
	const ins = stageInstances.find(i => i.path == mdPath);

	const requirementFormats = [...new Set(ins.stageFormatInfo.requirements)];
	// list of lists.
	const requirements = new Array(requirementFormats.length).fill(0).map(() => []);

	const visitedInstances = [];

	// find index in `requirements` and add this 
	function addIfMatch(_ins) {
		const idxInReq = requirementFormats.indexOf(_ins.metadata.format);
		if (idxInReq != -1) {
			if (!requirements[idxInReq].some(i => i == _ins.path))
				requirements[idxInReq].push(_ins.path);
		}
	}

	function dfs(instancePath) {
		// ignore if already visited
		if (visitedInstances.some(e => e == instancePath)) return;

		// find stage instance
		/** @type {{path: string, metadata: InstanceMetadata, stageFormatInfo: StageFormatInfo|undefined}} */
		const ins = stageInstances.find(i => i.path == instancePath);

		// check if this is one of the required formats
		addIfMatch(ins);

		visitedInstances.push(instancePath);

		// siblings
		for (const sibling of ins.metadata.siblingStageInstancesAbs) {
			addIfMatch(stageInstances.find(i => i.path == sibling));
		}

		// recurr
		for (const parent of ins.metadata.parentStageInstancesAbs) {
			dfs(parent);
		}
	}

	dfs(mdPath);

	// add all other stage formats to the list (at the bottom)
	stageInstances.forEach(instance => {
		addIfMatch(instance);
	});

	// duplicate requirement list if necessary in case this stage format has multiple of the same type of requirement.
	return ins.stageFormatInfo.requirements.map(req => 
		requirements[requirementFormats.indexOf(req)]
	)
}

export default function OpenStageDialog(props) {


	const {onCancel, onClose, mdPath} = props;


	const ins = stageInstances.find(i => i.path == mdPath);

	if (mdPath == null) return <></>

	// create the dialog to open requirements (if there are any)
	const requirementInstanceList = getRequirementInstanceList(mdPath);

	// keeps track of the selected options in the list
	const [selectedRequirements, setSelectedRequirements] = useState(requirementInstanceList.map(options => options[0])); // default
	function handleSelectedOptionsChange(idx, newValue) {
		const newOptions = Array.from(selectedRequirements);
		newOptions[idx] = newValue;
		setSelectedRequirements(newOptions);
	}


	return <Dialog open={mdPath != null} onClose={onCancel}>
		<DialogTitle>Select Requirement Instances</DialogTitle>
		<DialogContent>
			{ins.stageFormatInfo.requirements.map((req, j) => {
				const options = requirementInstanceList[j];

				return <FormControl fullWidth key={j}>
					<InputLabel variant="standard" htmlFor="uncontrolled-native">
						{req}
					</InputLabel>
					<NativeSelect
						defaultValue={options[0]}
						inputProps={{
							name: req,
							id: 'uncontrolled-native',
							onChange: (event) => handleSelectedOptionsChange(j, event.target.value)
						}}
					>
						{options.map((op, index) => {
							// make one option for each instance. Use the datafile name, as is displayed in the stage tracker.
							const datafile = stageInstances.find(i => i.path == op).metadata.datafile;
							return <option value={op} key={index}>{datafile}</option>
						})}
					</NativeSelect>
				</FormControl>
			})}
		</DialogContent>
		<DialogActions>
			<Button onClick={onCancel}>Cancel</Button>
			<Button onClick={() => onClose(selectedRequirements)}>Open</Button>
		</DialogActions>
	</Dialog>

}