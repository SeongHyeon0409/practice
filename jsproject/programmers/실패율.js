function solution(N, stages) {
    var answer = [];
    const clear = Array(N+1).fill(0);
    let fail = Array(N+1).fill(0);
    let player = stages.length;
    
    for (let i of stages) {
        clear[i-1]++;
    }

    clear.forEach((n, index) => {
        fail[index] = [n/player, index+1];
        player -= n;
    })
    fail = fail.slice(0, N);
    fail.sort((a, b) => (b[0] - a[0]));
    fail = fail.map(a => a[1]);
    return fail;
}