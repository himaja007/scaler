console.log(typeof 10)//number
console.log(typeof "Hello")//string
console.log(typeof true)//boolean
console.log(typeof undefined)//undefined
console.log(typeof null)//object (this is a known quirk in JavaScript)
console.log(typeof { name: "John", age: 30 })//object
console.log(typeof [1, 2, 3, 4, 5])//object (arrays are a type of object in JavaScript)
console.log(typeof function() { console.log("Hello") })//function
console.log(typeof Symbol("id"))//symbol
console.log(typeof BigInt(12345678901234567890))//bigint
console.log(typeof NaN)//number (NaN stands for "Not-a-Number", but it is of type number)
console.log(typeof Infinity)//number
console.log(typeof -Infinity)//number
console.log(typeof new Date())//object (Date is a built-in object in JavaScript)
console.log(typeof /abc/)//object (regular expressions are also objects in JavaScript)
console.log(typeof 9.5) //no float type
console.log(typeof 0b1010) //binary
console.log(typeof 0o12) //octal
console.log(typeof 0x1A) //hexadecimal
console.log(typeof 1n) //BigInt literal