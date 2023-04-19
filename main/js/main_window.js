const path = require('path');
const { BrowserWindow, app, ipcMain, Notification, dialog, Menu } = require('electron');
const { mainMenu } = require("./menu")



function createWindow(projectPath = null) {
	const win = new BrowserWindow({
		width: 1200,
		height: 800,
		backgroundColor: "white",
		webPreferences: {
			nodeIntegration: false,
			worldSafeExecuteJavaScript: true,
			contextIsolation: true,
			preload: path.join(__dirname, 'preload.js')
		},
		show: false
	})

	win.once("ready-to-show", () => {
		if (projectPath != null) {
			win.webContents.send("openProject", projectPath);
		}
		win.show()
	});
	
	win.loadFile('index.html');
	return win;
}

module.exports = { createWindow };