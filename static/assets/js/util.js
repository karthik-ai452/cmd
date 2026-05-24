/*
 * CmdRunner — Utility Functions
 */

var CmdRunner = CmdRunner || {};

CmdRunner.util = {
    debounce: function (fn, delay) {
        var timer = null;
        return function () {
            var context = this;
            var args = arguments;
            clearTimeout(timer);
            timer = setTimeout(function () {
                fn.apply(context, args);
            }, delay);
        };
    },

    throttle: function (fn, limit) {
        var inThrottle = false;
        return function () {
            if (!inThrottle) {
                fn.apply(this, arguments);
                inThrottle = true;
                setTimeout(function () {
                    inThrottle = false;
                }, limit);
            }
        };
    },

    isMobile: function () {
        return window.innerWidth < 768;
    },

    scrollToElement: function (selector, offset) {
        var el = document.querySelector(selector);
        if (el) {
            var y = el.getBoundingClientRect().top + window.pageYOffset - (offset || 0);
            window.scrollTo({ top: y, behavior: 'smooth' });
        }
    }
};