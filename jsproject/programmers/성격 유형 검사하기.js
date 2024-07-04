function solution(survey, choices) {
    var answer = '';
    var mbti = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0};
    
    for (let i =0; i < survey.length; i++){
        if (choices[i] <= 3){
            mbti[survey[i][0]] += 4 - choices[i];
        }
        else if (choices[i] >= 5){
            mbti[survey[i][1]] += -4 + choices[i];
        }
    }
    
    const types = ["RT","CF","JM","AN"];
    return types.map(([a, b]) => mbti[b] > mbti[a] ? b : a).join("");

}