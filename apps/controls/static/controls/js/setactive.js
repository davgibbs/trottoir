"use strict";

window.onload = setActive;

function setActive() {
    var document_location = document.location.href;
    $('#navbarNav a').each(function(){
        if (document_location === this.href) {
            $(this).addClass('active');
        }
    });
}