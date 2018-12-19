var app = require('app');
var BrowserWindow = require('browser-window'); 
require('crash-reporter').start();
var mainWindow = null;
app.on('window-all-closed', function() {
  app.quit();
});

app.on('ready', function() {
  // call python
  var subpy = require('child_process').spawn('python', [__dirname + '/src/python/hello.py']);

  // Create the browser window.
  mainWindow = new BrowserWindow({width: 800, height: 600});
  
  // Disable default menu bar
  // mainWindow.setMenu(null);

  // and load the index.html of the app.
  mainWindow.loadURL('file://' + __dirname + '/index.html');
  //mainWindow.loadURL('http://localhost:5000');

  // Open the devtools.
  // mainWindow.openDevTools();

  // Emitted when the window is closed.
  mainWindow.on('closed', function() {
    mainWindow = null;

    // kill python
    subpy.kill('SIGINT');
  });
})
