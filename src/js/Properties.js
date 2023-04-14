import React, { useState, useEffect } from 'react';
import { List, ListItem, ListItemText, ListItemButton, Typography, ListItemIcon, IconButton, TextField, Button } from '@mui/material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPen, faPenNib, faRoute, faTrash } from '@fortawesome/free-solid-svg-icons';

export default function Properties() {
  const [prop, setProp] = useState('-1');
  const [value, setValue] = useState('');
  const [node, setNode] = useState('');
  const [changed, setChanged] = useState('false');

  useEffect(() => {
    const handle_properties_change = (event) => {
      setProp(event.detail.id);
      const node_id = dpgraph.find(obj => obj.id === event.detail.id);
      setValue(node_id.name);
      setNode(node_id);
    };

    window.addEventListener('showProperties', handle_properties_change);

    return () => {
      window.removeEventListener('showProperties', handle_properties_change);
    };
  }, []);

  const handleScriptLoad = (item) =>{
    node_to_update = dpgraph.find(obj => obj.id === prop);
    node_to_update.description = item.meta.description
    node_to_update.file = item.meta.launchScript
    node_to_update.input_stage_formats = item.meta.inputStageFormats
    node_to_update.output_stage_formats = item.meta.outputStageFormats 
    node_to_update.name = item.meta.name
    node_to_update.params = item.meta.params
    
  }
  

  let prop_node = null;
  console.log("rendering");
  if (prop === '-1') {
    prop_node = <Typography>Select element to view properties</Typography>;
  } else {
    prop_node = (
      <div>
        <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '20px', paddingLeft: '5px' }}>
          Name:
        </Typography>
        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px' }}>
          <TextField
            variant="outlined"
            style={{ width: '90%', height: '15%', backgroundColor: '#7aa2bd33', borderRadius: '8px'}}
            value={value}
            onChange={(event) => setValue(event.target.value)}
            inputProps={{ style: { color: 'white', textAlign:'center' } }}
            InputProps={{ style: { borderColor: 'white' } }}
          />
        </div>
        {node.file === undefined ? 
        <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '20px', paddingLeft: '5px' }}>Script: undefined</Typography>
         : 
        <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '20px' }}>
          Script location: {node.file}
        </Typography>}
        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px' }}>
          <Button variant="contained" onClick={async () => {handleScriptLoad(await window.electron.openBNOPIALG())}}>Select Script</Button>
        </div>

      </div>
    );
  }

  return (
    <>
      {prop_node}
    </>
  );
}
