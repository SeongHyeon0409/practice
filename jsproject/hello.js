const dateToearthdays = (year, month, day) => {
    const days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    let total_days = (year - 1) * 365 + Math.floor((year - 1) / 4 ) // 기본 년수 + 윤년 계산
    
    for (let m = 0; m < month-1; m++)
        total_days += days_in_month[m]
    
    if (month > 2 && year % 4 == 0)  // 윤년 체크
        total_days += 1
    
    total_days += day
    return total_days
};

console.log(dateToearthdays(3, 3, 1))  // 738201