const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");


key = [['q','w','e','r','t','y','u','i','o','p'],
        ['a','s','d','f','g','h','j','k','l'],
        ['z','x','c','v','b','n','m']];

right = ['y','u','i','o','p','h','j','k','l','b','n','m'];

let [sl, sr] = input[0].trim().split(" ");
let zoac = input[1].trim().split("");


let time = 0;

function lenkey(a, b) {
    for (let i = 0; i < key.length; i++){
        if (key[i].includes(a)) [xl, yl] = [i, key[i].indexOf(a)];
        if (key[i].includes(b)) [xr, yr] = [i, key[i].indexOf(b)];
    }
    return Math.abs(xl - xr) + Math.abs(yl - yr);
}

let xl, yl, xr, yr;

// for (let i = 0; i < key.length; i++){
//     if (key[i].includes(sl)) [xl, yl] = [i, key[i].indexOf(sl)];
//     if (key[i].includes(sr)) [xr, yr] = [i, key[i].indexOf(sr)];
// }

zoac.forEach(z => {

    if (right.includes(z)){
        time += lenkey(z, sr);
        sr = z;
    }
    else{
        time += lenkey(z, sl);
        sl = z;
    }
    time += 1;

})

console.log(time);

