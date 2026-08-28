function sumArray(numbers){
    let result=0;
    for(number of numbers){
        result+=number;
    }
    return  result;
}
console.log(sumArray([1, 2, 3, 4]));    // 输出 10
console.log(sumArray([-1, 5, 3]));      // 输出 7
console.log(sumArray([]));              // 输出 0


'以下是用forEach方法实现'
//function sumArray(numbers) {
//    let result = 0;
//    numbers.forEach(number => {
//        result += number;
//    });
//    return result;
//}
