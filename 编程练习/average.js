function average(numbers){
    let sum=0;
    for(let i of numbers){
        sum+=i;
    }
    let result=(sum/numbers.length).toFixed(2);
    return result
}
console.log(average([1, 2, 3, 4]));
console.log(average([10, 20, 30]));
console.log(average([5]));