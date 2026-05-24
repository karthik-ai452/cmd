/*
 * CmdRunner — Main JavaScript
 * Analytics tracking, FAQ accordion, video lazy loading
 */

(function () {
    'use strict';

    /* ---- Analytics helpers ---- */
    function safeTrack(eventName, payload) {
        if (typeof gtag === 'function') {
            gtag('event', eventName, payload || {});
        }
    }

    window.safeTrack = safeTrack;

    window.trackBeta = function () {
        safeTrack('click_beta_button', {
            event_category: 'engagement',
            event_label: 'Request Beta Access'
        });
    };

    window.trackDemo = function () {
        safeTrack('click_demo_button', {
            event_category: 'engagement',
            event_label: 'Product Animation'
        });
        var demoSection = document.getElementById('demo');
        if (demoSection) {
            demoSection.scrollIntoView({ behavior: 'smooth' });
        }
    };

    window.trackSignup = function (email) {
        safeTrack('sign_up', {
            event_category: 'conversion',
            event_label: email
        });
    };

    /* ---- FAQ Accordion ---- */
    window.toggleAccordion = function (headerElement) {
        var content = headerElement.nextElementSibling;
        var isActive = content.classList.contains('active');

        var activePanels = document.querySelectorAll('.accordion-content.active');
        for (var i = 0; i < activePanels.length; i++) {
            if (activePanels[i] !== content) {
                activePanels[i].classList.remove('active');
                activePanels[i].previousElementSibling.classList.remove('active');
            }
        }

        content.classList.toggle('active', !isActive);
        headerElement.classList.toggle('active', !isActive);
    };

    /* ---- Vimeo video lazy loading with autoplay ---- */
    var demoVideo = document.getElementById('demoVideo');
    var demoSection = document.getElementById('demo');

    if ('IntersectionObserver' in window && demoVideo && demoSection) {
        var videoObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting && demoVideo.dataset.src && demoVideo.src !== demoVideo.dataset.src) {
                    demoVideo.src = demoVideo.dataset.src;
                }
            });
        }, { threshold: 0.45 });

        videoObserver.observe(demoSection);
    }

})();