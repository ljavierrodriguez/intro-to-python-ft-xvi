/* 
    Functions
*/

/* 

function functionName(){
    sentences
}

const variableName = function(){
    sentences
}

const variableName = () => {
    sentences
}


*/

function saludo(){
    console.log("Hola");
}

saludo()

const saludo2 = function(){
    console.log("Hola 2");
}

saludo2()

const suma = (a, b) => {
    return a + b;
}

const resta = (a, b) => a - b;

console.log(suma(10, 5)) // 15
console.log(resta(4, 3)) // 1


const bienvenida = (name = "John", lastname = "Doe") => {
    return `Hola, ${name} ${lastname}`; 
}

console.log(bienvenida("Luis", "Smith"))