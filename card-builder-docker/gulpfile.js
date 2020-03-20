let gulp = require('gulp');

var run = {
	less: require('gulp-less'),
	concat: require('gulp-concat'),
	css_minify: require('gulp-csso'),
	css_beutify: require('gulp-cssbeautify'),
	plumber: require('gulp-plumber'),
	rename: require('gulp-rename'),
	path: require('path'),
};

let assets  = run.path.resolve('./app/');


function less_watcher() {
	return gulp.watch([assets + "/*.less" ], less_builder);
}

function less_builder() {
	return gulp.src( assets + "/*.less")
		.pipe(run.plumber())
		.pipe(run.less())
		.pipe(run.rename(function (path) {
			path.extname = ".min.css"
		}))
		.pipe(run.css_minify())
		.pipe(run.plumber.stop())
		.pipe(gulp.dest( assets + "/" ))
}

function css_minify_watcher() {
	return gulp.watch([ assets + "/*.min.css" ], css_minify);
}

function css_minify() {
	return gulp.src(assets + "/*.min.css")
		.pipe(run.plumber())
		.pipe(run.rename(function (path) {
			path.basename = path.basename.replace(".min", "")
			path.extname = ".css"
		}))
		.pipe(run.css_beutify())
		.pipe(run.plumber.stop())
		.pipe(gulp.dest(assets + "/"))
}

exports.default = gulp.parallel(
	gulp.parallel(less_watcher, css_minify_watcher),
	gulp.parallel(less_builder),
);
