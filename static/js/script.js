// app.js

document.addEventListener("DOMContentLoaded", function () {
    // Get the logo image
    const logo = document.querySelector(".logo");

    // Load the logo image in the background
    const image = new Image();
    image.src = "/logo.png";

    // When the logo image is fully loaded, display the image and set the opacity to 1
    image.onload = function () {
        logo.src = image.src;
        logo.style.opacity = 1;
    };

    // Button programming
    const buttons = document.querySelectorAll(".buttons a");
   
    buttons.forEach(function (button) {
        button.addEventListener("mouseover", function () {
            button.style.backgroundColor = "#282f43";
        });

        button.addEventListener("mouseout", function () {
            button.style.backgroundColor = "#505c79";
        });

        button.addEventListener("focus", function () {
            button.style.backgroundColor = "#bf6f60";
            button.style.boxShadow = "0 0 5px #333";
        });

        button.addEventListener("blur", function () {
            button.style.backgroundColor = "#505c79";
            button.style.boxShadow = "none";
        });

        button.addEventListener("mousedown", function () {
            button.style.transform = "scale(0.98)";
        });

        button.addEventListener("mouseup", function () {
            button.style.transform = "scale(1)";
        });
    });
});