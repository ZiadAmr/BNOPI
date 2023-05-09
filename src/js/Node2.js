import React, { useCallback, useState, useEffect } from 'react';
import { Handle, Position } from 'reactflow';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGear, faStop, faPlus, faMapLocationDot } from '@fortawesome/free-solid-svg-icons';
import { Button } from 'react-bootstrap';
import { v4 as uuidv4 } from 'uuid';
import './map.js'

const handleStyle = { left: 10 };

export default function Node2({ data }) {
  const [name, setName] = useState('')
  const [script, setScript] = useState('')
  const [isDisabled, setIsDisabled] = useState(false);

  useEffect(() => {
    const handle_state_change = (event) => {
      if(event.detail.id.toString() === data.id.toString()){
        setName(event.detail.name);
        setScript(event.detail.script)
      }
    };

    const change_state_true = (event) => {
      setIsDisabled(true)
    }

    const change_state_false = (event) => {
      setIsDisabled(false)
    }

    window.addEventListener('change_state', handle_state_change);
    
    window.addEventListener('started_specifying', change_state_true);
    window.addEventListener('finished_specifying', change_state_false);

    return () => {
      window.removeEventListener('change_state', handle_state_change);
      window.removeEventListener('started_specifying', change_state_true);
      window.removeEventListener('finished_specifying', change_state_false);
    };
  }, []);

  const onChange = useCallback((evt) => {
    // console.log(evt.target.value);
  }, []);

  return (
    <div className='depNode'>
      <Handle type="target" position={Position.Left} />
      <div>
      <label htmlFor="text" className='nodeLabel' style={{ whiteSpace: 'nowrap', overflow:'hidden', textOverflow:'ellipsis' }}>Name: {name}</label>
        <label htmlFor="text" className='nodeLabel' style={{ whiteSpace: 'nowrap', overflow:'hidden', textOverflow: 'ellipsis' }}>Script: {script}</label>
        <Button variant ='secondary' id="setting" size= 'sm' onClick={() => data.propertyClick(data.id)}><FontAwesomeIcon icon={faGear}/></Button>
        <Button variant ='secondary' id="map_work_area_select" disabled={isDisabled} size= 'sm' onClick={(event) => {specifyRegion(event)}}><FontAwesomeIcon icon={faMapLocationDot}/></Button>
        <Button variant ='danger' id="addNode2" onClick={() => data.addNewNode(data.label, uuidv4())} size= 'sm'><FontAwesomeIcon icon={faPlus}/></Button>
      </div>
      <Handle type="source" position={Position.Right} id="a" />
    </div>
  );
}

