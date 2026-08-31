const { chromium } = require('@playwright/test');

async function main() {
    const browser = await chromium.launch({ headless: false });
    const page = await browser.newPage();

    await page.goto('https://www.baidu.com');

    await page.locator('#kw').evaluate((element) => {
        element.value = '测试开发';
    });

    await page.locator('#su').evaluate((element) => {
        element.click();
    });

    await page.locator('h3.t a').first().waitFor();

    const titles = await page.locator('h3.t a').allTextContents();

    console.log('搜索到的结果标题：');
    titles.forEach((title, index) => {
        console.log(`${index + 1}. ${title}`);
    });

    await browser.close();
}

main();