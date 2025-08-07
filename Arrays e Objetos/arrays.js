//Arrays são listas,podemos inserir qualquer tipo de dados,usando[] e separando por vírgula
const lista = [1, 2, 3, 4, 5, 6, 7];

console.log(lista);// [1, 2, 3, 4, 5, 6, 7]

console.log(typeof lista);// object

//pode colcar dados diferentes
const dados = ['Luiz', true, 6, 41.2, []];

console.log(dados)//["Luiz", true, 6, 41.2, Array(0)]

// propriedades = são como infomações de um objeto...
const numbers = [1, 2, 3]

console.log(numbers.length);//mostra quantos elementos tem na lista
//ou
console.log(numbers["length"])//mostra quantos elementos tem na lista

const meuNome = "Cleone"

console.log(meuNome.length);//mostra quantos elementos tem na lista
//ou
console.log(meuNome["length"]);//mostra quantos elementos tem na lista

//mais sobre o Array,acessando pelo indeci
const arr = [1, 2, 3, 4, 5, 6, 7]// elementos começa de zero...0,1,2,3,4,5,6
 
console.log(arr[0]);// mostra o 1
console.log(arr[2]);// mostra o 3
console.log(arr[4]);// mostra 0 5
console.log(arr[6]);// mostra o 7

//Métodos
const outrosNumeros = [1, 2, 3];

const todosNumeros = numbers.concat(outrosNumeros);//concatena 2 arrays

console.log(todosNumeros);//mostra 1,2,3,1,2,3

//trabalhando com txt
const txt = "Métodos"

console.log(txt.toUpperCase());//para deixar tudo maiúsculo

console.log(typeof txt.toUpperCase);//mostra que é uma função

console.log(txt.indexOf("o"));//mostra a posição de o

//Aprendendo sobre Objetos
const pessoa = {
    nome: "Luiz Cleone",
    idade: 41,
    trabalho: "Programador",
};

console.log(pessoa);//mostra todos os dado do objeto pessoa

console.log(pessoa.nome);//mostra somente o nome do objeto pessoa( Luiz Cleone)

console.log(pessoa.nome.length)//mostra quanntos caracteres tem o nome 

console.log(typeof pessoa);//mostra o tipo que é objeto

//criando e deletando propeidades em ojetos
const carro = {
    motor: 1.6,
    marca: "gol",
    modelo: "saveiro",
    km:  40000,
}

console.log(carro);

carro.portas = 4;
carro.cor = "verde";

console.log(carro);
//para deletar um objeto
delete carro.km//delata o km de carro

console.log(carro);
//OBS: diferença entre Array e Obejeto
// os arrays são utilizados com lista de itens,geralmente nao possuie, tipo
//já os obejetos são utlizados para descrever um item
//tbm podemos ter um array de objeto

//avançando em obejetos com o método assign
const obj = {
    a: "teste",
    b: true,
};

console.log(obj instanceof Object);//mostra que é verdadeiro ( true )

const obj2 = {
    c: [],
};

Object.assign(obj2, obj);//traz os valores do outro objeto

console.log(obj2);

console.log(obj);

//conhecendo melhor os obejetos como o método keys e método entries
console.log(Object.keys(obj));// mostra a e b
console.log(Object.keys(obj2));//c,a e b
console.log(Object.keys(carro));// mostra as chaves do obejeto ['motor', 'marca', 'modelo', 'portas', 'cor']
// e método entries que mostra o valores do objeto
console.log(Object.entries(carro));

//mutação(Mutabikity)
const a = {
    nome: "Luiz",
};

const b = a;

console.log(a);
console.log(b);

console.log(a === b);//true

a.idade = 40;

console.log(b);//o obejeto b tambem recebe o valor de a

delete b.idade;

console.log(a)//deleta tbm do a

//loop em Arrays
const nomes = ["Lucas", "Pedro", "José", "Zuca"];

for(let i = 0; i < nomes.length; i++) {
    console.log(`Listando os nome: ${nomes[i]}`);
};

