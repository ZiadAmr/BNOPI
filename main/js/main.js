const { BrowserWindow, app, ipcMain, Notification, dialog, Menu} = require('electron');
const fs = require('fs');
const fsp = require('fs/promises');
const path = require('path');
const { Template } = require('webpack');
const child = require('child_process')

const file_handler = require("./file_handler.js");
const { StageFormatHandler } = require("./stage_format_handler");
const { electron } = require('process');
const {createLaunchPage} = require("./launch_page")
const { createWindow } = require("./main_window")

const isDev = !app.isPackaged;

/** @type {BrowserWindow} */
var mainWindow; // BrowserWindow
/** @type {BrowserWindow} */
var launchPage;
/** @type {StageFormatHandler} */
var sfh; // StageFormatHandler


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


  // application menu
  const isMac = process.platform === "darwin";

  const template = [
    ...(isMac ? [{
      label: app.name,
      submenu: [
        { role: "about" },
        { type: "separator" },
        { role: "quit" }
      ]
    }] : []),
    {
      label: "File",
      submenu: [
        {
          label: "Open project",
          click: async () => {
            if (launchPage == null) {
              launchPage = createLaunchPage();
              launchPage.on("close", () => launchPage = null);
            }
          },
          accelerator: "CmdOrCtrl+O"
        },
        {
          label: "Save",
          click: async () => {
            mainWindow.webContents.send("save");
            console.log("save");
          },
          accelerator: "CmdOrCtrl+S"
        },
        { role: "quit" }
      ]
    },
    {
      label: 'View',
      submenu: [
        { role: 'reload' },
        { role: 'forceReload' },
        { role: 'toggleDevTools' }
      ]
    }
  ];

  Menu.setApplicationMenu(Menu.buildFromTemplate(template));

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

      console.log("Running: ");
      console.log("\t Script: ", script)
      console.log("\t Arguments: ", args)
      arr = ["-file", script].concat(args)
      console.log("\t Array: ", arr)
      const data = await child.spawn("powershell", arr);
      let output = ""
      await data.stdout.on('data',function(data){
        console.log("data: ",data.toString());
        // memory[id] = data.toString()
        
        // console.log("after:", memory)
        
        output += data.toString()

        return data.toString()
      });
      console.log("success!", output)
      return true;
    } catch (err) {
      console.log("Spawn child isn't working!\n", err);
    }
  })


  // ================================================================
  // Path creation endpoints
  // ================================================================
  ipcMain.handle("createNewLoc", async (event, loc, format, id) => {
    const temp = `${format}_${id}.json`;
    const return_path = path.join(loc, temp);
    return return_path;
  });

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
  ipcMain.handle("openBNOPIDir", async (event) => file_handler.selectBNOPIOutputStageInstanceLocation())
  ipcMain.handle("getStageFormatInfo", async (event, ...args) => sfh.getStageFormatInfo(...args));

  // ================================================================
  // dialog boxes
  // ================================================================
  ipcMain.handle("showMessageBox", async (event, ...args) => dialog.showMessageBox(...args));

  // ================================================================
  // inter-window communication between the launch page and the main window
  // ================================================================
  // launch page tells the main page to open a project
  ipcMain.handle("sendOpenProjectSignal", async (event, projPath) => {

    // close the launch page
    if (launchPage != null) {
      launchPage.close();
    }

    // open the project
    // open a new main window, if necessary.
    if (mainWindow == null) {
      mainWindow = createWindow(projPath);
      mainWindow.on("close", function() {
        app.quit();
      })
    } else {
      mainWindow.webContents.send("openProject", projPath)
    }
  });


  mainWindow = createWindow();

  launchPage = createLaunchPage();
  launchPage.on("close", () => launchPage = null);
  // createWindow();
}
)
