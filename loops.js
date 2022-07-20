/* 
    Loops 
*/

/* 

for (inicializador; condition; increment){
    sentences
}

for(index in values){
    sentences
}

for(value of values){
    sentences
}

while(condition){
    sentences
}

do {
    sentences
} while (condition)

*/

for(let i = 1; i <= 10; i++){
    console.log(i);
}

let nombres = ["Hugo", "Pago", "Luis"];

for(let i = 0; i < nombres.length; i++){
    console.log(nombres[i]);
}

for(let index in nombres){
    console.log(nombres[index])
}

for(let nombre of nombres){
    console.log(nombre)
}

let i = 0;
while(i < nombres.length){
    console.log(nombres[i]);
    i++;
}