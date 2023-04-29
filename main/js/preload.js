
const { ipcRenderer, contextBridge } = require('electron');

contextBridge.exposeInMainWorld('electron', {
  notificationApi: {
    sendNotification(message) {
      ipcRenderer.send('notify', message);
    }
  },
  batteryApi: {

  },
  filesApi: {

  },
  writeFile: (path, data) => ipcRenderer.invoke('writeFile', path, data),
  readFile: (path) => ipcRenderer.invoke('readFile', path),

  /* 
  * Dependency Graph
  */

  spawn_child: (script, args, names, wlat, wlon, wrad) => ipcRenderer.invoke('spawn_child', script, args, names, wlat, wlon, wrad),

  /*
  * specific functions for loading/saving stage formats
  * defined in file_handler.js
  */
  openStageFormat: (project, stage, path) => ipcRenderer.invoke("openStageFormat", project, stage, path),
  saveStageFormat: (project, stage, path, data, metadata) => ipcRenderer.invoke("saveStageFormat", project, stage, path, data, metadata),
  getListOfStageInstance: (...args) => ipcRenderer.invoke("getListOfStageInstance", ...args),
  openBNOPIALG: () => ipcRenderer.invoke('openBNOPIALG'),
  openBNOPIDir: () => ipcRenderer.invoke('openBNOPIDir'),
  getStageFormatInfo: (...args) => ipcRenderer.invoke("getStageFormatInfo", ...args),

  inputTextBox: (prompt) => ipcRenderer.invoke("inputTextBox", prompt),

  // launch page
  openProjectFolderDialog: () => ipcRenderer.invoke("openProjectFolderDialog"),
  createNewProjectDialog: () => ipcRenderer.invoke("createNewProjectDialog"),
  createNewProject: (projpath) => ipcRenderer.invoke("createNewProject", projpath),
  getProjectMetadata: (projpath) => ipcRenderer.invoke("getProjectMetadata", projpath),
  getRecents: (...args) => ipcRenderer.invoke("getRecents", ...args),
  addToRecents: (...args) => ipcRenderer.invoke("addToRecents", ...args),
  sendOpenProjectSignal: (...args) => ipcRenderer.invoke("sendOpenProjectSignal", ...args),
  loadStageInstance: (...args) => ipcRenderer.invoke("loadStageInstance", ...args),
  saveStageInstanceAs: (...args) => ipcRenderer.invoke("saveStageInstanceAs", ...args),

  // dialog boxes
  showMessageBox: (...args) => ipcRenderer.invoke("showMessageBox", ...args),


  // one way communication, main process to bnopi window renderer:
  onOpenProject: (callback) => ipcRenderer.on("openProject", callback),
  onSave: (callback) => ipcRenderer.on("save", callback),

  // Path creation
  createNewLoc: (loc, format, id, type) => ipcRenderer.invoke("createNewLoc", loc, format, id, type)

})
