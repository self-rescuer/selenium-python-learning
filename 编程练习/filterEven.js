function  filterEven(numbers){
    let result=[]
    for(let i of numbers){
        if(i%2===0){
            result.push(i)
        }
    }
    return  result
}
console.log(filterEven([19,57,46,38,73]))