const { BrowserWindow, app, ipcMain, Notification, dialog } = require('electron');
const fs = require('fs');
const fsp = require('fs/promises');
const path = require('path');
const { Template } = require('webpack');
const child = require('child_process')

const file_handler = require("./file_handler.js");
const { StageFormatHandler } = require("./stage_format_handler");
const { electron } = require('process');

const isDev = !app.isPackaged;

/** @type {BrowserWindow} */
var mainWindow; // BrowserWindow
/** @type {StageFormatHandler} */
var sfh; // StageFormatHandler

function createWindow() {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    backgroundColor: "white",
    webPreferences: {
      nodeIntegration: false,
      worldSafeExecuteJavaScript: true,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    }
  })

  mainWindow = win;

  win.loadFile('index.html');
}

function createLaunchPage() {
  const win = new BrowserWindow({
    width: 800,
    height: 450,
    resizable: true,
    autoHideMenuBar: true,
    backgroundColor: "white",
    webPreferences: {
      nodeIntegration: false,
      worldSafeExecuteJavaScript: true,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    }
  })

  win.loadFile(path.resolve('launchwindow.html'));
}

if (isDev) {
  require('electron-reload')(__dirname, {
    electron: path.join(__dirname, 'node_modules', '.bin', 'electron')
  })
}

ipcMain.on('notify', (_, message) => {
  new Notification({ title: 'Notifiation', body: message }).show();
})

app.whenReady().then(() => {

  // ================================================================
  // instansiate objects from other files
  // ================================================================
  sfh = new StageFormatHandler(); 
  // load all the default stage formats
  // TODO in the future these directories will be listed in the project info.json file
  sfh.loadStageFormatsFromDir("bnopi-stage-fmts");

  // ================================================================
  // setup endpoints for front-end functions
  // ================================================================

  ipcMain.handle('writeFile', async (event, fileName, data) => {
    const response = fs.writeFile(fileName, data, (err) => {
      if (err) {
        console.log(err);
      } else {
        console.log("Error writing file");
      }
    });
    return response;
  }
  )

  ipcMain.handle('readFile', async (event, fileName) => {
    try {
      const data = await fsp.readFile(fileName, { encoding: 'utf-8' });
      return data;
    } catch (err) {
      console.log(err);
    }

    // Alternate synchronous version
    // const response = fs.readFileSync(fileName, 'utf-8', () => { })
    // return response;
  }
  )

  // ================================================================
  // dependency graph
  // ================================================================
  ipcMain.handle('spawn_child', async (event, script, args) => {
    try {
      const data = await child.spawn("./print.sh");
      // python.stdout.on('data',function(data){
      //   console.log("data: ",data.toString());
      //   memory[id] = data.toString()
        
      //   console.log("after:", memory)

      //   return data.toString()
      // });
      console.log("success!")
      return "return";
    } catch (err) {
      console.log("Spawn child isn't working!\n", err);
    }
  })



  // ================================================================
  // file_handler endpoints
  // ================================================================
  ipcMain.handle("openStageFormat", async (event, ...args) => file_handler.openStageFormat(...args));
  ipcMain.handle("saveStageFormat", async (event, ...args) => file_handler.saveStageFormat(...args));
  ipcMain.handle("getListOfStageFormat", async (event, ...args) => file_handler.getListOfStageFormat(...args));

  // ================================================================
  // getting user input (mainly for testing)
  // ================================================================
  ipcMain.handle("openProjectFolderDialog", async (event) => file_handler.openProjectFolderDialog());
  ipcMain.handle("createNewProjectDialog", async (event) => file_handler.createNewProjectDialog());
  ipcMain.handle("createNewProject", async (event, ...args) => file_handler.createNewProject(...args));
  ipcMain.handle("openProject", async (event, ...args) => file_handler.openProject(...args));
  ipcMain.handle("getRecents", async (event, ...args) => file_handler.getRecents(...args));
  ipcMain.handle("getProjectMetadata", async (event, ...args) => file_handler.getProjectMetadata(...args));
  ipcMain.handle("addToRecents", async (event, ...args) => file_handler.addToRecents(...args));
  ipcMain.handle("loadStageInstance", async (event, ...args) => sfh.loadStageInstance(...args));
  ipcMain.handle("saveStageInstanceAs", async (event, ...args) => sfh.saveStageInstanceAs(...args));
  ipcMain.handle("openBNOPIALG", async (event) => file_handler.openBNOPIAlg());
  ipcMain.handle("getStageFormatInfo", async (event, ...args) => sfh.getStageFormatInfo(...args));

  // ================================================================
  // inter-window communication between the launch page and the main window
  // ================================================================
  // launch page tells the main page to open a project
  ipcMain.handle("sendOpenProjectSignal", async (event, projPath) => {
    mainWindow.webContents.send("openProject", projPath)
  });

  createLaunchPage();
  createWindow();
}
)
