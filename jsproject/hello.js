a = {"a" : [1,2]}

for (let i of a["a"]){
    i[0] = 3;
}

console.log(a);