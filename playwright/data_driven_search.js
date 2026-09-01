const { chromium } = require('@playwright/test');

async function main() {
    const browser = await chromium.launch({ headless: false });
    const page = await browser.newPage();

    // 测试数据：多个关键词
    const keywords = ['测试开发', '软件测试', 'pytest'];

    for (const keyword of keywords) {
        console.log(`\n===== 搜索关键词：${keyword} =====`);

        // 每次循环重新打开百度首页，保证干净状态
        await page.goto('https://www.baidu.com');

        // 用 evaluate 绕过可见性检查，设置搜索框的值
        await page.locator('#kw').evaluate((element, kw) => {
            element.value = kw;
        }, keyword);

        // 用 evaluate 触发搜索按钮点击
        await page.locator('#su').evaluate((element) => {
            element.click();
        });

        // 等待搜索结果出现
        await page.locator('h3.t a').first().waitFor();

        // 获取所有标题
        const allTitles = await page.locator('h3.t a').allTextContents();

        // 过滤空标题
        const validTitles = allTitles.filter(title => title.trim() !== '');

        console.log(`共找到 ${validTitles.length} 条有效结果：`);
        validTitles.slice(0, 5).forEach((title, index) => {
            console.log(`${index + 1}. ${title}`);
        });
    }

    await browser.close();
}

main();