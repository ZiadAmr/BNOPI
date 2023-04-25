import React, {useState, useEffect, useCallback} from 'react';
import {List, ListItem, ListItemText, ListItemButton, Typography, ListItemIcon, IconButton} from '@mui/material';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPen, faPenNib, faRoute, faTrash } from '@fortawesome/free-solid-svg-icons';

export default function Routes_list() { 
  const [selectedIndex, setSelectedIndex] = React.useState({});
  const [routes, setRoutes] = useState(false);
  

  useEffect(() =>{
    const handle_change_routes = () => {
      setRoutes(!routes)
      setSelectedIndex({})
    }

    window.addEventListener('routes_change', handle_change_routes);

    return () => {
      window.removeEventListener('routes_change', handle_change_routes);
      
    }
  }, [routes]);

  // Returns true initially and if all the list items are not selected
  const all_draw = () => {
    if(selectedIndex === {}){
      return true
    }else{
      return Object.values(selectedIndex).every((v) => v === false);
    }
  }

  // Updates the state of the route on the map (either draws on the map or not)
  const setRouteState = (val, state) => {
    val.links.forEach(pL => {
      pL.setMap(state);
    });
    val.continuityLinks.forEach(pL => {
        pL.setMap(state);
    });

    if(state != null){
      val.stops.forEach(stp => {
        active_stops.push(stp)
      })
    }
  };

  useEffect(()=>{
    active_stops = []
    if(all_draw()){
      window.dispatchEvent(new CustomEvent('displaying_routes', {detail: {status:false}}))
      routeMap.forEach((value, key) => {
        setRouteState(value, map);
      });

      busStops.forEach((value, key) => {
        value.setMap(map);
      })
    }else{
      window.dispatchEvent(new CustomEvent('displaying_routes', {detail: {status:true}}))
      routeMap.forEach((value, key) => {
        if(selectedIndex[key] === true){
          setRouteState(value, map);
        }else{
          setRouteState(value, null);
        }
      });

      busStops.forEach((value, key) => {
        if(active_stops.includes(key)){
          value.setMap(map);
        }else{
          value.setMap(null);
        }
      })
    }
  }, [selectedIndex])

  const handleListItemClick = useCallback((id) => {
    const new_click_vals = {...selectedIndex}
    if(new_click_vals[id] === true){
      new_click_vals[id] = false;
    }else{
      new_click_vals[id] = true;
    }

    setSelectedIndex(new_click_vals);

  },[selectedIndex]);

  var generate_listing = Array.from(routeMap).map(([key, item], index) => {
    return <ListItemButton style={selectedIndex[key] === true ? {backgroundColor: '#c0c6c9a8', color: '#ffffff'} : null} key={key} selected={selectedIndex[key] === true} onClick={() => handleListItemClick(key)}>
              <ListItemIcon>
                  <FontAwesomeIcon icon={faRoute} style={{color:'#ffffff'}}/>
              </ListItemIcon>
              <ListItemText id='route_list' primary={item.name} style={{color:'ffffff'}}/>
              <IconButton onClick={(event)=>{
                event.stopPropagation();
              }}>
                <FontAwesomeIcon icon={faPen} style={{ color: '#ffffff', fontSize:17 }} />
              </IconButton>
              <IconButton onClick={(event) => {
                event.stopPropagation();
                deleteDisplayRoute(key);
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