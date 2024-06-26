const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);

// Initialize the balls array with values from 1 to N
let balls = Array.from({ length: N+1 }, (_, index) => index);


for (let l = 1; l <= M; l++) {
    let [i, j] = input[l].split(" ").map(Number);
    [balls[i], balls[j]] = [balls[j], balls[i]];

}

console.log(...balls.slice(1));


