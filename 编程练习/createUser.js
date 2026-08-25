const createUser = (name, age = 20, city = '武汉') => {
    return {
        name,
        age,
        city
    };
};

const user = createUser('张三', 22, '武汉');
console.log(`姓名：${user.name}，年龄：${user.age}，城市：${user.city}`);