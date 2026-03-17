function createGreeting(greeting) {
    function greet (name) {
        console.log(greeting + ' ' + name + '!');
    }
    return greet;
}

const sayHello = createGreeting('Hello');
const sayHi = createGreeting('Hi');

sayHello('Alice'); // Output: Hello Alice!
sayHi('Bob'); // Output: Hi Bob!



const arr = [-1, 12, 32, 34, 5];
function compareNumbers(a, b) {
    return a - b;
}
console.log(arr.sort(compareNumbers)); // Output: [-1, 5, 12, 32, 34] (the array is sorted in ascending order using the compareNumbers function)