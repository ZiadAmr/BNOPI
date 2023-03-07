
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
  readFile: (path) => ipcRenderer.invoke('readFile', path)
})
