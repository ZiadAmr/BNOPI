async function runScript(filename) {
    /*...*/
    var python = require('child_process').spawn('python', [filename]);
    python.stdout.on('data',function(data){
        console.log("data: ",data.toString());
        return data.toString()
    });
}

runScript('python-scripts/example.py')

