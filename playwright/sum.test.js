function sum(a,b){
    return a+b;
}
test('两数相加',()=>{
    expect(sum(4,5)).toBe(9)
    expect(sum(-1,1)).toBe(0)
});
test('浮点数相加',()=>{
    expect(sum(1.2,2.9)).toBe(4.1)
});
