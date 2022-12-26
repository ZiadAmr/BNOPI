import React from 'react';
import { useCallback } from 'react';
import { Button } from 'react-bootstrap';
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


const directed = {
  type: 'arrow', // 'arrow' or 'arrowclosed'
  strokeWidth: 6,
  color:'#000000'
}

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
    })
  }, []);

  const removeNode = useCallback((nodeID) => {
    setNodes((nodes)=>{
      console.log(nodes);
      console.log(nodeID);
      return nodes.filter(item=>item.id!=nodeID);
    })
  },[]);


  const initialNodes = [
    { id: '1', type: 'nodeAlg', position: { x: 50, y: 50 }, data: { label: '1', addNewNode:addNewNode, removeNode:removeNode} }];
  
  const initialEdges = [];

  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);


  const onConnect = useCallback((params) => setEdges((eds) => addEdge(params, eds)), [setEdges]);

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
    </>
  );
}

export default DependencyGraph;