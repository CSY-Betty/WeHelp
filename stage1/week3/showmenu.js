function showmenu(elem){
    let menumobile = document.getElementById('menumobile');
    elem.style.display = 'none';
    menumobile.style.display = 'inline-block';
    menumobile.style.position = 'fixed';
}

function hidemenu(elem){
    let menuthumb = document.getElementById('menuthumb');
    elem.style.display = 'none';
    menuthumb.style.display = 'block';
}