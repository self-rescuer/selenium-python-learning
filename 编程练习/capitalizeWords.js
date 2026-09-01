function capitalizeWords(str) {
    let words = str.split(' ');
    let result = words.map(word => {
        return word[0].toUpperCase() + word.slice(1).toLowerCase();
    });
    return result.join(' ');
}
console.log(capitalizeWords("hello world"));        // 输出 "Hello World"
console.log(capitalizeWords("javascript is fun")); // 输出 "Javascript Is Fun"
console.log(capitalizeWords("HELLO WORLD"));       // 输出 "Hello World"