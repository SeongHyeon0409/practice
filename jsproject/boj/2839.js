const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
let input = fs.readFileSync(filePath).toString().trim();
input = Number(input);

let dp = new Array(input+5).fill(5001);

dp[3] = 1;
dp[5] = 1;
for (let i = 6; i < input+1; i++){
    dp[i] = Math.min(dp[i-3]+1, dp[i-5]+1)
}

if (dp[input] > 5000){
    console.log(-1);
}
else{
    console.log(dp[input])
}