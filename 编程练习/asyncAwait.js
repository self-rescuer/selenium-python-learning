function delayMessage(message,delay){
    return  new Promise((resolve)=>{
        setTimeout(()=>{
            resolve(message);
        },delay);
    });
}

function  failMessage(message,delay){
    return new  Promise((resolve,reject)=>{
        setTimeout(()=>{
            reject(message);
        },delay);
    });
}

async function main(){
try{
    const msg1=await  delayMessage('第一条消息',2000);
    console.log(msg1);
    const msg2=await   delayMessage('第二条消息',2000);
    console.log(msg2);
    const msg3=await  delayMessage('第三条消息',2000);
    console.log(msg3);
    }catch(error){
        console.log('捕获到错误：'+error);
    }
}
main();
console.log('这条先打印');