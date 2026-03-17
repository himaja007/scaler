let x = 10; // 'x' is declared and initialized with the value 10
console.log(x); // 10
function letchange(){
    let x = 20; // 'x' is declared and initialized with the value 20, this 'x' is different from the 'x' outside the function due to block scope of 'let'
    console.log(x); // 20
    if (true) {
        let x = 30; // 'x' is declared and initialized with the value 30, this 'x' is different from the 'x' in the function scope due to block scope of 'let'
        console.log(x); // 30
    }
    console.log(x); // 20 (the 'x' in the function scope remains unchanged)
}
letchange();
console.log(x); // 10 (the 'x' outside the function remains unchanged)

/*
var x = 10;
console.log(x); // 10

function change() {
    console.log(x); // 10 (due to hoisting, 'x' is declared but not initialized at this point, so it is 'undefined')
    var x = 20; // This 'x' is a different variable than the one outside the function, due to function scope of 'var'
    if (true) {
        var x = 30; // This 'x' is the same as the one declared in the function scope, so it will overwrite the previous value of 'x' in the function scope
        console.log(x); // 30
    }
    console.log(x); // 20
}

change();
console.log(x); // 10 (the 'x' outside the function remains unchanged)

*/