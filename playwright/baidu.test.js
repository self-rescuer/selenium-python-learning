const { chromium } = require('@playwright/test');

jest.setTimeout(60000); // 全局超时 60 秒

let browser;
let page;

beforeAll(async () => {
    browser = await chromium.launch({ headless: false });
    page = await browser.newPage();
});

afterAll(async () => {
    await browser.close();
});

describe('百度搜索测试', () => {
    const keywords = ['测试开发', '软件测试', 'pytest'];

    test.each(keywords)('搜索关键词：%s', async (keyword) => {
        await page.goto('https://www.baidu.com');

        await page.locator('#kw').evaluate((element, kw) => {
            element.value = kw;
        }, keyword);

        await page.locator('#su').evaluate((element) => {
            element.click();
        });

        // 等待结果出现，给足 55 秒
        // 如果没弹验证，几秒就继续；如果弹了，你有 55 秒手动完成
        console.log('如果出现人机验证，请手动完成...');
        await page.locator('h3.t a').first().waitFor({ timeout: 55000 });

        const titles = await page.locator('h3.t a').allTextContents();
        const validTitles = titles.filter(title => title.trim() !== '');

        expect(validTitles.length).toBeGreaterThan(0);
        console.log(`${keyword} 找到 ${validTitles.length} 条结果，第一条：${validTitles[0]}`);
    });
});