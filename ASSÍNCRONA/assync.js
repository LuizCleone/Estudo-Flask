//Assícrona
//setTimeout
console.log("Ainda não executou!")

setTimeout(function() {
    console.log("Requisição Assícrona")
},2000);

console.log("Ainda não executou2!")

//FUNÇÃO SETINTERNAL
//A função setInternal é semelhante ao setTimeout,ela é executada após um tempo
//Porém ela nã para de ser executada,temos a sua chamada defenida pelo tempo de espera na execução;
//É como um loop infinito com execução de tempo controlada;
console.log("EXECUTANDO!")

//setInterval(function() {
//    console.log("Requisição do setInternal")
//},3000);//executa a cada 3 segundos infinitamente

console.log("Executou2!")

//PROMISES
//As promises são execuções assíncronas;
//É literalmente uma promessa de um valor que pode chegar em um ponto futuro;
const promessa = Promise.resolve(5 + 5);

console.log("Teste1");

promessa
  .then((valor) => {
    console.log(`A soma é ${valor}`);
    return valor;
  })
  .then((valor) => valor - 1)
  .then((valor) => console.log(`Agora a soma é ${valor}`));

console.log(("Outro valor!"));

//TRATANDO ERROS NAS PROMISES
//Uma promises pode conter um erro,ou dependendo de como o código é executado podemos receber um erro;
//Utilizando a funçao catch para isso,podemos pegar o erro e exibir;
Promise.resolve(5 * "Luiz")
  .then((n) => {
    if (Number.isNaN(n)) {
        throw new Error("Valores Iválidos!");
    }
  })
  .catch((err) => console.log(`Um erro ocorreu: ${err}`));

//REJEITANDO PROMISES
//A rejeição,diferentes do erro,ocorre quando nós deicidimos ejetar uma promises
//Podemos fazer isso com o método rejact
function checarNumero(n) {
    return new Promise((resolve, reject) => {
        if (n > 10) {
            resolve(`O número é maior que 10`);
        } else {
            reject(new Error("Número menor que 10"));
        }
    });
}
const a = checarNumero(15);
const b = checarNumero(9);

a.then((v) => console.log(`O resultado é ${v}`)).catch((err) =>
    console.log(`Um erro ocorreu: ${err}`)
);

b.then((v) => console.log(`O resultado é ${v}`)).catch((err) =>
    console.log(`Um erro ocorreu: ${err}`)
);

//RESOLVENDO VÁRIAS PROMISES
//Com o método all podemos executar várias promises;
//JS se encareega de verificar e retornar os seus valores finais
const p1 = new Promise((resolve, reject) => {
    setTimeout(function () {
        resolve(10);
    },1000);
});

const p2 = Promise.resolve(10 + 10);

const p3 = new Promise((resolve, reject) => {
    if (30 > 10) {
        resolve(30);
    } else {
        reject("Erro!");
    }
});

Promise.all([p1,p2,p3]).then((valores) => console.log(valores));

//ASYNC FUNCTION
//As async funtions são funções que retornam Promises;
//Consequentemente há a possibilidade de receber o resultado delas depois,
//além da utilização dos métodos de Promises;
async function somarDelay(a, b) {
    return a + b;
}

somarDelay(2, 4).then((valor) => {
    console.log(`O valor da soma é ${valor}`);
});

console.log("Teste Async");

//INSTRUÇÃO AWAIT
//SERVE PARA GUARDAR O RESULTADO DE UMA FUNCTION;
//tornando mais simples lidar com este tipo de funçao,desta maneira não precisamos
//trabalhar diretamente com promises
function resolveDelay() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve("Resolver a Promise");
        }, 2000);
    });
}

async function chamadaAsync() {
    console.log("Chamando a Promise, e esperando o resultado");
    const result = await resolveDelay();
    console.log(`O resultado chegou: ${result}`);
}

chamadaAsync();

//Generates
//funcionam de forma semelhante as promises;
//Ações podem se pausadas e continuadas depois;
//Temos novos operadores,como:function* e yield
function* generator() {
    yield 1;
    yield 2;
    yield 3;
}

const gen = generator();

console.log(gen.next().value);
console.log(gen.next().value);
console.log(gen.next().value);