import React from 'react';
import { useCallback } from 'react';
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

const initialNodes = [
  { id: '1', position: { x: 0, y: 0 }, data: { label: '1' } },
  { id: '2', position: { x: 0, y: 100 }, data: { label: '2' } },
  { id: '3', position: { x: 100, y: 200 }, data: { label: '3' } }
];

const directed = {
    type: 'arrow', // 'arrow' or 'arrowclosed'
    strokeWidth: 6,
    color:'#000000'
  }

const initialEdges = [{ id: 'e1-2', source: '1', target: '2', type:'smoothstep', markerEnd:directed},
                        { id: 'e2-3', source: '2', target: '3', animated:true, style:{stroke:'red'}, markerEnd:directed}];

function DependencyGraph() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback((params) => setEdges((eds) => addEdge(params, eds)), [setEdges]);

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
    >
      {/* <Controls /> */}
      <Background />
    </ReactFlow>
  );
}

export default DependencyGraph;