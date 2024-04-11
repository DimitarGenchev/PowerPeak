const selectElements = document.getElementsByTagName('select');

for (const select of selectElements) {
    select.options[0].style.display = "none";
}

window.onload = function() {
    if (performance.navigation.type === 1) {
        window.history.replaceState({}, document.title, window.location.pathname);
    }
}