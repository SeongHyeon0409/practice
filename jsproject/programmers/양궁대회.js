function solution(n, info) {

    function compare(ryan, info) {
        let ps = 0;
        let rs = 0;
        for (let i = 0; i < info.length; i++) {
            if (info[i] < ryan[i]) {
                rs += 10 - i;
            }
            else if (info[i] > 0)
                ps += 10 - i;
        }

        return rs - ps;
    }
    function isLowerScoreBetter(ryan1, ryan2) {
        for (let i = 10; i >= 0; i--) {
            if (ryan1[i] > ryan2[i]) return true;
            if (ryan1[i] < ryan2[i]) return false;
        }
        return false;
    }
    
    let box = Array(11).fill(0);
    let maxDiff = 0;
    let answer = Array(11).fill(-1);
    function dfs(d, left) {
        if (d === 11) { 
            //console.log(...box);
            let diff = compare(box, info);
            if (diff > 0 && (diff > maxDiff || (diff === maxDiff && isLowerScoreBetter(box, answer)))){
                maxDiff = diff;
                answer = [...box];
            }
            return
        }
        
        for (let i = left; i >= 0; i--) {
            box[d] = i;
            dfs(d + 1, left - i);
            box[d] = 0;
        }
        
    }
    
    dfs(0, n);

    return maxDiff > 0 ? answer : [-1];
}