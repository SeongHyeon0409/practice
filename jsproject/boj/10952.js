const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

for (let i = 0 ; i < input.length-1; i++){
    let n = input[i].split(' ');

    console.log(Number(n[0]) + Number(n[1]));
}

