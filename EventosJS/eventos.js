//Adicionando eventos
const btn = document.querySelector("#my-button");

btn.addEventListener("click", function () {
    console.log("Clique Aqui!");
});

//Removendo enventos
const segundoBtn = document.querySelector("#btn");

function imprimirMensagem() {
    console.log("Teste");
};

segundoBtn.addEventListener("click", imprimirMensagem);

const terceiroBtn = document.querySelector("#other-btn");

terceiroBtn.addEventListener("click", () => {
    console.log("Evento Removido");
    segundoBtn.removeEventListener("click", imprimirMensagem);
});

// O obejeto de evento
// Todo evento possui um argumento especial, que contém informções do mesmo
//Geralmente chamado de event ou e;
const myTitle = document.querySelector("#my-title");

myTitle.addEventListener("click", (event) => {
    console.log(event);
    console.log(event.offsetX);//poisção do elemento
    console.log(event.pointerType);//
    console.log(event.target);//elemento alvo

});

//Propagação
//Quando um elemento de um evento não é claramente definido pode haver propagação;
//Ou seja,um outro elemento ativar o evento
//para resolver este problema temos o método stopPropagation
const containerBtn = document.querySelector("#btn-container");
const btnInsideContainer = document.querySelector("#div-btn");

containerBtn.addEventListener("click", () => {
    console.log("Evento Um");
});

btnInsideContainer.addEventListener("click", (e) => {
    e.stopPropagation();
    console.log("Evento Dois");
});

//Ações default - removendo comportamento padrão
const a = document.querySelector("a");

a.addEventListener("click", (e) => {
    e.preventDefault();

    console.log("Página não exibida");
});


//Evento de Teclas
//temos a disposição keyup e keydown
//keyup quando solta a tecla
//keydown quando é precionada
document.addEventListener("keydown", (e) => {
    console.log(`Apertou a tecla ${e.key}`);
});
document.addEventListener("keyup", (e) => {
    console.log(`Precionou a tecla ${e.key}`);
});

//Outros eventos de mouse
//O mouse pode ativar outros eventos
// mousedown: pressionou botão do mouse;
// mouseup: soltou o botão do mouse
// dblclick: clique duplo
const mouseEvents = document.querySelector("#mouse");

mouseEvents.addEventListener("mousedown", () => {
    console.log("Pressionou o mouse");
});

mouseEvents.addEventListener("mouseup", () => {
    console.log("Soltou o mouse");
});

mouseEvents.addEventListener("dblclick", () => {
    console.log("Clicou duas vezes no mouse");
});

//Movimento do Mouse
//É possível ativar um evento a partir da movimentação do mouse
//O evento mousemove
document.addEventListener("mousemove", (e) => {
 //   console.log(`No eixo X: ${e.x}`);//mostra toda movimentação do mouse
//    console.log(`No eixo Y: ${e.y}`);//mostra toda movimentação do mouse
});//desativar para não atrapalhar o console

//EVENTOS POR SCROLL
window.addEventListener("scroll", (e) => {
    if(window.pageYOffset > 200) {
        console.log("Passamos de 200px")//mostra assim que passa de 200px
    }
});

//EVENTOS DE FOCO
//O evento focus é disparado quando focamos em um elemento
//Já o blur é quando perde o foco do elemento
//usados no inputs
const input = document.querySelector("#meu-input");

input.addEventListener("focus", (e) => {
    console.log("Entrou no Input");
});

input.addEventListener("blur", (e) => {
    console.log("Saiu do Input");
});

//EVENTO DE CARREGAMENTO DE PÁGINA
//Usando o load
//para sair beforeunload (não muito utilizado)
window.addEventListener("load", () => {
    console.log("A página carregou!")//mostra a página está carregada
});

window.addEventListener("beforeunload", (e) => {
  e.preventDefault();
//  e.returnValue = "Sair";
});

//Técnica de debounce
//O debounce é uma técnica utilizada para fazer evento disparar menos vezes;
const debounce = (f, delay) => {
    let timeout

    return (...argumento) => {
        if (timeout) {
            clearTimeout(timeout);
        }

        timeout = setTimeout(() =>{
           f.apply(argumento);
        }, delay);
    };
};

window.addEventListener("mousemove", debounce(() => {
      console.log("Executando a cada 400ms")}, 400)
);
