const users = [
    { name: "张三", age: 18 },
    { name: "李四", age: 20 },
    { name: "王五", age: 25 },
    { name: "赵六", age: 17 }
];
function getAdultNames(users){
    const result=users
    .filter(user=>user.age>=20)
    .map(user=>user.name);
    return  result
}
console.log(getAdultNames(users))