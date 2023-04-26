
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Typography } from '@mui/material';
import { Col, Row, Container } from 'react-bootstrap';
import Box from '@mui/material/Box';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus } from '@fortawesome/free-solid-svg-icons';
import { faFolder } from '@fortawesome/free-regular-svg-icons'; 
import Button from '@mui/material/Button';
import logo from "../../icons/bnopi-logo.png";


export default function Welcome() {

	async function startNewProject() {
		const dir = await window.electron.createNewProjectDialog();
		if (dir.canceled) {
			return;
		}
		// actually create the prooject
		await window.electron.createNewProject(dir.filePath);
		await openProject(dir.filePath);
	};

	async function openExistingProject() {
		const project_loc = await window.electron.openProjectFolderDialog();
		switch (project_loc.status) {
			case "ok":
				// call another electron function to actually load the project.
				console.log("The project is located at " + project_loc.path)
				await openProject(project_loc.path);
				break;

			case "not_project":
			case "cancelled":
			default:
				break;
		}
	}

	async function openProject(projPath) {
		await window.electron.sendOpenProjectSignal(projPath);
	}

	return (
		<div>
			<img src={logo} width="200px" />
			<Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 30, fontFamily: 'sans-serif', color: "white", fontWeight: "bold" }}>
				Welcome to BNOPI
			</Typography>
			<Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 15, fontFamily: 'sans-serif', color: "white"}}>
				Bus Network Optimization and Planning Interface. Create a new project or open an existing one to begin.
			</Typography>
			<Container style={{ width: "100%", height: "200px", display: "flex", alignItems: "center" }} >
				<Row style={{ margin: 0, width: "100%" }}>
					<Col sm={6} style={{ display: 'flex', justifyContent: 'center', alignItems: "center", flexDirection: "column", height: "100%"}}>
						<Box sx={{ width: '100px', height: '100px', backgroundColor: "red" }}>
							<Button variant='danger' id="setting" size='sm' style={{ alignItems: "center", width: "100%", height: "100%" }} onClick={startNewProject}>
								<FontAwesomeIcon icon={faPlus} style={{ fontSize: "60px" }}/>
							</Button>
							<center>New</center>
						</Box>
					</Col>
					<Col sm={6} style={{ display: 'flex', justifyContent: 'center', alignItems: "center", flexDirection: "column" }}>
						<Box sx={{ width: '100px', height: '100px', backgroundColor: "red" }}>
							<Button variant='danger' id="setting" size='sm' style={{ alignItems: "center", width: "100%", height: "100%" }} onClick={openExistingProject}>
								<FontAwesomeIcon icon={faFolder} style={{ fontSize: "60px" }} />
								
							</Button>
							<center>Open</center>
						</Box>
					</Col>
				</Row>
			</Container>
		</div>
	)
}
