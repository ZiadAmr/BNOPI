import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Popover from 'react-bootstrap/Popover';

export default function RouteDrawTools() {
    const [displaying, setDisplaying] = useState(false);

    useEffect(() => {
        const handleChange = (event) => {
            setDisplaying(event.detail.status)
        };
    
        window.addEventListener('done_button', handleChange);
    
        return () => {
          window.removeEventListener('done_button', handleChange);
        };
    }, []);

    const popover = (
      <Popover id="popover-basic">
        <Popover.Header as="h3" style={{color:"black"}}>Route draw controls</Popover.Header>
        <Popover.Body>
          Left-click on the map to place a pathing point. Right click on map to create a bus stop.
        </Popover.Body>
      </Popover>
    );

  return (
    <>
      {displaying ? (
        <>
        <Button id='Route_drawing' onClick={() => {window.changeMode(0)}} variant="secondary">
          Done
        </Button>
        <OverlayTrigger trigger="click" placement="bottom" overlay={popover}>
          <Button id='Route_help' variant="secondary">Help</Button>
        </OverlayTrigger>
        </>
      ) : null}
    </>
  )
}