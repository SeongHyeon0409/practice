const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim();

for (let i = 1; i <= 9; i++){
    console.log(`${input} * ${i} = ${Number(input) * i}`)
}

