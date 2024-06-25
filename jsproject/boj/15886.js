const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");


const n = input[0];
let last = input[1][0];
let ans = 0;
for (l of input[1].slice(1)){
    if (last === 'E' && l === 'W'){
        ans += 1;
    }
    last = l;
        
}

console.log(ans);