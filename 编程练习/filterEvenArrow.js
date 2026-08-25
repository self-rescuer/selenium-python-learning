const filterEven=numbers=>{
    let result=[]
    for(let i of numbers){
        if(i%2===0){
            result.push(i)
        }
    }
    return  result
}
console.log(filterEven([1, 2, 3, 4, 5, 6]));  // 输出 [2, 4, 6]