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
import Node2 from './Node2';

import './dependency.js';
import { addParam, addParent, addStage, deleteStage, getdpgraph, runGraph } from './dependency.js';

const directed = {
  type: 'arrow', // 'arrow' or 'arrowclosed'
  strokeWidth: 3,
  color: '#FFFFFF'
}

addStage("1", "Base node", {bash: 'print.sh', powershell: 'print.ps1', python3:'Unspecified'}, [], [], "", [], null)

const nodeTypes = { nodeAlg: AlgorithmNode, node: Node2 }

function DependencyGraph() {

  const show_properties = useCallback((id) => {
    var show_properties = new CustomEvent('showProperties', {detail: {id: id, type: 'dependency_node'}});
    window.dispatchEvent(show_properties)
  }, []);

  //Function used to create a new node when the user has clicked on the + button on a node
  const addNewNode = useCallback((prevNodeId, newNodeID) => {

    //Add a new node to the list of nodes
    setNodes((nodes) => {
      return [...nodes, {
        id: newNodeID, type: 'nodeAlg',
        position: { x: nodes.filter((item) => item.id == prevNodeId)[0].position.x + 300, y: nodes.filter((item) => item.id == prevNodeId)[0].position.y + (Math.random() * 300) - 150 },
        data: { label: newNodeID, addNewNode: addNewNode, removeNode: removeNode, propertyClick:show_properties, id:newNodeID, name:'New node'}
      }];
    });


    //Add a new edge from parent node to new node
    setEdges((edges) => {
      return [...edges, { id: prevNodeId + '-' + newNodeID, source: prevNodeId, target: newNodeID, type: 'default', animated: true, markerEnd: directed }]
    });


    //When a new node is added we need to update our backend to hold this data
    addStage(newNodeID, "New stage", {bash:'Unspecified', powershell:'', python3:'Unspecified'}, [], [prevNodeId], "", null);

  }, []);

  const removeNode = useCallback((nodeID) => {

    let deletions = deleteStage(nodeID);

    // Delete the nodes
    setNodes((nodes) => {
      return nodes.filter(item => !deletions[0].includes(item.id));
    });

    setEdges((edges) => {
      return edges.filter(item => !deletions[1].includes(item.id))
    });

  }, []);

  const initialNodes = [
    { id: '1', type: 'node', position: { x: 50, y: 50 }, data: { label: '1', addNewNode: addNewNode, propertyClick:show_properties, id:'1', name:'New node' } }];

  const initialEdges = [];

  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);


  // Function is called when we manually connect two nodes
  const onConnect = useCallback((params) => {
    setEdges((eds) => addEdge(params, eds))

    // Set the parent of the node in our backend
    addParent(params.target, params.source);
  }, [setEdges]);

  return (
    <>
      <ReactFlow
        nodeTypes={nodeTypes}
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        proOptions={{ hideAttribution: true }}
      >
        {/* <Controls /> */}
        {/* <Background /> */}
      </ReactFlow>
      <Button id="executeGraph" onClick={() => runGraph()} variant='secondary' data-bs-toggle="button" autoComplete="off" aria-pressed="false"><FontAwesomeIcon icon={faPlay} /></Button>
    </>
  );
}

export default DependencyGraph;