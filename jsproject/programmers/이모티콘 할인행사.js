function solution(users, emoticons) {
    var answer = [];
    const sail = [10, 20, 30, 40];
    const m = emoticons.length;
    const n = users.length;
    let sails = [];
    
    let box = [];
    function dfs(){
        if (box.length === m) {
            sails.push([...box]);
            return;
        }
        for (let i = 0; i < 4; i++) {
            box.push(sail[i]);
            dfs();
            box.pop();
        }
    }
    dfs();
    
    for (let i = 0; i < sails.length; i++) {
        let subs = 0;
        let buying = 0;
        for (let j = 0; j < n; j++) {
            let [undersail, underbuy] = [users[j][0], users[j][1]];
            let temp = 0;
            for (let k = 0; k < m; k++) {
                if (undersail <= sails[i][k])
                    temp += emoticons[k] - (emoticons[k] * Number(sails[i][k]) / 100);
            }
            if (temp >= underbuy) {
                subs += 1
                temp = 0;
            }
            buying += temp;
        }
        answer.push([subs, buying]);
        answer.sort((a, b) => {
            if (a[0] === b[0]) {
                return b[1] - a[1];
            }
            else
                return b[0] - a[0];
        })
    }

    return answer[0];
}