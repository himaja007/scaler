function a() {
    let x = 10; // 'x' is declared and initialized with the value 10
    let p = 1;
    function b(){
        let x=10; // 'x' is declared and initialized with the value 10, this 'x' is different from the 'x' in the outer function due to block scope of 'let'
        p = 2;
    }
}