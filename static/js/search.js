const search = () => {
const searchbox = document.getElementById("search-item").value.toUpperCase();
const storeitems = document.getgetElementById("resto-list")
console.log(storeitems);
const resto = document.querySelectorAll(".card")
console.log(resto);

for (let i =0; i< resto.length; i++){
let title = resto[i].querySelector(".card-body h3");
console.log(title);

if(title.innerText.toUpperCase.indexOf(searchbox) > -1){

title[i].style.display = "";
} else{
title[i].style.display = "none";
}
}
}
}