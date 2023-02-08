import React from 'react';
import { useCallback } from 'react';
import { Button } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlay } from '@fortawesome/free-solid-svg-icons';
import ReactFlow, {
  MiniMap,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  addEdge,
  SmoothStepEdge,
} from 'reactflow';

import 'reactflow/dist/style.css';
import AlgorithmNode from './AlgorithmNode';

import './dependency.js';
import { addParam, addParent, addStage, deleteStage, getdpgraph, runGraph } from './dependency.js';

const directed = {
  type: 'arrow', // 'arrow' or 'arrowclosed'
  strokeWidth: 3,
  color:'#FFFFFF'
}

addStage("1", "Base node")

const nodeTypes = {nodeAlg : AlgorithmNode}

function DependencyGraph() {
  //Function used to create a new node when the user has clicked on the + button on a node
  const addNewNode = useCallback((prevNodeId, newNodeID) => {

    //Add a new node to the list of nodes
    setNodes((nodes)=>{
      return [...nodes,{id: newNodeID, type: 'nodeAlg', 
      position: { x:nodes.filter((item)=>item.id == prevNodeId)[0].position.x + 300, y:nodes.filter((item)=>item.id == prevNodeId)[0].position.y + (Math.random() * 300) - 150}, 
      data: { label: newNodeID, addNewNode:addNewNode, removeNode:removeNode}}];
    });


    //Add a new edge from parent node to new node
    setEdges((edges)=>{
      return[...edges, {id:prevNodeId + '-' + newNodeID, source:prevNodeId, target:newNodeID, type:'default', markerEnd:directed}]
    });


    //When a new node is added we need to update our backend to hold this data
    addStage(newNodeID, "New stage", "path", [], [prevNodeId]);
    console.log(getdpgraph());

  }, []);

  const removeNode = useCallback((nodeID) => {

    let deletions = deleteStage(nodeID);

    // Delete the nodes
    setNodes((nodes)=>{
      return nodes.filter(item=>!deletions[0].includes(item.id));
    });

    setEdges((edges)=>{
      return edges.filter(item=>!deletions[1].includes(item.id))
    });

  },[]);


  const initialNodes = [
    { id: '1', type: 'nodeAlg', position: { x: 50, y: 50 }, data: { label: '1', addNewNode:addNewNode, removeNode:removeNode} }];
  
  const initialEdges = [];

  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);


  // Function is called when we manually connect two nodes
  const onConnect = useCallback((params) => { 
    setEdges((eds) => addEdge(params, eds))

    // Set the parent of the node in our backend
    addParent(params.target, params.source);
  } , [setEdges]) ;

  return (
    <>
      <ReactFlow
        nodeTypes={nodeTypes}
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        proOptions={{hideAttribution: true}}
      >
        {/* <Controls /> */}
        {/* <Background /> */}
      </ReactFlow>
      <Button id= "executeGraph" onClick={() => runGraph()} variant='secondary' data-bs-toggle="button" autoComplete="off" aria-pressed="false"><FontAwesomeIcon icon={faPlay} /></Button>
    </>
  );
}

export default DependencyGraph;