import React, { useState, useEffect } from 'react';
import { List, ListItem, ListItemButton, ListItemText, Typography, ListItemIcon, IconButton, Tooltip, Dialog, DialogContent } from '@mui/material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFolderClosed } from '@fortawesome/free-solid-svg-icons';
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




export default function RecentProjects() {
	const [selectedIndex, setSelectedIndex] = React.useState(-1);
	const [projects, setProjects] = useState(false);

	const handleListItemClick = (event, index) => {
		setSelectedIndex(index);
	};

	useEffect(() => {
		const handle_change = () => {
			setProjects(!projects)
		}

		window.addEventListener('recent_projects_change', handle_change);

		return () => {
			window.removeEventListener('recent_projects_change', handle_change);
		}
	}, [projects]);


	var generate_listing = Array.from(recents).map((recentPath, index) => {


		const recentName = recentPath.split('\\').pop().split('/').pop();

		// if there is no stage format for this loaded make it a different color.

		const stageInstanceButton = <ListItemButton style={selectedIndex === index ? { backgroundColor: '#c0c6c9a8', color: '#ffffff' } : null}
			selected={selectedIndex === index}
			onClick={(event) => {
				handleListItemClick(event, index);
			}}

			onDoubleClick={async (event) => {
				// click button to load stage instance.
				// if there are any requirements open a dialog box
				window.electron.sendOpenProjectSignal(recentPath);
			}}>
			<ListItemIcon>
				<FontAwesomeIcon icon={faFolderClosed} style={{ color: '#ffffff' }} />
			</ListItemIcon>
			<ListItemText id='stage_instances_list' primary={`${recentName}`} style={{ color: 'ffffff' }} />
		</ListItemButton>

		return <span key={index}>{stageInstanceButton}</span>;


	});

	return (
		<div>
			<Typography variant="h6" gutterBottom style={{ textAlign: 'center', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '20px' }}>
				Recent Projects
			</Typography>
			{((recents.length == 0) ? <>No recent projects. Click the "New" button to create one.</> : <List dense={true} style={{ maxHeight: '100%', overflow: 'auto' }}>
				{generate_listing}
			</List>)}
		</div>
	)
}



