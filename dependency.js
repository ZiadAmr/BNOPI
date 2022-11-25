const { memo } = require('react')

dpgraph = []

memory = {}

function addStage(stageName, filename, parameters=[], parents=[]) {
    dpgraph.push({
        "name": stageName,
        "file": filename,
        "params": parameters,
        "parents": parents
    })
}

function addParam(name, value) {
    memory[name] = value
}

function runGraph() {
    stages_run = []
    while(stages_run.length < dpgraph.length){
        run = []
        dpgraph.forEach((x, i) => {
            if( x.parents.every( p => stages_run.find(e => e == p)) && x.name != stages_run){
                run.push(x)
            }
        });
        // console.log(run)
        run.forEach((x,i) => runScript(x.name, x.file, x.params))
        run.forEach((x,i) => stages_run.push(x.name))
        console.log("loop", stages_run)
        // console.log("Stages Run: ", stages_run)
    }
    
    console.log("Stages Run: ", stages_run)
}

function runScript(stageName, filename, params) {
    /*...*/
    args = [filename]
    console.log("Params = ", params)
    for (var i = 0; i < params.length; i++){
        args.push(memory[params[i]])
    }
    console.log(args, memory["param1"], memory["param2"])
    var python = require('child_process').spawn('python', args);
    python.stdout.on('data',function(data){
        console.log("data: ",data.toString());
        memory[stageName] = data.toString()
        
        console.log("after:", memory)

        return data.toString()
    });
}

// runScript('python-scripts/example.py')

addStage("example", "python-scripts/example.py")

addStage("secondexample", "python-scripts/io.py", ["param1", "param2"], ["example"])
addParam("param1", 1)
addParam("param2", "food")

runGraph()

