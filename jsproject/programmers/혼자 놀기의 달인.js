function solution(cards) {
    let box = [];
    let cnt = 0;
    let s = 0;

    while (true) {
        if (cards.reduce((a, b) => a+b, 0) === 0){
            box.push(cnt);
            break;
        }

        if (cards[s] !== 0) {
            var old_s = s;
            s = cards[old_s] - 1; 
            cards[old_s] = 0;
            cnt++;
        }
        else {
            box.push(cnt);
            cnt = 0;
            for (let i = 0; i < cards.length; i++){
                if (cards[i] !== 0) s = i;
            }
        }

    }

    if (box.length === 1) return 0;
    
    else{
       box.sort((a, b) => b-a);
       return box[0] * box[1];
    }

}