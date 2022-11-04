'use strict';


// ---- kvalitet vazduha -----------------------
let kvVazduha = document.querySelector('.kv').innerText;

if (kvVazduha === 'Dobar') {
    document.querySelector('.kv').style.color = 'green';
} else if (kvVazduha === 'Zadovoljavajući') {
    document.querySelector('.kv').style.color = 'lightgreen';
} else if (kvVazduha === 'Osrednji') {
    document.querySelector('.kv').style.color = 'yellow';
} else if (kvVazduha === 'Loš') {
    document.querySelector('.kv').style.color = 'orange';
} else if (kvVazduha === 'Veoma loš') {
    document.querySelector('.kv').style.color = 'red';
} else {
    document.querySelector('.kv').style.color = 'black';
}
// ------------------------------------------------