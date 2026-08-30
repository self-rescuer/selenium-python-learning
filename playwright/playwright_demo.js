const{chromium}=require('@playwright/test');
async   function main(){
    // 1. 启动浏览器，headless: false 表示显示窗口
    const browser=await chromium.launch({headless:false})
    // 2. 创建新页面
    const page=await browser.newPage();

    // 3. 打开百度首页
    await page.goto('https://www.baidu.com');

    // 4. 获取页面标题并打印
   const title =await page.title();
   console.log('当前页面标题：',title);
    // 5. 关闭浏览器
    await browser.close();
    }

main();