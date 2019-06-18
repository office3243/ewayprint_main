function currentlink(element){
    defaultlink();
    document.getElementById(element).classList.add("tz-currentlink");
}
function defaultlink(){
     check = document.getElementById("home-tab").classList.contains("tz-currentlink");
    if(check == true){
        document.getElementById("home-tab").classList.remove("tz-currentlink");
    }
     check = document.getElementById("upload-tab").classList.contains("tz-currentlink");
    if(check == true){
        document.getElementById("upload-tab").classList.remove("tz-currentlink");
    }
     check = document.getElementById("transaction-tab").classList.contains("tz-currentlink");
    if(check == true){
        document.getElementById("transaction-tab").classList.remove("tz-currentlink");
    }
     check = document.getElementById("account-tab").classList.contains("tz-currentlink");
    if(check == true){
        document.getElementById("account-tab").classList.remove("tz-currentlink");
    }
}
function fileChange(element){
    document.querySelector("#file-input-msg").innerHTML = element.files[0].name;
}
function changeTable(element){
    if(element.id == "printed-btn"){
        document.querySelector('#printed').style.display="block";
        document.querySelector('#not-printed').style.display="none";
        element.classList.add("tz-singlebtn-active");
        document.querySelector("#not-printed-btn").classList.remove("tz-singlebtn-active");
    }
    else{
        document.querySelector('#printed').style.display="none";
        document.querySelector('#not-printed').style.display="block";
        element.classList.add("tz-singlebtn-active");
        document.querySelector("#printed-btn").classList.remove("tz-singlebtn-active");
    }
}