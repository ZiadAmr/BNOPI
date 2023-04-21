import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';

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

  return (
    <>
      {displaying ? (
        <Button id='Route_drawing' onClick={() => {window.changeMode(0)}} variant="secondary">
          Done
        </Button>
      ) : null}
    </>
  )
}