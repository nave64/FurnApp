// Django Admin Sidebar Scroll Position Preservation
(function() {
    'use strict';
    
    let sidebarScrollPosition = 0;
    let isRestoring = false;
    
    // Function to save sidebar scroll position
    function saveSidebarScrollPosition() {
        const sidebar = document.getElementById('nav-sidebar');
        if (sidebar && !isRestoring) {
            sidebarScrollPosition = sidebar.scrollTop;
            sessionStorage.setItem('adminSidebarScrollPosition', sidebarScrollPosition);
        }
    }
    
    // Function to restore sidebar scroll position
    function restoreSidebarScrollPosition() {
        const sidebar = document.getElementById('nav-sidebar');
        if (sidebar) {
            const savedPosition = sessionStorage.getItem('adminSidebarScrollPosition');
            if (savedPosition && parseInt(savedPosition) > 0) {
                isRestoring = true;
                setTimeout(function() {
                    sidebar.scrollTop = parseInt(savedPosition);
                    isRestoring = false;
                }, 10);
            }
        }
    }
    
    // Function to setup sidebar event listeners
    function setupSidebarListeners() {
        const sidebar = document.getElementById('nav-sidebar');
        if (sidebar) {
            // Add click listeners to all links in the sidebar
            const sidebarLinks = sidebar.querySelectorAll('a');
            sidebarLinks.forEach(function(link) {
                link.addEventListener('click', saveSidebarScrollPosition);
            });
            
            // Save position when scrolling the sidebar
            sidebar.addEventListener('scroll', function() {
                if (!isRestoring) {
                    sidebarScrollPosition = sidebar.scrollTop;
                    sessionStorage.setItem('adminSidebarScrollPosition', sidebarScrollPosition);
                }
            });
            
            // Handle sidebar toggle button
            const toggleButton = document.getElementById('toggle-nav-sidebar');
            if (toggleButton) {
                toggleButton.addEventListener('click', function() {
                    // Save position before toggle
                    saveSidebarScrollPosition();
                    // Restore position after toggle animation
                    setTimeout(restoreSidebarScrollPosition, 50);
                });
            }
        }
    }
    
    // Initialize when DOM is ready
    function init() {
        setupSidebarListeners();
        
        // Restore position after page loads
        restoreSidebarScrollPosition();
        
        // Handle dynamic content loading (for cases where sidebar is recreated)
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                    // Check if sidebar was recreated
                    const newSidebar = document.getElementById('nav-sidebar');
                    if (newSidebar && !newSidebar.hasAttribute('data-scroll-listeners-added')) {
                        newSidebar.setAttribute('data-scroll-listeners-added', 'true');
                        setupSidebarListeners();
                        restoreSidebarScrollPosition();
                    }
                }
            });
        });
        
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
        
        // Handle window resize (sidebar might change)
        window.addEventListener('resize', function() {
            setTimeout(restoreSidebarScrollPosition, 10);
        });
        
        // Handle browser back/forward
        window.addEventListener('pageshow', function(event) {
            if (event.persisted) {
                setTimeout(restoreSidebarScrollPosition, 10);
            }
        });
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
