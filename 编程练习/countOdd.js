function    countOdd(numbers){
     let  sum=0
    for(let i of numbers){
        if(i%2!=0){
            sum+=1;
        }
    }
    return  sum;
}
console.log(countOdd([7,8,44,59,68,73]));