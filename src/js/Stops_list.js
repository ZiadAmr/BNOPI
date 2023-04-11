import React, {useState, useEffect} from 'react';
import {List, ListItem, ListItemButton, ListItemText, Typography, ListItemIcon, IconButton} from '@mui/material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPenNib, faBusSimple, faTrash } from '@fortawesome/free-solid-svg-icons';

export default function Stops_list() { 
  const [selectedIndex, setSelectedIndex] = React.useState(-1);
  const [stops, setStops] = useState(false);

  const handleListItemClick = (event, index) => {
    setSelectedIndex(index);
  };

  useEffect(() =>{
    const handle_change = () => {
      setStops(!stops)
    }

    window.addEventListener('bus_stops_change', handle_change);

    return () => {
      window.removeEventListener('bus_stops_change', handle_change);
    }
  }, [stops]);

  var generate_listing = Array.from(busStops).map(([key, item], index) => {
    return <ListItemButton style={selectedIndex === index ? {backgroundColor: '#c0c6c9a8', color: '#ffffff'} : null} key={index} selected={selectedIndex === index} onClick={(event) => handleListItemClick(event, index)}>
              <ListItemIcon>
                  <FontAwesomeIcon icon={faBusSimple} style={{color:'#ffffff'}}/>
              </ListItemIcon>
              <ListItemText id='route_list' primary={item.name} style={{color:'ffffff'}}/>
              <IconButton onClick={() => {
                //console.log(busStops)
                console.log(item);
                item.setMap(null);
                busStops.delete(key);
                window.dispatchEvent(new Event('bus_stops_change'));
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