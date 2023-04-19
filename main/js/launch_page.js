const { BrowserWindow } = require("electron");
const path = require("path");


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
		},
		show: false
	})

	win.once("ready-to-show", () => {
		win.show();
	});

	win.loadFile(path.resolve('launchwindow.html'));

	return win;
}

module.exports = {createLaunchPage};