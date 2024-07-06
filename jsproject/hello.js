

const a = [1,2,3,4,5];
a.forEach((n, idx, arr) => {
    console.log(n, idx, arr);
})

b = a.reduce((acc, cur, idx) => {
    console.log(acc, cur, idx);
    return acc + cur;
  }, 0);

console.log(b);