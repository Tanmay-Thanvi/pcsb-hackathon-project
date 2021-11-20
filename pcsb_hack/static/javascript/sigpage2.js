
let cc = document.querySelector("#one")
let classroom = document.querySelector("#two");
let task = document.querySelector("#three");
let announcement = document.querySelector("#four");
let para = document.querySelector('#para');

let ccshow = document.querySelector('#course-content');
let classroomshow = document.querySelector('#classroom');
let taskshow = document.querySelector('#task');
let announcementshow = document.querySelector('#announcement');

  function changeLanguage(language) {
    var element = document.getElementById("url");
    element.value = language;
    element.innerHTML = language;
}

function showDropdown() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

function showDropdown() {
    document.getElementById("dropdown").style.display = "flex";
  
  }
  function closedropdown() {
    document.getElementById("dropdown").style.display = "none";
  }

function openaddmodal()
{
    var x = document.getElementById("addmodal");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
 
 
}
function funcaddtopic(){
  document.getElementById("addtopic").click();
}
function funcaddmaterial(){
  document.getElementById("addmaterial").click();
}
