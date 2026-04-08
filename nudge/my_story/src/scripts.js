/* SugarCube configuration */
Config.cleanupWikifierOutput = true;

/* Configure MathJax before loading it */
var mathJaxReady = false;
window.MathJax = {
	tex: {
		inlineMath:  [['\\(', '\\)']],
		displayMath: [['$$', '$$']]
	},
	startup: {
		typeset: false,
		ready: function () {
			MathJax.startup.defaultReady();
			mathJaxReady = true;
			var passage = document.querySelector('.passage');
			if (passage) {
				MathJax.typesetPromise([passage]);
			}
		}
	}
};

/* Load MathJax (importScripts is a SugarCube built-in) */
importScripts("https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js");

/* Typeset only the visible passage, never the whole document */
$(document).on(':passagedisplay', function () {
	var passage = document.querySelector('.passage');
	if (mathJaxReady && passage) {
		MathJax.typesetPromise([passage]);
	}
});

/* Dark mode toggle */
var darkModeHandler = function () {
	if (settings.darkMode) {
		$("html").addClass("dark");
	} else {
		$("html").removeClass("dark");
	}
};
Setting.addToggle("darkMode", {
	label    : "Dark mode",
	default  : false,
	onInit   : darkModeHandler,
	onChange  : darkModeHandler
});
