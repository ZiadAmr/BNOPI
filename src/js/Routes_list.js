import React, {useState, useEffect} from 'react';
import {List, ListItem, ListItemText, ListItemButton, Typography, ListItemIcon, IconButton} from '@mui/material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPen, faPenNib, faRoute, faTrash } from '@fortawesome/free-solid-svg-icons';

export default function Routes_list() { 
  const [selectedIndex, setSelectedIndex] = React.useState(-1);
  const [routes, setRoutes] = useState(false);

  useEffect(() =>{
    const handle_change_routes = () => {
      console.log(routes);
      setRoutes(!routes)
    }

    const handleOutsideClick = (event) => {
      if (event.target.getAttribute("id") !== "routes_stops_content") {
        setSelectedIndex(-1);
      }
    };

    window.addEventListener('routes_change', handle_change_routes);
    window.addEventListener("click", handleOutsideClick);

    return () => {
      window.removeEventListener('routes_change', handle_change_routes);
      window.removeEventListener("click", handleOutsideClick);
    }
  }, [routes]);

  const handleListItemClick = (event, index) => {
    setSelectedIndex(index);
  };

  var generate_listing = Array.from(polyMap).map(([key, item], index) => {
    return <ListItemButton style={selectedIndex === index ? {backgroundColor: '#c0c6c9a8', color: '#ffffff'} : null} key={index} selected={selectedIndex === index} onClick={(event) => handleListItemClick(event, index)}>
              <ListItemIcon>
                  <FontAwesomeIcon icon={faRoute} style={{color:'#ffffff'}}/>
              </ListItemIcon>
              <ListItemText id='route_list' primary={item.name} style={{color:'ffffff'}}/>
              <IconButton>
                <FontAwesomeIcon icon={faPen} style={{ color: '#ffffff', fontSize:17 }} />
              </IconButton>
              <IconButton onClick={() => {
                item.setMap(null);
                polyMap.delete(key);
                window.dispatchEvent(new Event('routes_change'));
              }}>
                  <FontAwesomeIcon icon={faTrash} style={{ color: '#ffffff', fontSize:17 }} />
              </IconButton>
          </ListItemButton>
  });

  return (
    <>
      <Typography variant="h6" gutterBottom style={{textAlign:'center', fontSize:17, fontFamily:'sans-serif', paddingTop:'20px'}}>
        List of routes
      </Typography>
      <List dense={true} style={{ maxHeight: 200, overflow: 'auto'}}>
        {generate_listing}
      </List>
    </>
  )
}