dpgraph = []

function addStage(stageName, filename, parameters=[], parents=[]) {
    dpgraph.push({
        "name": stageName,
        "file": filename,
        "params": parameters,
        "parents": parents
    })
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
        run.forEach((x,i) => runScript(x.file))
        run.forEach((x,i) => stages_run.push(x.name))
        console.log("loop", stages_run)
        // console.log("Stages Run: ", stages_run)
    }
    
    console.log("Stages Run: ", stages_run)
}

async function runScript(filename) {
    /*...*/
    var python = require('child_process').spawn('python', [filename]);
    python.stdout.on('data',function(data){
        console.log("data: ",data.toString());
        return data.toString()
    });
}

// runScript('python-scripts/example.py')

addStage("example", "python-scripts/example.py")
addStage("secondexample", "python-scripts/example.py", [], ["example"])

runGraph()

// console.log(dpgraph)