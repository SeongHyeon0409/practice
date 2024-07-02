function solution(n, t, m, timetable) {
    // 0 < n <= 10이므로
    // 셔틀 출발시간을 배열로 모두 정리해둠
    // 인원수에 따라 셔틀에 배분하고 탑승할 수 있는 가장 마지막 셔틀에 탑승

    let [hour, minute] = strTotime("09:00");
    let restSeat = n * m;
    const depart = [[hour, minute, m]];
    function strTotime(time){
        [a, b] = time.split(":").map(Number);
        return [a, b];
    }
    
    function timeTostr(hour, minute){
        if (hour < 10) hour = `0${hour}`;
        if (minute < 10) minute = `0${minute}`;
        return `${hour}:${minute}`;
        
    }
    for (let i = 1; i < n; i++){
        minute += t;
        if (minute + t > 60){
            hour += 1;
            minute = minute - 60;
        }
        depart.push([hour, minute, m]);
    }
    
    timetable = timetable.map(strTotime);
    timetable.sort((a, b) => {
    if (a[0] === b[0]) {
            return a[1] - b[1];
        } else {
            return a[0] - b[0];
        }
    });

    let answer = [];
    
    for (let i = 0; i < timetable.length; i++){
        let [hours, minute] = [timetable[i][0], timetable[i][1]];
        if (restSeat === 0){
            break
        }
        answer = [hours, minute];

        [dh, dm] = [depart[0][0], depart[0][1]];
        while(depart.length > 1 && ((hours > dh) || (hours >= dh && minute > dm))){
            restSeat -= depart[0][2];
            depart.shift();
            [dh, dm] = [depart[0][0], depart[0][1]];
        }

        if ((hours < dh) || (hours <= dh && minute <= dm)){
            depart[0][2] -= 1;
            restSeat -= 1;
        }

        if (depart[0][2] === 0)depart.shift();

    }



    if (restSeat > 0){
        answer = [depart[depart.length-1][0], depart[depart.length-1][1]];
    }
    else{
        answer[1]--;
        if (answer[1] < 0){
            answer[0]--;
            answer[1] = answer[1] + 60;
        }
    }
    
    return timeTostr(answer[0], answer[1]);
}