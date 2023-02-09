import React, { useCallback } from 'react';
import { Handle, Position } from 'reactflow';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBus, faPenToSquare, faRoute, faStop, faPlus, faMinus } from '@fortawesome/free-solid-svg-icons';
import { Button } from 'react-bootstrap';
import { v4 as uuidv4 } from 'uuid';

const handleStyle = { left: 10 };

export default function Node2({ data }) {
  const onChange = useCallback((evt) => {
    // console.log(evt.target.value);
  }, []);

  return (
    <div className='depNode'>
      <Handle type="target" position={Position.Left} />
      <div>
        <label htmlFor="text" className='nodeLabel'>Algorithm name:</label>
        <label htmlFor="text" className='nodeLabel'>Script path:</label>
        <Button variant ='danger' id="breakPoint2" size= 'sm'><FontAwesomeIcon icon={faStop}/></Button>
        <Button variant ='secondary' id="addNode2" onClick={() => data.addNewNode(data.label, uuidv4())} size= 'sm'><FontAwesomeIcon icon={faPlus}/></Button>
        {/* <input id="text" name="text" onChange={onChange} /> */}
      </div>
      <Handle type="source" position={Position.Right} id="a" />
    </div>
  );
}

