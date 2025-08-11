const buttons = document.querySelectorAll("#imagem-picker li");
const image = document.querySelector("#imagem-produto");

buttons.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      console.log(e);
      buttons.forEach((btn) => {
        btn.querySelector(".color").classList.remove("selected");
    });

    const button = e.target;

    const id = button.getAttribute("id");

    button.querySelector(".color").classList.add("selected");

    image.classList.add("changing");
    image.setAttribute("src", `imagens/iphone_${id}.png` );

    setTimeout(() => {
        image.classList.remove("changing");
    },200);
    });
});
