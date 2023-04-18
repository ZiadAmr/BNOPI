import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBus, faPenToSquare, faRoute } from '@fortawesome/free-solid-svg-icons';
export default function NetworkToolKit() {

    function handleChange(newMode){
        //Get the 5 buttons
        var buttons = [document.getElementById("add_stop"), 
                    document.getElementById("remove_stop"), 
                    document.getElementById("add_route"), 
                    document.getElementById("remove_route"), 
                    document.getElementById("edit_route")];

        //Very very ugly code, couldnt be asked to fix it. Maybe get back to it later
        //Set the state of all other buttons to inactive
        for (let i = 0; i < buttons.length; i ++){
            if(i + 1 != newMode){
                if(buttons[i].className.slice(-6) === "active"){
                    buttons[i].toggleAttribute(false);
                    buttons[i].className = buttons[i].className.slice(0, -6);
                }
            }
        }

        //Finally call the function in the back-end to change the mode
        window.changeMode(newMode);
    }

  return (
    <>
        <ButtonGroup vertical id="Network_toolkit">
            <Button id= "add_stop" onClick={() => handleChange(1)} variant='secondary' data-bs-toggle="button" autoComplete="off" aria-pressed="false"><FontAwesomeIcon icon={faBus}></FontAwesomeIcon></Button>
            <Button id= "remove_stop" onClick={() => handleChange(2)} variant='secondary' data-bs-toggle="button" autoComplete="off" aria-pressed="false"><FontAwesomeIcon icon={faBus} id="icon1"></FontAwesomeIcon></Button>
            <Button id= "add_route" onClick={() => handleChange(3)} variant='secondary' data-bs-toggle="button" autoComplete="off" aria-pressed="false"><FontAwesomeIcon icon={faRoute}></FontAwesomeIcon></Button>
            <Button id= "remove_route" onClick={() => handleChange(4)} variant='secondary' data-bs-toggle="button" autoComplete="off" aria-pressed="false"><FontAwesomeIcon icon={faRoute} id="icon2"></FontAwesomeIcon></Button>
            <Button id= "edit_route" onClick={() => handleChange(5)} variant='secondary' data-bs-toggle="button" autoComplete="off" aria-pressed="false"><FontAwesomeIcon icon={faPenToSquare}></FontAwesomeIcon></Button>
        </ButtonGroup>
    </>
  )
}