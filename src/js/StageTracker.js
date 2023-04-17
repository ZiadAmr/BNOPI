import React, { useState, useEffect } from 'react';
import { List, ListItem, ListItemButton, ListItemText, Typography, ListItemIcon, IconButton, Tooltip, Dialog, DialogContent } from '@mui/material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPenNib, faBusSimple, faTrash, faFileLines } from '@fortawesome/free-solid-svg-icons';
import OpenStageDialog from './OpenStageDialog';

/**
 * Contents of a stage instance metadata file
 * @typedef {{timeCreated: string, dependencyGraph: string, format: string, generatedBy: string, nodeInGraph:(number|null), parentStageInstances:string[], siblingStageInstances:string[], datafile:string}} InstanceMetadata
 */


// called on successful + uncancelled open.
function dispatchOpenEvent(instanceMetdataPath, requirementMetadataPaths) {
	window.dispatchEvent(new CustomEvent("displayStageInstance", {
		detail: {
			instanceMetdataPath: instanceMetdataPath,
			requirementMetadataPaths: requirementMetadataPaths
		}
	}));
}




export default function StageTracker() {
	const [selectedIndex, setSelectedIndex] = React.useState(-1);
	const [stages, setStages] = useState(false);
	// const [dialogOpen, setDialogOpen] = React.useState(false);
	const [dialogPath, setDialogPath] = React.useState(null);

	// for OpenStageDialog
	function cancelDialog() {
		setDialogPath(null)	}

	function closeDialog(selectedRequirements) {
		dispatchOpenEvent(dialogPath, selectedRequirements);
		setDialogPath(null)
	}


	const handleListItemClick = (event, index) => {
		setSelectedIndex(index);
	};

	useEffect(() => {
		const handle_change = () => {
			setStages(!stages)
		}

		window.addEventListener('stage_instances_change', handle_change);

		return () => {
			window.removeEventListener('stage_instances_change', handle_change);
		}
	}, [stages]);




	var generate_listing = Array.from(stageInstances).map(({ path, /** @type {InstanceMetadata} */ metadata, stageFormatInfo }, index) => {




		// if there is no stage format for this loaded make it a different color.
		const disabled = (typeof stageFormatInfo == "undefined");

		const stageInstanceButton = <ListItemButton style={selectedIndex === index ? { backgroundColor: '#c0c6c9a8', color: '#ffffff' } : null}
			disabled={disabled}
			selected={selectedIndex === index}
			onClick={(event) => {
				handleListItemClick(event, index);
			}}
			key={index}
			onDoubleClick={async (event) => {
				// click button to load stage instance.
				// if there are any requirements open a dialog box
				if (stageFormatInfo.requirements.length > 0) {
					setDialogPath(path);
				} else {
					dispatchOpenEvent(path, []);
				}
				
			}}>
			<ListItemIcon>
				<FontAwesomeIcon icon={faFileLines} style={{ color: '#ffffff' }} />
			</ListItemIcon>
			<ListItemText id='stage_instances_list' primary={`${metadata.datafile} (${metadata.format})`} style={{ color: 'ffffff' }} />
		</ListItemButton>


		if (disabled) {
			return <Tooltip title="Unrecognized stage format" placement="top" key={index} >
				<span>
					{stageInstanceButton}
				</span>
			</Tooltip>
		} else {
			return <span>{stageInstanceButton}</span>;
		}


	});


	return (
		<div>
			<Typography variant="h6" gutterBottom style={{ textAlign: 'center', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '20px' }}>
				Stage Tracker
			</Typography>
			<List dense={true} style={{ maxHeight: '100%', overflow: 'auto' }}>
				{generate_listing}
			</List>
			<OpenStageDialog onCancel={cancelDialog} onClose={closeDialog} mdPath={dialogPath} />
		</div>
	)
}



