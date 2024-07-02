function solution(places) {
    var answer = [];
    const [dx, dy] = [[0, 1, 1, -1], //아래, 오른쪽, 대각 아래만 확인하면?
                     [1, 0, 1, 1]];
    
    function check(p){
        for (let i = 0; i < 5; i++){
            for (let j = 0; j < 5; j++){
                if (p[i][j] === "P"){
                    for (let d = 0; d < 4; d++){
                        let [nx, ny] = [j+dx[d], i+dy[d]];
                        if (nx < 0 || nx >= 5 || ny < 0 || ny >= 5) continue;
                        if (d < 2){ // 거리 1 상하좌우 확인
                            if (p[ny][nx] === "P") return 0;
                        }
                        else{ // 거리 1 대각선 확인
                            if (p[ny][nx] === "P"){
                                // 사이값 - > p[ny][x], p[y][nx]
                                if (p[ny][j] !== "X" || p[i][nx] !== "X") return 0; 
                            }
                        }
                    }
                    for (let d = 0; d < 2; d++){
                        let [nx, ny] = [j+(dx[d]*2), i+(dy[d]*2)];
                        if (nx < 0 || nx >= 5 || ny < 0 || ny >= 5) continue;
                        // 거리 2 상하좌우 확인
                        if (p[ny][nx] === "P")
                            if (p[i + dy[d]][j + dx[d]] !== 'X') return 0;
                    }
                }
            }
        }
        return 1;
    }
    
    for (let p of places){
        answer.push(check(p));
    }

    // 2칸 떨어져있는 응시자까지의 거리만 확인
    // 1칸이면 false
    // 2칸이면 파티션이 존재하는지 확인 필요.
    // 사실 한번확인 하면 다음 응시자는 전 응시자를 확인할 필요가없음.. < 최적화 필요
    return answer;
    

}