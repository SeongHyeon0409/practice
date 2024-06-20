const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

for (let i = 0 ; i < input.length; i++){
    console.log(input[i]);
}

process.stdout.write("abc\nabc")