let a = 10;
function change(b){
    b = 2;;
}
change(a)
console.log(a) //10 (primitive types are passed by value, so the original variable 'a' remains unchanged)   

let x=[1,2,3]
function changeArray(y){
    y.push(4);
}
changeArray(x)
console.log(x) //[1,2,3,4] (arrays are reference types, so the original array 'x' is modified when we push a new element into it)