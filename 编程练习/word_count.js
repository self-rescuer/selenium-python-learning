function word_count(text){
    for(let i of text){
        i.toLowerCase()
    }
    let words=text.split(' ')
    let result={}
    for(let i of words){
        if (i in result){
            result[i]+=1;
        }
        else{
        result[i]=1
        }
    }
    return result
}
console.log(word_count("hello world hello"))

console.log(word_count("Python is great and python is fun"))
