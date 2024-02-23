
        const sidebar = document.getElementById('sidebar');
        const content = document.getElementById('content');
        const menuToggle = document.getElementById('menu-toggle');
    
        // Remove the initial click requirement
        sidebar.style.left = '0px'; // Set the initial state to open
        content.style.marginLeft = '250px'; // Set the initial margin-left
    
        menuToggle.addEventListener('click', () => {
            if (sidebar.style.left === '0px') {
                sidebar.style.left = '-250px';
                content.style.marginLeft = '0';
                menuToggle.classList.remove('open');
            } else {
                sidebar.style.left = '0px';
                content.style.marginLeft = '250px';
                menuToggle.classList.add('open');
            }
        });
