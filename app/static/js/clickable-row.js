document.addEventListener("DOMContentLoaded", function () {
    var clickableRows = document.getElementsByClassName("clickable-row");

    for (var i = 0; i < clickableRows.length; i++) {
        clickableRows[i].addEventListener("click", function (e) {
            // Get the URL from the data-href attribute
            var url = this.getAttribute("data-href");

            // Open the URL in the same tab
            window.open(url, "_self");
        });
    }
});