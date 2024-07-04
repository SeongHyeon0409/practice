function solution(n, arr1, arr2) {
    var answer = [];
    const narr1 = [];
    const narr2 = [];
    for (let i = 0; i < n; i++) {
        narr1.push(arr1[i].toString(2).padStart(n, "0"));
        narr2.push(arr2[i].toString(2).padStart(n, "0"));
    }
    
    for (let i = 0; i < n; i++) {
        let temp = '';
        for (let j = 0; j < n; j++) {
            if (narr1[i][j] === '1' || narr2[i][j] === '1')
                temp += '#';
            else
                temp += ' ';
        }
        answer.push(temp);
    }
    console.log(narr1);
    console.log(narr2);
    return answer;
}