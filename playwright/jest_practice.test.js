let counter = 0;

beforeAll(() => {
    console.log('beforeAll：只执行一次');
});

afterAll(() => {
    console.log('afterAll：只执行一次');
});

beforeEach(() => {
    counter = 0;
    console.log('beforeEach：每个用例执行前重置 counter');
});

afterEach(() => {
    console.log(`afterEach：本用例结束时 counter = ${counter}`);
});

describe('钩子函数测试', () => {
    test('用例1：counter加1', () => {
        counter += 1;
        expect(counter).toBe(1);
    });

    test('用例2：counter加2', () => {
        counter += 2;
        expect(counter).toBe(2);
    });
});

describe('断言方法测试', () => {
    test('对象深度相等', () => {
        expect({ a: 1, b: [2, 3] }).toEqual({ a: 1, b: [2, 3] });
    });

    test('数组包含', () => {
        expect([1, 2, 3]).toContain(2);
    });

    test('字符串长度', () => {
        expect("hello").toHaveLength(5);
    });

    test('字符串匹配', () => {
        expect("测试开发").toMatch(/测试/);
    });
});