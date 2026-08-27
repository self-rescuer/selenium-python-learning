// 1. 创建对象
const student = {
    name: "张三",
    age: 20,
    courses: ["数学", "英语"]
};

// 2. 添加属性
student.gender = "男";

// 3. 遍历对象
console.log("遍历对象：");
for (let [key, value] of Object.entries(student)) {
    console.log(`${key}: ${value}`);
}

// 4. 对象转 JSON 字符串
const jsonStr = JSON.stringify(student);
console.log("JSON 字符串：");
console.log(jsonStr);

// 5. JSON 字符串转对象
const parsed = JSON.parse(jsonStr);
console.log("解析回对象：");
console.log(parsed.name);
console.log(parsed.courses);

// 6. 深拷贝
const copied = JSON.parse(JSON.stringify(student));
copied.courses.push("物理");
console.log("原对象 courses：", student.courses);
console.log("拷贝对象 courses：", copied.courses);