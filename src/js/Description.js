
import React from 'react';
import {Navbar, Nav} from 'react-bootstrap';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';


export default function Description() {

  return (
    <Router id='Navigation'>
      <div>
        <Navbar bg="light" id ="bar">
          {/* <Navbar.Brand href="#">My App</Navbar.Brand> */}
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto justify-content-center nav-fill">
              <Nav.Link as={Link} to="/">Home</Nav.Link>
              <Nav.Link as={Link} to="/about">About</Nav.Link>
              <Nav.Link as={Link} to="/contact">Contact</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Navbar>

        {/* <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/contact">
            <Contact />
          </Route>
        </Switch> */}
      </div>
    </Router>
    // <div className="d-flex justify-content-around" id='Description_section'>
    //   <ButtonGroup style={{ flex: 1 }}>
    //     <Button variant='primary'>Properties</Button>
    //     <Button variant='primary'>Routes</Button>
    //     <Button variant='primary'>Stops</Button>
    //   </ButtonGroup>
    // </div>
  )
}