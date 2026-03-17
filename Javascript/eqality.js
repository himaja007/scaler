console.log(1 == '1') //true (loose equality, type coercion occurs)
console.log(1 === '1') //false (strict equality, no type coercion)

console.log (0 == false) //true (loose equality, type coercion occurs)  
console.log (0 === false) //false (strict equality, no type coercion)

console.log (null == undefined) //true (loose equality, type coercion occurs)

let arr1 = [1, 2, 3]
let arr2 = [1, 2, 3]
let arr3 = arr1

console.log(arr1 == arr2) //false (arrays are reference types, so they are not equal even if their contents are the same)
console.log(arr1 === arr2) //false (same reason as above)
console.log(arr1 == arr3) //true (arr1 and arr3 reference the same array in memory)
console.log(arr1 === arr3) //true (same reason as above)

