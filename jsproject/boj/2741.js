const fs = require('fs');
const filefath = "/dev/stdin";
const input = fs.readFileSync(filefath).toString().trim();

let ans = '';
for (let i = 1; i <= input; i++){
    ans = ans + i + '\n';
}
console.log(ans);