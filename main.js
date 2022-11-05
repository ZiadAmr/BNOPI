const electron = require("electron");
const url = require("url");
const path = require("path");

const { app, BrowserWindow, Menu } = electron;

let mainWindow;
let addWindow;

// listen for app to be ready
app.on('ready', function () {
    //Create new window
    mainWindow = new BrowserWindow({});
    //load html into into window
    mainWindow.loadURL(url.format({
        //pass the path of the file 
        pathname: path.join(__dirname, 'mainWindow.html'),
        protocol: 'file',
        slashes: true
    }));

    //quit app when closed
    mainWindow.on("closed", function () {
        app.quit();
    });

    //build menu from template
    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
    //insert menu
    Menu.setApplicationMenu(mainMenu);
});

const mainMenuTemplate = [
    {
        label: 'File',
        submenu: [
            {
                label: 'Quit',
                accelerator: process.platform == 'darwin' ? 'Commmand + Q': 'Ctrl+Q',
                click() {
                    app.quit();
                }
            }
        ]
    }
];

//handle create add window
function createAddWindow() {
    //Create new window
    addWindow = new BrowserWindow({
        width: 300,
        height: 200,
        title: "APP"
    });
    //load html into into window
    addWindow.loadURL(url.format({
        //pass the path of the file 
        pathname: path.join(__dirname, 'addWindow.html'),
        protocol: 'file',
        slashes: true
    }));
    //garbage collection
    addWindow.on("close", function () {
        addWindow = null;
    });
}