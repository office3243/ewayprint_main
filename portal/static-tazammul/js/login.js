function showSignup(){
    document.querySelector("#login-section").style.display = "none";
    document.querySelector("#new-account-section").style.display = "block";
    document.querySelector("#signup-button").style.display = "none";
    document.querySelector("#login-button").style.display = "block";
}
function showLogin(){
    document.querySelector("#new-account-section").style.display = "none";
    document.querySelector("#login-section").style.display = "block";
    document.querySelector("#forget-password-section").style.display = "none";
    document.querySelector("#login-button").style.display = "none";
    document.querySelector("#signup-button").style.display = "block";
}
function showForgetPsswd(){
    document.querySelector("#login-section").style.display = "none";
    document.querySelector("#forget-password-section").style.display = "block";
    document.querySelector("#signup-button").style.display = "none";
    document.querySelector("#login-button").style.display = "block";
}
    
