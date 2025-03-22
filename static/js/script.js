document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".favorite-btn");
    const favoriteSection = document.getElementById("favorite-plant");

    buttons.forEach(button => {
        button.addEventListener("click", function () {
            const plantName = this.getAttribute("data-plant");
            favoriteSection.textContent = "Your Favorite Plant: " + plantName;
        });
    });
});
