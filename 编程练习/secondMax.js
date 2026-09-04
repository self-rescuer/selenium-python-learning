function secondMax(numbers){
    let max=numbers[0];
    for (let i of numbers){
        if (i>=max){
            max=i;
        }
    }
    let newNumbers=numbers.filter(item=>item!==max)
    let second=newNumbers[0];
    for (let i of newNumbers){
        if (i>=second){
            second=i;
        }
    }
    return second
}

console.log(secondMax([1, 3, 5, 2]));
console.log(secondMax([5, 5, 3, 4]));
console.log(secondMax([10, 10, 10, 8]));
console.log(secondMax([7, 6]));