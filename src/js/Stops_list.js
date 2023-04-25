import React, {useState, useEffect, useCallback} from 'react';
import ReactDOMServer from 'react-dom/server';
import {List, ListItem, ListItemButton, ListItemText, Typography, ListItemIcon, IconButton} from '@mui/material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPenNib, faBusSimple, faTrash } from '@fortawesome/free-solid-svg-icons';

export default function Stops_list() { 
  const [selectedIndex, setSelectedIndex] = React.useState({});
  const [stops, setStops] = useState(false);
  const [infoWindows, setInfoWindows] = useState({})
  const [disabled, setDisabled] = useState(false);

  function returnInfo(id){
    const temp = busStops.get(id);
    return ReactDOMServer.renderToString(
    <div style={{color: 'black', display:'block'}}>
      <div>
        Name: {temp.name}
      </div>
      
      <div>
        Type: {temp.title}
      </div>
      
      <div>
        ID: {temp.id}
      </div>
    </div>);
  }

  const handleListItemClick = useCallback((id) => {

    const new_click_vals = {...selectedIndex}
    const new_info_windows = {...infoWindows}
    if(busStops.get(id) != undefined){
      if(new_click_vals[id] === true){
        new_click_vals[id] = false;
        new_info_windows[id].close();
        new_info_windows[id] = null;
      }else{
        new_click_vals[id] = true;
        // Info window to show information about the stop selected
        const info = new google.maps.InfoWindow({content:returnInfo(id)})
        info.open(map, busStops.get(id));
        new_info_windows[id] = info;
      }
  
      setSelectedIndex(new_click_vals);
      setInfoWindows(new_info_windows);
    }
  },[selectedIndex]);

  useEffect(() =>{
    const handle_change = () => {
      setStops(!stops)
      setSelectedIndex({})
      setInfoWindows({})
      setDisabled(false);
    }

    const handleRoutesDisplaying = (event) => {
      setDisabled(event.detail.status)
    }

    window.addEventListener('bus_stops_change', handle_change);
    window.addEventListener('displaying_routes', handleRoutesDisplaying);

    return () => {
      window.removeEventListener('bus_stops_change', handle_change);
      window.removeEventListener('displaying_routes', handleRoutesDisplaying);
    }
  }, [stops]);

  var generate_listing = Array.from(busStops).map(([key, item]) => {
    return <ListItemButton disabled={disabled} style={selectedIndex[key] === true ? {backgroundColor: '#c0c6c9a8', color: '#ffffff'} : null} key={key} selected={selectedIndex[key] === true} onClick={(event) => handleListItemClick(key)}>
              <ListItemIcon>
                  <FontAwesomeIcon icon={faBusSimple} style={{color:'#ffffff'}}/>
              </ListItemIcon>
              <ListItemText id='stops_list' primary={item.name} style={{color:'ffffff'}}/>
              <IconButton onClick={(event) => {
                event.stopPropagation();
                deleteDisplayStop(key);
              }}>
                  <FontAwesomeIcon icon={faTrash} style={{ color: '#ffffff', fontSize:17 }} />
              </IconButton>
          </ListItemButton>
  });
  

  return (
    <>
        <Typography variant="h6" gutterBottom style={{textAlign:'center', fontSize:17, fontFamily:'sans-serif', paddingTop:'20px'}}>
                List of stops
        </Typography>
        <List dense={true} style={{ maxHeight: 200, overflow: 'auto'}}>
            {generate_listing}
        </List>
    </>
  )
}