const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");


let [n, m, v] = input[0].split(" ").map(Number);
let graph = new Array(n + 1);

for (let i = 0; i < graph.length; i++) {
    graph[i] = [];
}

for (let i = 0; i < m; i++) {
    let [from, to] = input[i + 1].split(" ").map(Number);
    graph[from].push(to);
    graph[to].push(from);
}

graph.forEach((element) => {
    element.sort((a, b) => a - b);
});

let visited = new Array(n + 1).fill(0);
let answer_dfs = [];

function dfs(v) {
    if (visited[v]) return;
    visited[v] = 1;
    answer_dfs.push(v);

    for (let i = 0; i < graph[v].length; i++){
        let next = graph[v][i];
        if (visited[next] === 0) {
            dfs(next);
        }
    }
}

dfs(v);
console.log(answer_dfs.join(" "));

visited.fill(0);
let answer_bfs = [];

function bfs() {
    let q = [v];
    while (q.length){
        next = q.shift();
        visited[next] = 1;
        answer_bfs.push(next)
        
        graph[next].forEach(nn => {
            if (visited[nn] === 0){
                visited[nn] = 1;
                q.push(nn);
            }
        });

    }

}
bfs();
console.log(answer_bfs.join(" "));
