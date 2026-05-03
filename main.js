const { app, BrowserWindow } = require('electron');

app.whenReady().then(() => {
    const win = new BrowserWindow({
        width: 510,
        height: 480,
        resizable: false
    });

    win.webContents.setVisualZoomLevelLimits(1, 3);

    win.setMenu(null);

    win.loadFile("web/index.html");
})
