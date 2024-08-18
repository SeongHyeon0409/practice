const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().split('\n');

const n = Number(input[0]);
let answer = 0;
let max_temp = 0;
for (let i = 1; i < n + 1; i++) {
  const pay = Number(input[i].split(' ')[0]);
  let temp = 0;
  for (let i = 1; i < n + 1; i++) {
    if (Number(input[i].split(' ')[0]) >= pay) {
      const temptemp = pay - Number(input[i].split(' ')[1]);
      if (temptemp > 0) {
        temp += temptemp;
      }
    }
  }
  if (temp === max_temp && pay < answer) {
    answer = pay;
  }
  if (temp > max_temp) {
    max_temp = temp;
    answer = pay;
  }
}
console.log(answer);
