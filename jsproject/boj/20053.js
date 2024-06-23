const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");


for (let i = 1; i <= input[0]; i++){
    let nums = input[i * 2].trim().split(" ").map(v => Number(v));
    let ans = [];
    ans.push(Math.min(...nums));
    ans.push(Math.max(...nums));
    console.log(ans.join(" "));

}