function solution(tickets) {
    const airline = {};
    let visited = {};
    for (let t of tickets){
        if (Object.keys(airline).includes(t[0])) airline[t[0]].push([t[1], 0]);
        else airline[t[0]] = [[t[1], 0]];
    }
    
    let box = ["ICN"];
    let answer = [];
    
    function dfs(s, d){
        // 모든 티켓을 사용한 경우 d > tickets.length
        if (d === tickets.length) {
            answer.push([...box]);
        }
        
        if (!Object.keys(airline).includes(s)) return;

        
        airline[s].forEach((value, index, array) => {
            if (value[1] === 0){
                array[index][1] = 1;
                box.push(array[index][0]);
                dfs(array[index][0], d+1);
                array[index][1] = 0;
                box.pop();
            }
        });
    }
    

    dfs("ICN", 0);
    answer.sort();
    return answer[0];
}