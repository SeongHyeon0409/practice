const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().split("\n").map(v => Number(v));


console.log(input[0] + input[1]);
