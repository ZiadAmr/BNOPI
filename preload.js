
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
  * specific functions for loading/saving stage formats
  * defined in file_handler.js
  */
  openStageFormat: (project, stage, path) => ipcRenderer.invoke("openStageFormat", project, stage, path),
  saveStageFormat: (project, stage, path, data, metadata) => ipcRenderer.invoke("saveStageFormat", project, stage, path, data, metadata),
  getListOfStageFormat: (project) => ipcRenderer.invoke("getListOfStageFormat", project),

  inputTextBox: (prompt) => ipcRenderer.invoke("inputTextBox", prompt),

  // launch page
  openProjectFolderDialog: () => ipcRenderer.invoke("openProjectFolderDialog"),
  createNewProjectDialog: () => ipcRenderer.invoke("createNewProjectDialog")



})
