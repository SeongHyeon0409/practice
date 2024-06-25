const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

n = input[0];
cow = new Array(11).fill(-1);
ans = 0;
for(let i = 1; i <= n; i++){
    let[c, lo] = input[i].trim().split(" ").map(Number);
    if (cow[c] === 1 && lo === 0) ans += 1;
    else if (cow[c] === 0 && lo === 1) ans += 1;
    cow[c] = lo;
}

console.log(ans);
