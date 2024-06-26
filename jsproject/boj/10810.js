const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);

let balls = Array(N).fill(0);
for (let l = 1; l <= M; l++) {
    let [i, j, k] = input[l].split(" ").map(Number);
    for (i; i <= j; i++) {
        balls[i-1] = k;
    }

}

console.log(...balls);

