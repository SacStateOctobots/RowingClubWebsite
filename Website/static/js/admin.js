// just made it so awesome ngl
// functions to clean from respective databases

const regex = /'(?=,)/gi;
const middleRegex = /(, ')/gi;
const firstRegex = /[(']/gi;
const newlineRegex = /\r?\n|\r/gi;

function memberSelect() {
    var x = document.getElementById("memberList").value

    const previewSplit = x.replaceAll(regex, '+');
    const splitArray = x.split(regex);
    const memberRole = splitArray[3].replace(middleRegex, '');

    document.getElementById("memberTitle").innerHTML = splitArray[0].replace(firstRegex, '');
    document.getElementById("memberDesc").innerHTML = splitArray[1].replace(middleRegex, '');
    document.getElementById("memberImage").src = "static/image_uploads/".concat(splitArray[2].replace(middleRegex, ''));
    document.getElementById("memberRole").innerHTML = "Role: ".concat(memberRole.substring(0, splitArray[3].length - 5));
    //alert(previewSplit); //use this to see where exactly im splitting the raw sql string			
}

function officerSelect() {
    var x = document.getElementById("officerList").value

    const previewSplit = x.replaceAll(regex, '+');
    const splitArray = x.split(regex);
    const officerImg = splitArray[2].replace(middleRegex, '');

    document.getElementById("officerTitle").innerHTML = splitArray[0].replace(firstRegex, '');
    document.getElementById("officerDesc").innerHTML = splitArray[1].replace(middleRegex, '');
    document.getElementById("officerImage").src = "static/image_uploads/".concat(officerImg.substring(0, splitArray[2].length - 5));
    //alert(previewSplit); //use this to see where exactly im splitting the raw sql string			
}

function alumniSelect() {
    var x = document.getElementById("alumniList").value

    const previewSplit = x.replaceAll(regex, '+');
    const splitArray = x.split(regex);
    const alumniImg = splitArray[2].replace(middleRegex, '');

    document.getElementById("alumniTitle").innerHTML = splitArray[0].replace(firstRegex, '');
    document.getElementById("alumniDesc").innerHTML = splitArray[1].replace(middleRegex, '');
    document.getElementById("alumniImage").src = "static/image_uploads/".concat(alumniImg.substring(0, splitArray[2].length - 5));
    //alert(previewSplit); //use this to see where exactly im splitting the raw sql string			
}

function testimonialSelect() {
    var x = document.getElementById("testimonialList").value

    const previewSplit = x.replaceAll(regex, '+');
    const splitArray = x.split(regex);
    const cleanTestimonialBody = splitArray[1].replace(middleRegex, '');
    const testimonialJob = splitArray[3].replace(middleRegex, '');

    document.getElementById("testimonialTitle").innerHTML = splitArray[0].replace(firstRegex, '');
    document.getElementById("testimonialBody").innerHTML = cleanTestimonialBody.replace(newlineRegex, '');
    document.getElementById("testimonialImage").src = "static/image_uploads/".concat(splitArray[2].replace(middleRegex, ''));
    document.getElementById("testimonialJob").innerHTML = "Job: ".concat(testimonialJob.substring(0, splitArray[3].length - 5));
    //alert(previewSplit); //use this to see where exactly im splitting the raw sql string			
}

//selected tab js
//Script for displaying tabs and saving tab state 
//https://www.w3schools.com/w3css/w3css_tabulators.asp
window.onload = Loader;

//Selected Tab
function openTab(evt, tabName) {
    var i, x, tabname;
    x = document.getElementsByClassName("tabname");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablink");

    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" w3-red", "");
    }

    document.getElementById(tabName).style.display = "block";
    localStorage.setItem('activeTab', tabName);

    evt.currentTarget.className += " w3-red";

} // End Selected Tab

function Loader() {
    str = localStorage.getItem('activeTab');

    switch (str) {
        case 'TeamMembers':
        case 'Officers':
        case 'Testimonials':
        case 'Content':
            openTab(" w3-red", str);
            break;
        default:
            alert("no value");
    }

}