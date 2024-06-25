const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

ans = [];
alpha = {};
n = Number(input[0].trim());

for (let i = 65; i <= 90; i++){
  alpha[String.fromCharCode(i)] = 0;
}

for (i = 1; i <= n; i++){
  flag = 0;
  temp = '';
  input[i].trim().split(" ").forEach(c => {
    if (alpha[c[0].toUpperCase()] === 0 && flag === 0){
      alpha[c[0].toUpperCase()] = 2;
      flag = 2;
      for (j = 0 ; j < c.length; j++){
        if (j===0) temp += `[${c[0]}]`;
        else temp+= c[j];
      }
    }
    else{
      temp += c;
    }
    temp += ' ';
  })

  if (flag === 2){
    ans.push(temp);
    continue;
  }


  temp = '';
  flag = 0;
  for (let j = 0; j < input[i].length; j++){
    if (alpha[input[i][j].toUpperCase()] === 0 && flag === 0){
      alpha[input[i][j].toUpperCase()] = 1;
      flag = 1;
      temp += `[${input[i][j]}]`;
    }
    else{
      temp += input[i][j];
    }
  }
  ans.push(temp);
}


console.log(ans.join("\n"));
