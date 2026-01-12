document.addEventListener("DOMContentLoaded", () => {

    console.log("hello");

    const button = document.getElementById("testing");
    button.addEventListener("click", () => {
        alert("Button clicked!");
    });

});