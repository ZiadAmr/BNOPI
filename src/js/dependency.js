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
        "parents": parents,
    })
    return dpgraph;
}

export function getdpgraph(){
    return dpgraph;
}

export function deleteStage(id){
    lst = []
    pairs = []
    dpgraph.forEach((x,i) => {
        if(x.id == id){
            x.parents.forEach((y,i)=>{
                pairs.push(y + "-" + x.id)
            })

            dpgraph.splice(i, 1)
            lst.push(x.id)
        }
    })
    // remove deleted node from parents, and remove unconnected nodes
    let unchanged = false
    while(unchanged == false){
        unchanged = true
        dpgraph.forEach((x,i) => {

            x.parents.forEach((z,i) => {
                lst.forEach((y,i) => {
                    if(y == z){
                        pairs.push(y + "-" + x.id)
                    }
                })
            })

            x.parents = x.parents.filter(function(item) { 
                return lst.indexOf(item) < 0; // Returns true for items not found in b.
            });
            if(x.parents.length == 0 & x.id != "1"){
                lst.push(x.id)
                dpgraph.splice(i, 1)
                unchanged = false
            }
        })
    }

    return [lst, pairs]
}


export function addParam(id, value) {
    memory[id] = value
}

export function changeFilename(id, filename) {
    dpgraph.find(element => element.id == id).filename = filename
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


addStage(1, "example", true, "python-scripts/example.py")

addStage(2, "secondexample", false, "python-scripts/io.py", ["param1", "param2"], [1])

addStage(3, "thirdexample", false, "python-scripts/example.py", parents=[example,secondexample])


// out = deleteStage(3)
console.log(out)

