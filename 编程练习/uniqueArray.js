function  uniqueArray(arr){
    let end=[]
    for(let i of arr){
        if (end.includes(i)){
            continue
        }
        else{
            end.push(i);
        }
    }
    return end;
}
console.log(uniqueArray([1, 2, 2, 3, 4, 4, 5]));
console.log(uniqueArray(["a", "b", "a", "c"]));
console.log(uniqueArray([]));