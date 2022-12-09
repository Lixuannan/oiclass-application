const electron = require("electron")
let app = electron.app
let window = electron.BrowserWindow
let menu = electron.Menu

let mainWindow = null;
let dockMenu = menu.buildFromTemplate([
    {label: "打开", submenu: [
            {label: "登录", click: function (){ mainWindow.getURL("http://oiclass.com/login/"); }},
            {label: "题库", click: function (){ mainWindow.getURL("http://oiclass.com/p/"); }},
        ]}
])

app.dock.setMenu(dockMenu);
app.on("window-all-closed", function (){
    if (process.platform !== "darwin"){
        app.quit();
    }
});

app.on("ready", function (){
    mainWindow = new window({width: 800, height: 600});
    mainWindow.loadURL("http://oiclass.com/")
    mainWindow.on("closed", function (){
        mainWindow = null;
    });
});