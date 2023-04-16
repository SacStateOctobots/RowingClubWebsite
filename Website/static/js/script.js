/* Swiper for testinomial*/
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    grabCursor: true,
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});

/*For sending email
More information: https://smtpjs.com */

function sendEmail() {
    Email.send({
        SecureToken: "5af3dbb1-a0a2-4f4f-b8b0-a934fdc9aba8",
        To: 'phungphan151@hotmail.com',
        From: document.getElementById("email").value,
        Subject: "Web Contact Page: " + document.getElementById("subject").value,
        Body: "Hello, <br>"
            + "My name is: " + document.getElementById("name").value 
            + ". My email: " + document.getElementById("email").value 
            + " and my phone number: " + document.getElementById("phone").value 
            + "<br> Here is my message: " + document.getElementById("message").value   
            + "<br> <br> (Note: There is a message from Contact Page - Sac State Rowing Website)"
    }).then(
        message => alert("Thank you for your message. We will contact you soon.")
    );
}