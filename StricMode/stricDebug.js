//O strict é um modo de desenvolvimento que deixa o JS mais rigoroso na hora de programar
//Deve ser declarado no topo do arquivo ou de funções
//O stric não limita os recursos de JS,ele baliza a forma que vc programa
//Bibliotecas famosas são todas feitas em stric
// 1 - Usando o strict
"use strict";// a partir daqui o código começa funcionar com restrições
//não pode declarar variavel global
// exe.  carro = "Fiat";
const carro = "Fiat"

//nao pode declara variavael com palavra reservada
//   const undefined = 10;

//nao pode apagar um obejeto array
// delete [].length;

// Método de debug:console.log
//O método log de console é muito utilizado para debug;
//Utilizamos diversoas vezes nos nossos exemplos

let a = 1
let b = 2

if(a == 1) {
    a = b + 2;
};
console.log(a);

for (let i = 0; i < b; i++) {
    a = a + 2;
    console.log(a);
};

if (a > 5) {
    a = 25;
};
console.log(a)

//MÉTOD DE DEBUG:DEBUGGER
//O debugger é uma instrução que nos permite o debug no console do navegador
//Podemos evindenciar os valores das variáveis em tempo real e com o programa executando,
//o que ajuda bastante
let c = 1
let d = 2

if(c == 1) {
    c = d + 2;
};
//debugger

for (let i = 0; i < d; i++) {
    c = c + 2;
};

console.log("Executando o loop");
//debugger
if (c > 5) {
    c = 25;
};

//TRATAMENTO DE DADO POR FUNÇÃO
//Nunca podemos confiar no dado que é passado pelo usuário;
//Sempre devemos criar validação e tratamento para os mesmos;

function checkNumber(n) {
    const result = Number(n);

    if (Number.isNaN(result)) {
        console.log("Valor incorreto!");
        return;
    }

    console.log("Valor correto!");
    return result;
};
checkNumber(5);
checkNumber("10");
checkNumber({});
checkNumber("teste");

//EXEPTIONS
//As exeption são erros que nós geramos no programa;
//Este recurso faz o programa ser abortadp,ou seja,ele não continua sua execução;
//Utilizamos a expressão trow new Error,com a mensagem de erro como argumento
let x = 5

if( x != 6) {
 //   throw new Error("Valor diferente");
};//O usuário nao ler,é como um alerta para devs

//TRY Catch
//Try catch é um recurso famos nas linguagens de programação;
//onde tentamos executar algo em try,e se um erro ocorer ele cai no bloco do catch;
//Útil tanto para debug,como também no desenvolvimento de uma aplicação sólida;
try {
    const soma = x + y;
} catch (erro) {
    console.log(`Erro no programa: ${erro}`);
}
// try catch: Finally
//O finally é uma intrução que vai do bloco try catch;
//Ela executa independente de haver algum erro ou nao em try;
//vai depois do catch
try {
    const valor = checkNumber("2");

    if (!valor) {
      throw new Error("Valor diferente");   
    }
} catch (erro) {
    console.log(`Erro encontrado: ${erro}`);
} finally {
    console.log("O código foi executado!");
};

//ASSERTIONS
//Assertions são quando os tratamentos de valores passados pelo usuário,geram um erro;
//porém este recurso tem o obejetivo nos ajudar no desenv do programa,ou seja,
//seria algo para os deves e não para os usuário;
function checkArray(arr) {
    if(arr.length === 0) {
      throw new Error("Preica passar elementos para o array");
    } else {
        console.log(`O array tem ${arr.length} de elementos`)
    }
};

checkArray([]);
//passando elementos para o array
checkArray([2, 4, 6]);

//Programação Assícrona

