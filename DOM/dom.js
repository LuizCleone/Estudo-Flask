//Procolos da WEB
//é uma forma de comunicação entre computadores através da rede
//o HTTP serve para solicitar arquivos e imagens no servidor
//HTTP: Hyper Text Transfer Protocol
//É possivel navegar em site através do HTTP
//SMTP:protocolo para envio de email
//TCP:protocolo para transferencia de dados
   //tambem temos as Urls
//A URL(Uniform Resouce Locator)pode ser dividida em três partes
// protocolo: que é o HTTP
// Dominio: (nome..).com.br( que referncia um servidor(DNS > IP))
// INDEX.HTML: arquivo da página que estamosou o endpoint
//DOM e o HTML
//é uma representção fiel do html da página;
//ele é utilizado para acessar o HTML através de JS
// DOM - Documento Object Model
console.log(document.body);//para acessar JS em HTML eplo DOM
//comandos para acessar o css:
// (getElementsByTagName - para selecionar um conjunto de elementos por uma tag)
// (getElementByld - )
// (quertSelector)


//SELECIONANDO ELEMENTOS POR TAGS
const listItens = document.getElementsByTagName("li");
console.log(listItens);

//selecionando elementos pelo ID
//como o método getElementByID selecionamos um único elemento
//p argumento é uma string que leva o ide a ser selecionado
const title = document.getElementById("title");
console.log(title);

//Encontrando elementos por classe
//com o método getElementByClass selecionamos um conjunto de elementos por uma classe em comum;
//o argumento é uma string que leva a classe a ser selecionada
const products = document.getElementsByClassName("product");
console.log(products);

//Encontrando elementos po CSS
// com o método querySelectorAll selecionamos um conjunto de elementos por meio de um seletor de css;
//E com o querySelector apenas um elemento,com base tbm um seletor CSS;
const testeQuery = document.querySelectorAll(".product");
console.log(testeQuery);

const mainContainer = document.querySelector("#main-container");
console.log(mainContainer);

//Alterando o HTML pelo DOM
//Adicionar,remover e clonar eklementos
//Alguns métodos mais utilizados são: insertBefore,appendChild,replaceChild;
//insertBefore - insere um elemento antes do outro
//appendChild - insere o elemento dentro do outro
//replaceChild - troca um elemento por outro

//Método insertBefore
//É necessário criar um ele com JS,isso pode ser feito com o createElement;
const p = document.createElement("p");

const header = title.parentElement;

header.insertBefore(p, title);

//Método appendChild
const navLinks = document.querySelector("nav ul");

const li = document.createElement("li");

navLinks.appendChild(li);

//Método replaceChild
//é utilizado para trocar um elemento;
const h2 = document.querySelector("h2");

h2.textContent = "Novo Título!";

header.replaceChild(h2, title);

// Criandp nós de texto
//Os textos podem ser manipulados com métodos também;
//temos o createTextNode,que cria um nó de texto;
//E este nó pode ser inserido em um elemento;
const meuTexto = document.createTextNode("Inserindo outro título");
console.log(meuTexto);

const h3 = document.createElement("h3");
h3.appendChild(meuTexto);

console.log(h3);

mainContainer.appendChild(h3);

//TRABALHANDO COM ATRIBUTOS
//Podemos ler e alterar os valores dos atributos;
//Para ler vamos utilizar o método getAttribute,
// E para alterar utilizamos o setAttribute,este leva o nome do atributo e o valor para alterar
const primeiroLink = navLinks.querySelector("a");
console.log(primeiroLink);

primeiroLink.setAttribute("href", "https://www.google.com");
console.log(primeiroLink.getAttribute("href"));

primeiroLink.setAttribute("target", "_blank");

//ALTURA E LARGURA DOS ELEMENTOS
//É possível tbm pegar valores comaltura e largura de elememtos;
//Vamos utilizar as propriedades: offsetWidth, offsetHeight
//para desconsiderar as bordas temos: clientWidth e clientHeight
const footer = document.querySelector("footer");

console.log(footer.offsetWidth);//mostra a largura
console.log(footer.offsetHeight);//mostra a altura
console.log(footer.offsetLeft);//mostra a posição a esquerda da página
//atibuto visíveis para o cliente
console.log(footer.clientWidth);//
console.log(footer.clientHeight);//

//POSIÇÃO DO ELEMENTO
//Com o método gtetClientBoundingRect podemos pegar várias informações do elemento;
//Como:posição no eixo X,Y,altura,largura e outros;
const product1 = products[0];

console.log(product1.getBoundingClientRect());

//ALTERANDO O CSS PELO JAVASCRIPT
mainContainer.style.color = "red";
mainContainer.style.backgroundColor = "yellow";

//ALTERANDO ESTILOS DE HTMLCollection
//HTMLCollection aparece quando selecionamos vários elementos de uma vez
//Podemos passar por cada um dos elemento com um for of,e estilizar individualmente cada item
for (const li of listItens) {
   li.style.backgroundColor = "yellow"
}

