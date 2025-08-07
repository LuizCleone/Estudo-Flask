//métodos POO
const animal = {
    nome: "TOTÓ",
    latir: function() {
        console.log("Au au");
    },
};
console.log(animal.nome);

animal.latir();

//exe2. A profudando em Métodos POO
// usando o this
const pessoa = {
    nome: "Luiz",

    getNome: function () {
        return this.nome;//retornar o nome Luiz
    },

    setNome: function (novoNome) {
        this.nome = novoNome;//retorna Luiz
    },
};

//sem alteração
console.log(pessoa.nome);

console.log(pessoa.getNome());

pessoa.setNome("Cleone")//alterando o valor de nome..

console.log(pessoa.getNome());

//Sobre o Prototype
//Prototype é um recurso que faz parte da arquitetura de JavaScript;
//É uma especié de herança,onde obejetos pais herdam proprieadades e métodos aos filhos;
//Por isso muitos dados são considerados obejetos e temos obejetos, como: String, Number, e outros;
//Ou seja,cada dado tem um obejeto pai que herdou característica pelo prototype...
//O recurso fudamental do prototype que temos que entender é o fallback
//exe
const texto = "Prototype"
console.log(Object.getPrototypeOf(texto));

// função como classe - função construtora
function criarCachorro(nome, raca) {
    const cachorro = Object.create({});

    cachorro.nome = nome;
    cachorro.raca = raca;

    return cachorro;
};

const bob = criarCachorro("Bob", "Vira-Lata");
const jalidisse = criarCachorro("Jalidisse", "Vira-Lata");

//console.log(bob);

const cojack = criarCachorro("Cojack", "PitBull");

console.log(bob, jalidisse, cojack);

//Funções como classe - usando o new
function Cacharro(nome, raca) {
    this.nome = nome;
    this.raca = raca;
};
const husky = new Cacharro("Norbit", "Pischer");

console.log(husky);

//Classes em JavaScript ES6
//nas versões atuais de Js abandonamos as funções e utilizamos as classes;
//aqui temos recursos comuns em outras linguagens,como o construtor
//Além da instância new
class CacharroClasse {
    constructor(nome, raca) {
        this.nome = nome;
        this.raca = raca;
    };
};
const lili = new CacharroClasse("Lili", "Poodle");
console.log(lili);

//Mais sobre classes
class Caminhao {
    constructor(eixos, cor, cavalos) {
        this.eixos = eixos;
        this.cor = cor;
        this.cavalos = cavalos;
    }
    descreverCaminhao() {
        console.log(`O caminhão tem ${this.eixos} eixos,das cor ${this.cor} com ${this.cavalos} cavalos de potência`);
    }
};

const scania = new Caminhao(7, "Preta", 420);

console.log(scania)

scania.descreverCaminhao();

// Override
class Humano {
    constructor(nome, idade) {
       this.nome = nome;
       this.idade = idade; 
    }
};
const cleone = new Humano("Cleone", 41);
console.log(cleone);

//Symbols em Classes
//Quando utilizamo o recurso de symbol com classe,é possível criar propriedade única e imutável;
//Isso é útil quando há algum dado que se repetirá em todos os obejetos criados a partir da classe
class Aviao {
    constructor(marca, turbina) {
        this.marca = marca;
        this.turbina = turbina;
    }
};
const asas = Symbol();
const pilotos = Symbol();
Aviao.prototype[asas] = 2;
Aviao.prototype[pilotos] = 3;

const boeing = new Aviao("Boeing", 6);
console.log(boeing);
//com prototype
console.log(boeing[asas]);
console.log(boeing[pilotos]);
//console.log(boeing[asas, pilotos]);

//Getters e Setters
//Ambos são bem famosos na POO
//O get é utilizado para exibir o valos de alguma propriedade
//O set é utilizado para alterar o valor
class Post {
    constructor(titulo, descricao, tags) {
        this.titulo = titulo;
        this.descricao = descricao;
        this.tags = tags;
    }

    get exibirTitulo() {
        return `Usando o Getters e o Setters: ${this.titulo}`;
    }

    set adicionarTags(tags) {
        const tagsArray = tags.split(", ");
        this.tags = tagsArray;
    };
};
const myPost = new Post("Esse Post","É sobre Programação");

console.log(myPost);
console.log(myPost.exibirTitulo);

myPost.adicionarTags = "JavaScript, Python, Java, PHP";

console.log(myPost);

//Herança
class Mamifero {
    constructor(patas) {
        this.patas = patas;
    };
};

class Lobo extends Mamifero {
    constructor(patas, nome) {
        super(patas, patas);
        this.nome = nome;
    }
}

const shark = new Lobo(4, "Brutus");
console.log(shark);
console.log(shark.patas);

//Operado Instanceof
//Assim como o typeof que verifica o tipo,temos o operador instanceof
//Que verifica de um objeto é pai de outro,para ter certeza da ancestralidade;
//Isso é verificado com objeto => classe,e não através das classes
console.log(shark instanceof Lobo);//verifica se é criado da classe...retorna true
//só retorna da classe


