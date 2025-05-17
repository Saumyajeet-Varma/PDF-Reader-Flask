const input = document.getElementById("pdf");
const label = document.getElementById("label");

input.addEventListener("change", function () {
    label.textContent = input.files.length ? `${input.files[0].name}` : 'Choose PDF';
});