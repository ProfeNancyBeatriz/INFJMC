document.querySelectorAll(".menu a").forEach(function (enlace) {
    if (enlace.getAttribute("href") === window.location.pathname) {
        enlace.classList.add("activo");
    }
});