function createcounter(init,delta){
    let x = init;
    let y = delta;
    function count(){
        x = x+y;
        return x;
        }
    return count;
    }

    const c1 = createcounter(10,5)
    const c2 = createcounter(15,2)

    console.log(c1(),c1(),c1()) // 15 20 25
    console.log(c2(),c2(),c2()) // 17 19 21

    