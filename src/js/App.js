
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import NetworkToolKit from './NetworkToolKit';
import DependencyGraph from './DependencyGraph';
import Description from './Description';

export default function App() {

  return (
    <>
      <Container fluid id="mainContainer">
        <Row id="firstRow">
          <Col sm={9} id="mapContainer">
            <div id="map"></div>
            <NetworkToolKit></NetworkToolKit>
          </Col>
          <Col sm id="Description">
            <Description></Description>
          </Col>
        </Row>

        <Row id="secondRow">
          <Col sm={9} id="Dependency_graph">
            <DependencyGraph></DependencyGraph>
          </Col>
          <Col sm id="StageTracker" style={{backgroundColor:'#3e3e3e'}}>Stage tracker</Col>
        </Row>
      </Container>
    </>
  )
}
