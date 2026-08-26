const  students =[
{name:'张三',age:19,id:58741,gender:'男'},
{name:'李四',age:21,id:56741,gender:'女'},
{name:'王五',age:22,id:55741,gender:'男'}
]
students.forEach(student=>console.log(student.name))

const names=students.map(student=>student.name)
console.log(names)

const boys=students.filter(student=>student.gender==='男')
console.log(boys)

const firstOver20=students.find(student=>student.age>=20)
console.log(firstOver20)