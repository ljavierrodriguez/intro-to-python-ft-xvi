/* 
Abstracion, Encapsulamiento, Polimorfismo y Herencia
*/

class Person {
    name;
    lastname;
    age;

    constructor(name = "John", lastname = "Doe", age = "Unknow"){
        this.name = name;
        this.lastname = lastname;
        this.age = age;
    }

    comer(){

    }

    correr(){
        this.comer();
        console.log("Person running");
    }
}
class Student extends Person {
    college = null;
    constructor(name, lastname, age, college = "MIT"){
        console.log('Student');
        super(name, lastname, age);
        this.college = college;
    }

    correr(){
        console.log("Student running");
    }
}


let est1 = new Student("Jane", "Doe", 29, "Harvard");

est1.comer()
console.log(est1.name);
console.log(est1.college);
est1.correr();


function saludo(){
    return;
}