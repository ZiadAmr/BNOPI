
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import NetworkToolKit from './NetworkToolKit';
import DependencyGraph from './DependencyGraph';
import Description from './Description';
import StageTracker from './StageTracker';
import RouteDrawTools from './RouteDrawTools';
import RegionSelect from './RegionSelect';
import { Hidden } from '@mui/material';

export default function App() {

  return (
    <>
      <Container fluid id="mainContainer" style={{overflow:"hidden"}}>
        <Row id="firstRow">
          <Col sm={9} id="mapContainer">
            <div id="map"></div>
            <NetworkToolKit></NetworkToolKit>
            <RouteDrawTools></RouteDrawTools>
            <RegionSelect></RegionSelect>
          </Col>
          <Col sm id="Description" style={{ overflow: "auto", maxHeight:'100%' }}>
            <Description></Description>
          </Col>
        </Row>

        <Row id="secondRow">
          <Col sm={9} id="Dependency_graph">
            <DependencyGraph></DependencyGraph>
          </Col>
          <Col sm id="StageTracker" style={{ overflow: "auto", maxHeight:'100%' }}>
            <StageTracker></StageTracker>
          </Col>
        </Row>
      </Container>
    </>
  )
}
