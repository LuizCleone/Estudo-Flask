console.log("teste");
//iniciando a calculadora no JS
const multiplicationForm = document.querySelector("#multiplication-form");
const numberInput = document.querySelector("#number");
const multiplicationInput = document.querySelector("#multiplicador");
const multiplicationTitle = document.querySelector("#titulo-multiplicacao span");
const multiplicationTable = document.querySelector("#operacao-multiplicacao");
//Funções
const createTable = (number, multiplicadorNumber) => {
   multiplicationTable.innerHTML = "";

    for(i = 0; i <= multiplicadorNumber; i++) {
        const result = number * i;

        const template = `<div class="row">
                <div class="operacao">${number} x ${i} = </div>
                <div class="result">${result}</div>
            </div>`;
        const parser = new DOMParser()
        
        const htmlTemplate = parser.parseFromString(template, "text/html")

        const row = htmlTemplate.querySelector(".row");

        multiplicationTable.appendChild(row);
        
    }

    multiplicationTitle.innerText = number;
};

//Eventos
multiplicationForm.addEventListener("submit", (e) => {
    
    e.preventDefault();

    const multiplicationNumber = +numberInput.value;

    const multiplicadorNumber = +multiplicationInput.value;

    if (!multiplicationNumber || !multiplicadorNumber) return;

    createTable(multiplicationNumber, multiplicadorNumber);
});
