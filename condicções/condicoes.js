function criandoFuncoes () {
    console.log('Criando Funções')
}

criandoFuncoes();

//função dentro de uma variavel
const funcaoVariavel = function () {
    console.log('Função dentro de uma variavél');
};

funcaoVariavel();

//funçaõ com parametros
function comArgumento(txt) {
    console.log(`Imprimindo: ${txt}`);//Imprimindo: 
}

comArgumento('Função com argumento!');

//retorno de Funções
const a = 10
const b = 20
const c = 30
const d = 40

function soma(n1, n2) {
    return n1 + n2;
}

const resultado = soma(a, b);

console.log(resultado);
//ou
console.log(soma(c, d));

//escopo de funções
let x = 83;

function escopoDeFuncao() {
    let x = 20;
    console.log(`X dentro da função é: ${x}`);
}

escopoDeFuncao();

console.log(`X fora da função é: ${x}`);

escopoDeFuncao();

// escopo aninhado
let l = 20

function escopoAninhado() {
  let l = 6;

  if (true) {
    let l = 30;

    if (true) {
      let l = 40;

      console.log(l);
    }

    console.log(l);
  }

  console.log(l);
}

escopoAninhado();

console.log(l);

//arrow function : arrow function é uma função anônima,precisa está dentro de uma variavél
const testeArrow =() => {
    console.log('Está é uma Arrow Function!');
}

testeArrow();
//Arrow com Parametro
const parOuImpar = (n) => {
    if (n % 2 === 0) {
        console.log('Par');
        return;
    }

    console.log('Ímpar');
};

parOuImpar(6);

parOuImpar(3);

//explorando Arrow Function
const raizQuadrada = (x) => {
    return x * x;
};

console.log(raizQuadrada(4));

//Arrow Function sem escopo de bloco...OBS:em uma linha
const raizQuadrada2 = (x) => x * x;

console.log(raizQuadrada2(7));

//Arrow sem parametros
const helloWorld = () => console.log('Hello World');
//OBS: já tem o console,se mandar outra vez dar underfine
helloWorld();

//Argumentos Opcionais
const multiplicar = function(m, n) {
    if (n === undefined) {
        return m * 2;
    } else {
        return m * n;
    }
};

console.log(multiplicar(5));

console.log(multiplicar(2, 5));

const greeting = (nome) => {

    if(!nome) {
        console.log('Ôla!!!')
        return
    }
    console.log(`Ôla ${nome}!!!`)
}

greeting();

greeting('Luiz')

//Arguemto default
const customGreeting = (nome, greet = "Ôla") => {
    return `${greet}, ${nome}!`;
};

console.log(customGreeting("Luiz"));

console.log(customGreeting("Cleone", "Bom Dia!!!"));

const repetirTexto = (texto, repetir = 2) => {
    for (let i = 0; i < repetir; i++) {
        console.log(texto);
    }
};

repetirTexto("Testando!!!")

repetirTexto("Agora repete 5x",5);

// Closure = é um conjunto de funções
function someFunction() {
    let txt = "Testando Closure";

    function display() {
        console.log(txt);
    }

    display();
};

someFunction();

//mais sobre closure
const somaEmClosure = (n) => {
    return (m) => {
        return n + m;
    };
};

const s1 = somaEmClosure(5);
const s2 = somaEmClosure(4);

console.log(s1);

console.log(s2);

console.log(s1(5));

console.log(s2(4));

//Recusão = um recurso que permite a função se auto invocar continuarmente,em loop
//precisa definir uma condiçãp final,para parar a execução
const untilTen = (n, m) => {
    if(n < 10 ) {
        console.log("a função partou de executar!");
    } else {
        const x = n - m;

        console.log(x);

        untilTen(x, m);
    }
};

untilTen(100, 10);


function factorial(x) {
    if(x === 0) {
        return 1
    } else {
        return x * factorial(x - 1);
    };
};

const num = 6

const result = factorial(num);

console.log(`O fatorial de ${num} é ${result}`);