//Métodos de Arrays: Push e Pop
// push adicionamos um item ao fim do array
// pop remove o elemento no fim do array
const array = ["b", "c", "d"];

console.log(array.length);//mostra a quantidade de itens no array
console.log(array);//mostra o array com 3 itens
// o push pod adicionar váruios elementos
array.push("e", "f");//adicionando E e F no array
console.log(array.length);//mostra 5 itens no array
console.log(array);//mostra o array com 5 itens
array.pop();//remove o último item do array...remove a letra f
console.log(array);//mostra o array com 4 itens

//o pop mostra o item removido em uma variavel
const itemRemovido = array.pop();//para mostrar o item removido

console.log(itemRemovido);//recupera o útimo item removido
console.log(array);//mostra o array com 4 itens

//Métodos do Array: shift e unshift
//shift remove o primeiro item do array
//unshift adiciona itens no inicio do array
array.unshift("A", "a");//adiciona 2 elementos
console.log(array);//mostra "A", "a", "b", "c", "d", "e"

array.shift("A");//remove o primeiro item da lista
console.log(array);//mostra "a","b","c","d", "e"

//Métodos Array: indexOf e lastIndexOf
//indexOf nos permite encontra o índice de elementos,que passamos como argumento para o método
//lastIndexOf é utilizado quando há repetições de elementos e precisamos do ídice da última ocorrência
//lastIndexOf mostra do ultimo para o primeiro elemento
const listaFrutas = ["Maçã","Banana", "Manga", "Goiaba","Cajú"];
// posicao da lista    "0",   "1",      "2",      "3",   "4"
console.log(listaFrutas.indexOf("Maçã"));//mostra o index pelo elemento,ou seja,a posicao 0
console.log(listaFrutas.lastIndexOf("Cajú"));
//quando passamos um elemento nao existente mostra -1

//Método Array: slice
//o método slice é utlizado para extrair um array menos de um array maior
//passando o intervalo do inicio ao fim,para mostra o ultimo acresenta +1
const testeSlice = ["Lucas", "Pedro", "José", "Zuca","Chico"];

console.log(testeSlice);
const subArray = testeSlice.slice(2, 4);//mostra o terceiro ao penultimo elemento
const subArray2 = testeSlice.slice(0, 4 + 1);//mostra do priemeiro ao ultimo elemento
// ou  .slice(2); mostra todos apartir do indice 2
console.log(subArray);
console.log(subArray2);
//quando nao passamos parametros,ou mesmo parametros inexiste,retorna uma array vazio


//Método Array: forEach
//o forEach é como uma estrutura for ou while,porém é um método
const numeros = [1, 2, 3, 4, 5];

numeros.forEach((numbers) => {
    console.log(`O número é ${numbers}`);
});

const posts = [
    {title: "Primeiro Post", category: "JavaScript"},
    {title: "Segundo Post", category: "Python"},
    {title: "Terceiro Post", category: "PHP"},
];

posts.forEach((post) => {
    console.log(`Exibindo post: ${post.title}, da categoria: ${post.category}`);
});

//Métodos de Array: Includes
//o inlcudes verifica se contém um item no array
const marcas = ["Fiat", "VW", "Toyota"];

console.log(marcas.includes("Fiat"));//retorna true,caso não tenha,retorna false
//exemplo de false
console.log(marcas.includes("VM"));//retorna false,pois não existe no array
//usando uma condição..if
if (marcas.includes("VW")) {
    console.log(`Há carros como essa marca VW!`);
};

//Métodos de Array: reverse
//o método reverse inverte os elementos do array
const reverseTeste = [1, 2, 3, 4, 5, 6];
console.log(reverseTeste);
reverseTeste.reverse();//inverte a seguencia para 6,5,4,3,2,1
console.log(reverseTeste);

//Método com strings: trim
//O trim remove tudo que não é teste em uma string
//nao modifica o originalzusando uma variavel
const trimTeste = "   Testando o trim \n  ";

