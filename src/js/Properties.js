import React, { useState, useEffect, useCallback } from 'react';
import { Typography, TextField, Button, Autocomplete, Select, MenuItem, IconButton, InputAdornment } from '@mui/material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFile } from '@fortawesome/free-solid-svg-icons';

export default function Properties() {
  const [prop, setProp] = useState('-1');
  const [value, setValue] = useState('');
  const [node, setNode] = useState('');
  const [description, setDescription] = useState('');
  const [autocompletevalues, setautocompletevalues] = useState({});
  const [positiveIntegers, setpositiveintegers] = useState({});
  const [outputLocs, setOutputLocs] = useState({});
  const [path, setPath] = useState('');
  const [stages, setStages] = useState({});
  const [type, setType] = useState('');

  useEffect(() => {
    const handle_properties_change = (event) => {
      if(event.detail.type === 'dependency_node'){
        setProp(event.detail.id);
        const node_id = dpgraph.find(obj => obj.id === event.detail.id);
        setValue(node_id.name);
        setNode(node_id);
        setPath(node_id.file.bash);
        setDescription(node_id.description);
        setType('dependency_node');
      }else if(event.detail.type === 'Route_draw'){
        setType('Route_draw');
      }
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
      var stage_change = new CustomEvent('change_state', {detail: {id: prop, name:event.target.value, script:path}});
      window.dispatchEvent(stage_change);
  }

  const handle_desc_change = (event) => {
    setDescription(event.target.value);
    var node_id = dpgraph.find(obj => obj.id === prop)
    node_id.description = event.target.value
  }

  const handleScriptLoad = useCallback(async (item) =>{
    var node_to_update = dpgraph.find(obj => obj.id === prop);
    node_to_update.location = item.path
    node_to_update.description = item.meta.description
    node_to_update.file = item.meta.launchScript
    node_to_update.input_stage_formats = item.meta.inputStageFormats
    node_to_update.output_stage_formats = item.meta.outputStageFormats 
    node_to_update.name = item.meta.name
    node_to_update.params = item.meta.params

    // Add new field to parameters
    let val = dpgraph.find(element => element.id === prop)
    const new_parameter_update = {...autocompletevalues}
    const new_posint_update = {...positiveIntegers}
    const new_selections = {...stages}
    const new_outputs = {...outputLocs}

    val.params.forEach((x,i) =>{
        x.setVal = x.default
        if(x.type === "dropdown"){
          const options = x.choices
          new_parameter_update[node_to_update.id.toString() + " " + i.toString()] = options.find(option => option === x.default)
        }else if(x.type === "posint"){
          new_posint_update[node_to_update.id.toString() + " " + i.toString()] = x.default
        }
    })

    val.input_stage_formats.forEach((x,i) =>{
      x.setStage = undefined
      new_selections[x.name.toString() + " " + i.toString() + " " + node_to_update.id.toString() + " " + "Stage_instance_select"] = ''
    })

    val.output_stage_formats.forEach((x,i)=> {
      x.setLoc = undefined
      new_outputs[i.toString() + " " + node_to_update.id.toString() + "stage_instance_output"]
    })

    setStages(new_selections);
    setpositiveintegers(new_posint_update);
    setautocompletevalues(new_parameter_update);
    setOutputLocs(new_outputs);
    setValue(node_to_update.name);
    setPath(node_to_update.file.bash);
    setDescription(node_to_update.description);
    var stage_change = new CustomEvent('change_state', {detail: {id: prop, name:node_to_update.name, script:node_to_update.file.bash}});
    window.dispatchEvent(stage_change);
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

  const handleSelectionChange = (info, index, value) => {
    const objToChange = dpgraph.find(obj => obj.id === info)
    if(value != null){
      objToChange.input_stage_formats[index].setStage = value
    }else{
      objToChange.input_stage_formats[index].setStage = null
    }
  };

  const select_output_location = useCallback(async (item, id, node_id, index) => {
    if(item.status === "ok"){
      dpgraph.find(obj => obj.id === node_id).output_stage_formats[index].setLoc = item.path
      const change_values = {...outputLocs}
      change_values[id] = item.path
      setOutputLocs(change_values)
    }
  },[prop]);

  function construct_param(item, index, info){
    if(item.type === "dropdown"){

      return <div key={index} style={{ display: 'flex', justifyContent: 'left', marginTop: '2px'}}>
        <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '12px', paddingLeft: '10px', paddingRight: '10px' }}>
          {index + 1}. {item.name} :
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
          {index + 1}. {item.name} :
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

  function construct_input_stage(item, index, info){
    const possible_stages = stageInstances.filter(stage => stage.metadata.format === item.stage_format);

    return <div key= {index.toString() + " " + info.toString() + " stage_instance"} style={{ display: 'flex', alignItems: 'center', paddingTop:'15px'}}>
      <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '6px', paddingLeft: '10px', paddingRight:'4px' }}>
        {index + 1}. {item.name} :
      </Typography>

      <Select
        labelId="selection"
        id="selection_prompt"
        value={stages[item.name.toString() + " " + index.toString() + " " + info.id.toString() + " " + "Stage_instance_select"]}
        label={item.name}
        onChange={(event, value) => {
          const values = {...stages};
          values[item.name.toString() + " " + index.toString() + " " + info.id.toString() + " " + "Stage_instance_select"] = value.props.children;
          setStages(values);
          handleSelectionChange(info.id, index.toString(), value.props.children)
        }}
        inputProps={{ style: { color: 'white', textAlign:'center' } }}
        style={{ width: '70%', height: '15%', backgroundColor: '#7aa2bd33', borderRadius: '8px', color:'white' }}
        >
          {possible_stages.map((element, i) => (
            <MenuItem key={"Random_key" + " " + i.toString() + " "+ index.toString() + " Menu item"}
            value={element.metadata.datafile}>
              {element.metadata.datafile}
            </MenuItem>
          ))}

      </Select>
    </div>
  }

  function construct_output_stage(item, index, info){

    return <div key= {item.name.toString() + " " + index.toString() + " " + info.id.toString() + " stage_instance_output"}>
      <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '20px', paddingLeft: '10px' }}>
        {index + 1}. {item.name}
      </Typography>
      <div style={{ display: 'flex', justifyContent: 'center', paddingTop:'15px'}}>
        <TextField
              variant="outlined"
              style={{ width: '80%', height: '15%', backgroundColor: '#7aa2bd33', borderRadius: '8px'}}
              value={outputLocs[item.name.toString() + " " + index.toString() + " " + info.id.toString() + " stage_instance_output"] || ''}
              inputProps={{ style: { color: 'white', textAlign:'center' } }}
              InputProps={{ style: { borderColor: 'white' }, readOnly: true, endAdornment:(
                <InputAdornment position='end'>
                  <IconButton onClick={async() => select_output_location(await window.electron.openBNOPIDir(), 
                    item.name.toString() + " " + index.toString() + " " + info.id.toString() + " stage_instance_output",
                    info.id.toString(),
                    index)}>
                    <FontAwesomeIcon icon={faFile} />
                  </IconButton>
                </InputAdornment>
              )}}
              InputLabelProps={{style: { color: "#ffffff94" }}}
        />
      </div>
    </div>
    
  }
  

  let prop_node = null;

  if (type === '') {
    prop_node = <Typography>Select element to view properties</Typography>;
  }else if(type === 'Route_draw'){
    
  }else {

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
              value={path || ''}
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
          <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '20px', paddingLeft: '10px', fontWeight:'bold' }}>
            Algorithm parameters
          </Typography>
          <div>
            {
            node.params != undefined &&
            node.params.map((item, index) => {
              return construct_param(item, index, node);
            })}
          </div>

          <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '20px', paddingLeft: '10px', fontWeight:'bold' }}>
            Input stage instances
          </Typography>
          <div>
            {
              node.input_stage_formats != undefined &&
              node.input_stage_formats.map((item, index) => {
                return construct_input_stage(item, index, node);
            })}
          </div>

          <Typography variant="h6" gutterBottom style={{ textAlign: 'left', fontSize: 17, fontFamily: 'sans-serif', paddingTop: '20px', paddingLeft: '10px', fontWeight:'bold' }}>
            Output stage instances location
          </Typography>
          <div>
            {
              node.output_stage_formats != undefined &&
              node.output_stage_formats.map((item, index) => {
                return construct_output_stage(item, index, node);
            })}
          </div>


        </div>

        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px', marginBottom:'20px'}}>
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
