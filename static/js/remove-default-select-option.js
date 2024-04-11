const selectElements = document.getElementsByTagName('select');

for (const select of selectElements) {
    select.options[0].style.display = 'none';
}