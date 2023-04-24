import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Popover from 'react-bootstrap/Popover';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';


export default function RegionSelect() {
    const [displaying, setDisplaying] = useState(false);
    const [openDialog, setOpenDialog] = useState(false);

    useEffect(() => {
        const handleChange = (event) => {
            setDisplaying(true)
        };

        const handleError = (event) => {
            setOpenDialog(true)
        }
    
        window.addEventListener('started_specifying', handleChange);
        window.addEventListener('error_select_region', handleError)
    
        return () => {
          window.removeEventListener('started_specifying', handleChange);
          window.removeEventListener('error_select_region', handleError)
        };
    }, []);

    const handleErrorClose = () => {
        setOpenDialog(false);
    }

    const popover = (
      <Popover id="popover-basic">
        <Popover.Header as="h3" style={{color:"black"}}>Region selection controls</Popover.Header>
        <Popover.Body>
          Click on map to start specifying the region of the map to generate the network. Click again to finish drawing. 
          You can adjust the region by dragging the 5 dots on the circle. Once satisfied please click the done button to confirm.  
        </Popover.Body>
      </Popover>
    );

  return (
    <>
      {displaying ? (
        <>
        <Button id='Region_selection_done' onClick={(event) => {
            event.stopPropagation();
            setDisplaying(false);
            window.dispatchEvent(new Event("finished_specifying"));
        }} variant="secondary">
          Done
        </Button>
        <OverlayTrigger trigger="click" placement="bottom" overlay={popover}>
          <Button id='Region_selection_help' variant="secondary">Help</Button>
        </OverlayTrigger>
        </>
      ) : null}
      {/* In case the user doesnt specify region of the map correctly, throw an alert */}
      <Dialog
            open={openDialog}
            onClose={handleErrorClose}
            aria-labelledby="error_dialog"
            aria-describedby="error_dialog_content"
        >
            <DialogTitle id="error_dialog">
                {"Select area of the map"}
            </DialogTitle>
            <DialogContent>
            <DialogContentText id="error_dialog_content">
                Please select a valid region of the map to generate the bus network.
            </DialogContentText>
            </DialogContent>
            <DialogActions>
            <Button onClick={handleErrorClose}>Close</Button>
            </DialogActions>
        </Dialog>
    </>
  )
}