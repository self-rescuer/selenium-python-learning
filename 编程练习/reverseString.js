function reverseString(str){
    const result=[];
    for(let i=0;i<str.length;i++){
        result[i]=str[str.length-1-i];
    }
    const end= result.join('');
    return  end
}
console.log(reverseString("hello"));
console.log(reverseString("JavaScript"));
console.log(reverseString(""));