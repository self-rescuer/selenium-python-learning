function countChar(str,char){
    let number=0;
        for(let i of str){
            if(i===char){
                number+=1;
            }
        }
        return number
}
console.log(countChar("hello world", "o"));
console.log(countChar("JavaScript", "a"));
console.log(countChar("abc", "d"));