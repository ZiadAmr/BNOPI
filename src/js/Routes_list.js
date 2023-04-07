import React, {useState, useEffect} from 'react';
import {List, ListItem, ListItemText, ListItemButton, Typography, ListItemIcon, IconButton} from '@mui/material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPenNib, faRoute, faTrash } from '@fortawesome/free-solid-svg-icons';

export default function Routes_list() { 
  const items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6'];
  const [selectedIndex, setSelectedIndex] = React.useState(-1);

  const handleListItemClick = (event, index) => {
    setSelectedIndex(index);
  };

  return (
    <>
      <Typography variant="h6" gutterBottom style={{textAlign:'center', fontSize:17, fontFamily:'sans-serif', paddingTop:'20px'}}>
        List of routes
      </Typography>
      <List dense={true} style={{ maxHeight: 200, overflow: 'auto'}}>
        {items.map((item, index) => (
          <ListItemButton 
          style={selectedIndex === index ? {backgroundColor: '#c0c6c9a8', color: '#ffffff'} : null} 
          key={index} selected={selectedIndex === index} 
          onClick={(event) => handleListItemClick(event, index)}
          >
            <ListItemIcon>
                <FontAwesomeIcon icon={faRoute} style={{color:'#ffffff'}}/>
            </ListItemIcon>
            <ListItemText id='route_list' primary={item} style={{color:'ffffff'}}/>
            <IconButton>
              <FontAwesomeIcon icon={faTrash} style={{ color: '#ffffff', fontSize:17 }} />
            </IconButton>
            <IconButton>
              <FontAwesomeIcon icon={faPenNib} style={{ color: '#ffffff', fontSize:17 }} />
            </IconButton>
          </ListItemButton>
        ))}
      </List>
    </>
  )
}