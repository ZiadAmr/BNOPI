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

const initialNodes = [
  { id: '1', type: 'nodeAlg', position: { x: 0, y: 100 }, data: { label: '1' } },
  { id: '2', type: 'nodeAlg', position: { x: 300, y: 100 }, data: { label: '2' } },
  { id: '3', type: 'nodeAlg', position: { x: 600, y: 100 }, data: { label: '3' } }
];

const directed = {
  type: 'arrow', // 'arrow' or 'arrowclosed'
  strokeWidth: 6,
  color:'#000000'
}

const nodeTypes = {nodeAlg : AlgorithmNode}

const initialEdges = [{ id: 'e1-2', source: '1', target: '2', type:'smoothstep', markerEnd:directed},
                        { id: 'e2-3', source: '2', target: '3', animated:true, style:{stroke:'red'}, markerEnd:directed}];

function DependencyGraph() {
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