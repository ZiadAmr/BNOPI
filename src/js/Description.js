
import React, {useState, useEffect} from 'react';
import {Navbar, Nav, Tab} from 'react-bootstrap';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import { faZ } from '@fortawesome/free-solid-svg-icons';
import Routes_list from './routes_list';
import Stops_list from './Stops_list';


export default function Description() {

  const [key, setKey] = useState('Properties');


  return (

    <Tab.Container activeKey={key} onSelect={setKey}>
      <Nav variant="tabs" className='Navigation'>
        <Nav.Item style={{ width: '50%', fontSize:15 }}>
          <Nav.Link eventKey="Properties" style={{ textAlign: 'center'}}>Properties</Nav.Link>
        </Nav.Item>
        <Nav.Item style={{ width: '50%', fontSize:15 }}>
          <Nav.Link eventKey="Routes_and_Stops" style={{ textAlign: 'center'}}>Map info</Nav.Link>
        </Nav.Item>
      </Nav>
      <Tab.Content id='routes_stops_content'>
        <Tab.Pane eventKey="Properties">
          
        </Tab.Pane>
        <Tab.Pane eventKey="Routes_and_Stops">
          <Routes_list></Routes_list>
          <Stops_list></Stops_list>
        </Tab.Pane>
      </Tab.Content>
    </Tab.Container>
  )
}