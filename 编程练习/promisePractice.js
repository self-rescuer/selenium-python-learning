function delayMessage(message,delay){
    return  new Promise((resolve)=>{
        setTimeout(()=>{
            resolve(message)
        },delay);
    });
}

function failMessage(message, delay) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            reject(message);
        }, delay);
    });
}


delayMessage('第一消息',2000)
    .then((msg)=>{
        console.log(msg);
        return  delayMessage('第二消息',2000)
    })
    .then((msg)=>{
        console.log(msg);
        return delayMessage('第三消息',2000)
    })
    .then((msg)=>{
        console.log(msg)
    });


delayMessage('第一条消息', 2000)
    .then((msg) => {
        console.log(msg);
        return failMessage('第二条消息加载失败', 2000);
    })
    .then((msg) => {
        console.log(msg);
        return delayMessage('第三条消息', 2000);
    })
    .then((msg) => {
        console.log(msg);
    })
    .catch((error) => {
        console.log('捕获到错误：' + error);
    });

