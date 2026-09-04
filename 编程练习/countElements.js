function countElements(arr){
    let result={};
    for (let i of arr){
        if (i in result){
            let sum=0;
            for (let j of arr){
                if (j===i){
                    sum+=1;
                }
            }
            result[i]=sum;
        }
        else{
            result[i]=1
        }
    }
    return result
}

console.log(countElements(["a", "b", "a", "c", "b", "a"]));
console.log(countElements([1, 2, 2, 3]));
