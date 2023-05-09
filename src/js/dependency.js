const { memo } = require('react')
let memory = {}

// Add breakpoints

export function addStage(id, stageName, filename, parameters=[], parents=[], description, instage, location) {
    console.log("Adding new stage", stageName)
    dpgraph.push({
        "id": id,
        "name": stageName,
        "file": filename,
        "params": parameters,
        "parents": parents,
        "description": description,
        "input_stage_formats":instage,
        "output_stage_formats":[],
        "location":location
    })
    return dpgraph;
}

export function getdpgraph(){
    return dpgraph;
}

export function deleteStage(id){
    let lst = []
    let pairs = []
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

export async function runGraph() {
    let stages_run = []
    while(stages_run.length < dpgraph.length){
        let run = []
        dpgraph.forEach((x, i) => {
            if( x.parents.every( p => stages_run.find(e => e == p)) && x.id != stages_run){
                run.push(x)
            }
        });
        console.log("RUN: ", run)
        console.log(stages_run)
        // run.forEach(async (x,i) => await runScript(x.id, x.file, x.params, x.input_stage_formats, x.output_stage_formats))
        for(let x of run){
            await runScript(x.id, x.file, x.params, x.input_stage_formats, x.output_stage_formats)
        }
        run.forEach((x,i) => stages_run.push(x.id))
        console.log("loop", stages_run)
        // console.log("Stages Run: ", stages_run)
    }
    
    console.log("Stages Run: ", stages_run)
    window.reloadStageTracker(projectPath)
}

export async function runScript(id, script, params, isf, osf) {
    /*...*/
    // let args = [filename]
    let args = []
    let names = []
    console.log("Stages Instances: ", isf)
    console.log("Params: ", params)
    for (var i = 0; i < params.length; i++){
        names.push(params[i].var)
        if (params[i].setVal == undefined){
            args.push(params[i].default)
        } else {
            args.push(params[i].setVal)
        }
    }

    console.log(dpgraph)
    for (var i = 0; i < osf.length; i++){
        names.push(osf[i].var)
        args.push(osf[i].setLoc)
        // for (var j = 0; j < stageInstances.length; j++){
        //     if (osf[i].stage_format == stageInstances[j].metadata.format){
        //         args.push(stageInstances[j].path)
        //         names.push(osf[i].var)
        //     }
        // }
    }

    for (var i = 0; i < isf.length; i++){
        for (var j = 0; j < stageInstances.length; j++){
            // names.push(isf[i].var)
            // args.push(isf[i].setLoc)
            if (isf[i].setStage == stageInstances[j].metadata.datafile){
                args.push(stageInstances[j].metadata.datafileAbs)
                names.push(isf[i].var)
                break
            }
        }
    }
    // console.log("\t Input Stages: ", stageInstances)
    var python = await window.electron.spawn_child(script.python3, args, names, WORK_AREA_LAT, WORK_AREA_LON, WORK_AREA_RADIUS);

    return ""
}


// addStage(1, "example", true, "python-scripts/example.py")

// addStage(2, "secondexample", false, "python-scripts/io.py", ["param1", "param2"], [1])

// addStage(3, "thirdexample", false, "python-scripts/example.py", parents=[example,secondexample])


// // out = deleteStage(3)
// console.log(out)

