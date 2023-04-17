import React, { useState, useEffect, useCallback } from 'react';
import { List, ListItem, ListItemText, ListItemButton, Typography, ListItemIcon, IconButton, TextField, Button, Autocomplete } from '@mui/material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPen, faPenNib, faRoute, faTrash } from '@fortawesome/free-solid-svg-icons';

export default function Properties() {
  const [prop, setProp] = useState('-1');
  const [value, setValue] = useState('');
  const [node, setNode] = useState('');
  const [path, setPath] = useState('Unspecified');
  const [description, setDescription] = useState('');
  const [autocompletevalues, setautocompletevalues] = useState({});
  const [positiveIntegers, setpositiveintegers] = useState({});

  useEffect(() => {
    const handle_properties_change = (event) => {
      setProp(event.detail.id);
      const node_id = dpgraph.find(obj => obj.id === event.detail.id);
      setValue(node_id.name);
      setNode(node_id);
      setPath(node_id.file.bash);
      setDescription(node_id.description);
    };

    window.addEventListener('showProperties', handle_properties_change);

    return () => {
      window.removeEventListener('showProperties', handle_properties_change);
    };
  }, []);

  const handle_name_change = (event) => {
      setValue(event.target.value);
      const node_id = dpgraph.find(obj => obj.id === prop)
      node_id.name = event.target.value
  }

  const handle_desc_change = (event) => {
    setDescription(event.target.value);
    var node_id = dpgraph.find(obj => obj.id === prop)
    node_id.description = event.target.value
  }

  const handleScriptLoad = useCallback(async (item) =>{
    var node_to_update = dpgraph.find(obj => obj.id === prop);
    node_to_update.description = item.meta.description
    node_to_update.file = item.meta.launchScript
    node_to_update.input_stage_formats = item.meta.inputStageFormats
    node_to_update.output_stage_formats = item.meta.outputStageFormats 
    node_to_update.name = item.meta.name
    node_to_update.params = item.meta.params

    // Add new field to parameters
    let val = dpgraph.find(element => element.id === prop).params
    const new_parameter_update = {...autocompletevalues}
    const new_posint_update = {...positiveIntegers}
    val.forEach((x,i) =>{
        x.setVal = x.default
        if(x.type === "dropdown"){
          const options = x.choices
          new_parameter_update[node_to_update.id.toString() + " " + i.toString()] = options.find(option => option === x.default)
        }else if(x.type === "posint"){
          new_posint_update[node_to_update.id.toString() + " " + i.toString()] = x.default
        }
    })
    setpositiveintegers(new_posint_update);
    setautocompletevalues(new_parameter_update);
    setValue(node_to_update.name);
    setPath(node_to_update.file.bash);
    setDescription(node_to_update.description);
  }, [prop]);


  const handleAutocompleteChange = (info, index, value) => {
    const objToChange = dpgraph.find(obj => obj.id === info)
    if(value != null){
      objToChange.params[index].setVal = value
    }else{
      objToChange.params[index].setVal = null
    }
  };

  const handlePositiveChange = (info, index, value) => {
    const objToChange = dpgraph.find(obj => obj.id === info)
    if(value != null){
      objToChange.params[index].setVal = value
    }else{
      objToChange.params[index].setVal = null
    }
  };


  function construct_param(item, index, info){
    if(item.type === "dropdown"){

      return <div key={index} style={{ display: 'flex', justifyContent: 'left', marginTop: '2px'}}>
        <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '12px', paddingLeft: '10px', paddingRight: '10px' }}>
          {item.name} :
        </Typography>

        <Autocomplete
          disablePortal
          options={item.choices}
          id="comboBox"
          value= {autocompletevalues[info.id.toString() + " " + index.toString()]}
          onChange={(event, value) => {
            const values = {...autocompletevalues};
            values[info.id.toString() + " " + index.toString()] = value;
            setautocompletevalues(values);
            handleAutocompleteChange(info.id, index.toString(), value)
          }}
          style={{backgroundColor: '#7aa2bd33', width: '40%'}}
          renderInput={(params) => {
            return <TextField {...params}/>}}
        />
      </div>
    }else if(item.type === "posint"){
      return <div key={index} style={{ display: 'flex', justifyContent: 'left', marginTop: '10px'}}>
        <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '12px', paddingLeft: '10px', paddingRight: '10px' }}>
          {item.name} :
        </Typography>
        <TextField
            type={"number"}
            value= {positiveIntegers[info.id.toString() + " " + index.toString()]}
            onChange={(event) =>{
                event.target.value < 0
                    ? (event.target.value = 0)
                    : event.target.value;
                const values = {...positiveIntegers};
                values[info.id.toString() + " " + index.toString()] = event.target.value;
                setpositiveintegers(values);
                handlePositiveChange(info.id, index.toString(), event.target.value)
            }}
            inputProps={{ style: { color: 'white', textAlign:'center' } }}
            style={{ width: '30%', height: '15%', backgroundColor: '#7aa2bd33', borderRadius: '8px', color:'white'}}
        />
      </div>
    }
  };
  

  let prop_node = null;

  if (prop === '-1') {
    prop_node = <Typography>Select element to view properties</Typography>;
  } else {

    prop_node = (
      <div>
        {/* <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '20px', paddingLeft: '5px' }}>
          Name:
        </Typography> */}
        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px' }}>
          <TextField
            label={"Name"}
            variant="outlined"
            style={{ width: '90%', height: '15%', backgroundColor: '#7aa2bd33', borderRadius: '8px'}}
            value={value}
            onChange={(event) => handle_name_change(event)}
            inputProps={{ style: { color: 'white', textAlign:'center' } }}
            InputProps={{ style: { borderColor: 'white' } }}
            InputLabelProps={{style: { color: "#ffffff94" }}}
          />
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
          <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px' }}>
            <TextField
              label={"Script"}
              variant="outlined"
              style={{ width: '90%', height: '15%', backgroundColor: '#7aa2bd33', borderRadius: '8px'}}
              value={path}
              inputProps={{ style: { color: 'white', textAlign:'center' } }}
              InputProps={{ style: { borderColor: 'white' }, readOnly: true }}
              InputLabelProps={{style: { color: "#ffffff94" }}}
            />
          </div>
          <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px' }}>
            <TextField
              variant="outlined"
              multiline
              maxRows={4}
              style={{ width: '90%', height: '30%', backgroundColor: '#7aa2bd33', borderRadius: '8px'}}
              label={"Description"}
              value={description}
              onChange={(event) => handle_desc_change(event)}
              inputProps={{ style: { color: 'white', textAlign:'center' } }}
              InputProps={{ style: { borderColor: 'white' }}}
              InputLabelProps={{style: { color: "#ffffff94" }}}
            />
          </div>

          {/* Parameters for the algorithm */}
          <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '20px', paddingLeft: '10px' }}>
            Algorithm parameters
          </Typography>
          <div>
            {
            node.params != undefined &&
            node.params.map((item, index) => {
              return construct_param(item, index, node);
            })}
          </div>

          {/* Input stage instances for the algorithm */}
          <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '20px', paddingLeft: '10px' }}>
            Input stage instances
          </Typography>


        </div>

        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px', overflow:'hidden' }}>
          <Button variant="contained" onClick={async () => {handleScriptLoad(await window.electron.openBNOPIALG())}}>Select Script</Button>
        </div>

      </div>
    );
  }

  return (
    <div>
      {prop_node}
    </div>
  );
}
