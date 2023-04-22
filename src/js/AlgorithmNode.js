import React, { useCallback, useEffect, useState } from 'react';
import { Handle, Position } from 'reactflow';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGear, faStop, faPlus, faMinus } from '@fortawesome/free-solid-svg-icons';
import { Button } from 'react-bootstrap';
import { v4 as uuidv4 } from 'uuid';

const handleStyle = { left: 10 };

export default function AlgorithmNode({ data }) {
  const [name, setName] = useState('')
  const [script, setScript] = useState('')

  useEffect(() => {
    const handle_state_change = (event) => {
      if(event.detail.id.toString() === data.id.toString()){
        setName(event.detail.name);
        setScript(event.detail.script)
      }
    };

    window.addEventListener('change_state', handle_state_change);

    return () => {
      window.removeEventListener('change_state', handle_state_change);
    };
  }, []);

  return (
    <div className='depNode'>
      <Handle type="target" position={Position.Left} />
      <div>
        <label htmlFor="text" className='nodeLabel' style={{ whiteSpace: 'nowrap', overflow:'hidden', textOverflow:'ellipsis' }}>Name: {name}</label>
        <label htmlFor="text" className='nodeLabel' style={{ whiteSpace: 'nowrap', overflow:'hidden', textOverflow: 'ellipsis' }}>Script: {script}</label>
        <Button variant ='secondary' id="setting" size= 'sm' onClick={() => data.propertyClick(data.id)}><FontAwesomeIcon icon={faGear}/></Button>
        <Button variant ='danger' id="breakPoint" size= 'sm'><FontAwesomeIcon icon={faStop}/></Button>
        <Button variant ='secondary' id="addNode" onClick={() => data.addNewNode(data.label, uuidv4())} size= 'sm'><FontAwesomeIcon icon={faPlus}/></Button>
        <Button variant ='secondary' id="deleteNode" onClick={()=> data.removeNode(data.label)} size= 'sm'><FontAwesomeIcon icon={faMinus}/></Button>
        {/* <input id="text" name="text" onChange={onChange} /> */}
      </div>
      <Handle type="source" position={Position.Right} id="a" />
    </div>
  );
}