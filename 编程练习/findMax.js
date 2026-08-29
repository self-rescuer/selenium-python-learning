function findMax(numbers){
    let  max=numbers[0];
    for (let i=0;i<numbers.length;i++){
        if  (numbers[i]>=max){
            max=numbers[i];
        }
    }
    return max
}
console.log(findMax([3, 1, 4, 1, 5, 9, 2]));
console.log(findMax([-10, -5, -20]));
console.log(findMax([7]));