const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim();


console.log(input === input.split("").reverse().join("") ? 1 : 0);

