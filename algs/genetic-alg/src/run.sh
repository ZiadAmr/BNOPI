for i in {1..2}
do 
    build/genetic_alg ../../projects/test_project/stage_instances/stops.json ../../projects/test_project/stage_instances/stop-connection-graph.json ../../projects/test_project/stage_instances/od-matrix.json >> $1
done
echo "Finished"