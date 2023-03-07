const { BrowserWindow, app, ipcMain, Notification } = require('electron');
const fs = require('fs');
const fsp = require('fs/promises');
const path = require('path');
const { Template } = require('webpack');

const isDev = !app.isPackaged;

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

  win.loadFile('index.html');
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
  createWindow()
}
)
