const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];

let input = [];
rl.on("line", (line) => {
    lines.push(line);
    if (line === '0 0') {
        rl.close();
    }
});

rl.on("close", () => {
  input.map((v) => console.log(v));
  process.exit();
});