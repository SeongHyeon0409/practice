const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

ans = [];

for (let i = 1; i <= input[0]; i++){
  let [a, b] = input[i].trim().split(" ");
  ans.push((BigInt(`0b${a}`) + BigInt(`0b${b}`)).toString(2));
}

console.log(ans.join("\n"));