console.log(trimTeste);//mostra a string com os espeços e o \n
console.log(trimTeste.trim());//mostra a string sem espeços e sem o \n

console.log(trimTeste.length);
console.log(trimTeste.trim().length);

//Método com strings:padStart
// o metodo padStart insere um texto no começo da string
//o texto pode ser repetido
const testePadStarte = "1";
const novoNum = testePadStarte.padStart(4, "0");//aumenta 3 zeros antes do 1

console.log(testePadStarte);
console.log(novoNum);

//tambem tem o padEnd,que acrescenta no final da string
const testePadEnd = novoNum.padEnd(8, "0");//contando do inicio aumenta mais 4 zeros no final,totalizando 8 itens

console.log(testePadEnd);


//Métodos de String: Split
//O split divide uma string em um array,cada elemento será determinado por um separador em como
//os separadores mais utilizados sao:ponto e vígula, vígula e espaço
const frase = "estudando java e aprendendo split e join";
console.log(frase);

const arrayFrase = frase.split(" ");//tranforma em um array

console.log(arrayFrase);//mostra a frase na forma de uma array

//Métodos de String:join
//O join une um array em uma string
const frase2 = arrayFrase.join(" ");//retorna um array como string

console.log(frase2);//mostra a frase como string

//segundo exemplo
const listaCompras = ["Mouse","Teclado","Monitor"];

const itensCompras = `Precisamos comprar: ${listaCompras.join(", ")}.`;

console.log(itensCompras);//muda o array para string

//Método de string: repeat
//o método repeat repete o text n vezes,onde n é o número que colocamos como seu argumento
const palavra = "Testando ";
console.log(palavra.repeat(4));//mostra a palavra testando 5 vezes

//Rest Operator/ Rest parameters
//o rest Operator é caracterizado pelo tres pontos(...),podemos utilizá-lo para receber
//indefinidos argumentos em uma função
const somoInfinita = (...args) => {

    let total = 0;

    for(let i = 0; i < args.length; i++) {
        total += args[i];
    }
    return total;
};
console.log(somoInfinita(1,2,3,4,5,6,7,8,9));

//Estrutura de repetição for...of
const somaInfinita2 = (...args) => {
    let total = 0;

    for (num of args) {
        total += num;
    }
    return total;
};

console.log(somaInfinita2(1,2,3,4,5,6,7,8,9));

//Destructuring em Obejto
//O destructuring é uma funcionalidade que nos permite desestruturar algum dado
//No caso dos objetos,é possível criar variáveis a partir das suas prpopriedades
const dadosUser = {
    nome: "Luiz",
    sobrenome: "Da Paz",
    job: "Programador",  
};

const { nome, sobrenome, job} = dadosUser;

console.log(nome, sobrenome, job);

//renomeando variaveis
const { nome: primeiroNome } = dadosUser;

console.log(nome);

//Destructuring em Arrays
const listaV = ["moto", "carro", "bicicleta"];

const [veiculo1, veiculo2, veiculo3] = listaV;

console.log(veiculo1, veiculo2, veiculo3);

//Conhecendo JSon
//O json,JavaScript Objet Notation,é um dado em formato de texto;
//Utillizamos para comunicação entre api e front-end;
//Sua formatação é rigorosa,se for mal feita o dado é invalidadoe e não conseguinmos comunicação;
//Regras: apenas aspas duplas e não aceita comentários
const myJSon = '{"nome": "Luiz", "idade": 41, "lista": ["PHP", "PYTHON", "JAVASCRIPT"]}';//exemplo

//JSON para Object
const meuObejeto = JSON.parse(myJSon);

console.log(meuObejeto);
//para adicionar propriedade
meuObejeto.isOpenToWork = true;

console.log(meuObejeto);
console.log(typeof meuObejeto);

// convertendo obejeto para JSon

const novoJSON = JSON.stringify(meuObejeto);

console.log(novoJSON);
console.log(typeof novoJSON);















