
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import RecentProjects from './RecentProjects';
import Welcome from './Welcome';

export default function LaunchPage() {

	return (
		<>
			<Container fluid id="LaunchPage">
				<Row style={{ margin: 0,height: "100%", width: "100%"}}>
					<Col sm={3} id="RecentProjects" style={{ overflow: "auto", minWidth: '100px', width: '250px'}}>
						<RecentProjects></RecentProjects>
					</Col>
					<Col sm id="Welcome" style={{ overflow: "auto", maxHeight: '100%', display: "flex", alignItems: "center" }}>
						<Welcome></Welcome>
					</Col>
				</Row>
			</Container>
		</>
	)
}
