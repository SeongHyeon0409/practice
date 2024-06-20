const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString();
for (let i = 1; i <= input; i++) {
    console.log("*".repeat(i));
  }