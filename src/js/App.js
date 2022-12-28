
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import NetworkToolKit from './NetworkToolKit';
import DependencyGraph from './DependencyGraph';

export default function App() {

  return (
    <>
      <Container fluid id="mainContainer">
        <Row id="firstRow">
          <Col sm={10} id="mapContainer">
            <div id="map"></div>
            <NetworkToolKit></NetworkToolKit>
          </Col>
          <Col sm id="Description">description</Col>
        </Row>

        <Row id="secondRow">
          <Col sm={10} id="Dependency graph">
            <DependencyGraph></DependencyGraph>
          </Col>
          <Col sm id="StageTracker">Stage tracker</Col>
        </Row>
      </Container>
    </>
  )
}
