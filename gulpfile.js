const { spawn } = require('child_process');
const gulp = require('gulp');
const PyLint = require('gulp-pylint');

gulp.task('lint', function() {
    return gulp.src(['**/*.py', '!node_modules/**'], {read: true})
        .pipe(PyLint({}))
});

gulp.task('test', function(cb) {
    let proceso = spawn('gulp', ['lint']);

    proceso.stdout.on('data', function (dato) {
        console.log(dato.toString())
    });
    proceso.on('exit', function() {
        console.log('process culminited');
    });
    cb();
})
