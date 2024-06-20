const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

for (let i = 1 ; i < input.length; i++){
    let n = input[i].split(' ');

    console.log(`Case #${i}: ${n[0]} + ${n[1].trim()} = ${Number(n[0]) + Number(n[1])}`);
}

