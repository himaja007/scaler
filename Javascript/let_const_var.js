let a = 10;
var b = 20;
const c = 30;

console.log(a); // 10

a = 15; // Allowed, 'a' is declared with 'let'
console.log(a); // 15

const o = {a:10};
o.b = 20; // Allowed, we can modify the properties of an object declared with 'const'   
console.log(o); // {a:10, b:20}

console.log(x); // {a:10}
console.log(y); // {a:10}
var x = 113;
var y = 321;

