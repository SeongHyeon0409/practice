const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let [n, k] = input[0].split(" ");
let course = input[1].split(" ");


for (let i = 1; i <= n; i++){
    k -= course[i-1];
    if (k < 0){
        console.log(i);
        break;
    }
}
if (k >= 0){
    for (let i = n; i >= 1; i--){
        k -= course[i-1];
        if (k < 0){
            console.log(i);
            break;
        }
    }
}

