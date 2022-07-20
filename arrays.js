/* 
    Arrays
*/

let nombres = [];


console.log(typeof(nombres))

nombres.push("Hugo");
nombres.push("Paco");

//nombres.pop()

nombres = nombres.filter((elem) => elem !== 'Hugo')

nombres = nombres.map((elem) => elem.toUpperCase())

console.log(nombres);

