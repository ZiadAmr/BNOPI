const { memo } = require('react')

let dpgraph = []
let memory = {}

// export const addStage = (stageName, filename, parameters=[], parents=[]) => {
//     dpgraph.push({
//         "name": stageName,
//         "file": filename,
//         "params": parameters,
//         "parents": parents
//     })
// }

export function addStage(id, stageName, filename, parameters=[], parents=[]) {
    dpgraph.push({
        "id": id,
        "name": stageName,
        "file": filename,
        "params": parameters,
        "parents": parents
    })
    return dpgraph;
}

export function getdpgraph(){
    return dpgraph;
}

// export function deleteStage(id){
//     delete dpgraph[id]
// }

export function addParam(id, value) {
    memory[id] = value
}

export function changeFilename(id, filename) {
    dpgraph[id].filename = filename
}

export function addParent(id, parentID) {
    dpgraph.find(element => element.id == id).parents.push(parentID)
}

export function runGraph() {
    stages_run = []
    while(stages_run.length < dpgraph.length){
        run = []
        dpgraph.forEach((x, i) => {
            if( x.parents.every( p => stages_run.find(e => e == p)) && x.id != stages_run){
                run.push(x)
            }
        });
        // console.log(run)
        run.forEach((x,i) => runScript(x.id, x.file, x.params))
        run.forEach((x,i) => stages_run.push(x.id))
        console.log("loop", stages_run)
        // console.log("Stages Run: ", stages_run)
    }
    
    console.log("Stages Run: ", stages_run)
}

export function runScript(id, filename, params) {
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
        memory[id] = data.toString()
        
        console.log("after:", memory)

        return data.toString()
    });
}

// runScript('python-scripts/example.py')

// addStage("example", "python-scripts/example.py")

// addStage("secondexample", "python-scripts/io.py", ["param1", "param2"], ["example"])
// addParam("param1", 1)
// addParam("param2", "food")

// runGraph()

