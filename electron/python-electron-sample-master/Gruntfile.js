module.exports = function (grunt) {
  grunt.initConfig({
    bower: {
      install: {
        options: {
          targetDir: './lib',
          layout : function (type, component) {
            if (type === 'css') {
              return 'css';
            } else {
               return 'js';
            }
          },
          install: true, 
          verbose: false, 
          cleanTargetDir: true,
          cleanBowerDir: false 
        }
      }
    },
  });
  grunt.loadNpmTasks('grunt-bower-task');
};
