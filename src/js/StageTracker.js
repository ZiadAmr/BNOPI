import React, { useState, useEffect } from 'react';
import { List, ListItem, ListItemButton, ListItemText, Typography, ListItemIcon, IconButton, Tooltip } from '@mui/material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPenNib, faBusSimple, faTrash, faFileLines } from '@fortawesome/free-solid-svg-icons';


export default function StageTracker() {
	const [selectedIndex, setSelectedIndex] = React.useState(-1);
	const [stages, setStages] = useState(false);

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

	/**
	 * Contents of a stage instance metadata file
	 * @typedef {{timeCreated: string, dependencyGraph: string, format: string, generatedBy: string, nodeInGraph:(number|null), parentStageInstances:string[], siblingStageInstances:string[], datafile:string}} InstanceMetadata
	 */


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
				// click button to load stage instance. needs to:
				// 1. if there are any requirements, get the user to select those too. (speech bubble)
				// first look for the requirement in the metadata file. Recurr until one is found.	


				// 2. load the stage instance
				const requirementMetadataPaths = []; // TODO
				window.dispatchEvent(new CustomEvent("displayStageInstance", {
					detail: {
						instanceMetdataPath: path,
						requirementMetadataPaths: requirementMetadataPaths
					}
				}));
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
			return stageInstanceButton;
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
		</div>
	)
}



