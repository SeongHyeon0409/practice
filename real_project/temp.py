def find_overlap(ranges):
    # ranges: [(start1, end1), (start2, end2), ...]
    start, end = ranges[0]
    for r_start, r_end in ranges[1:]:
        start = max(start, r_start)
        end = min(end, r_end)
    return (start, end) if start < end else None

ranges = [[2, 4], [3, 6], [4, 5], [3, 4], [4, 5]]
overlap = find_overlap(ranges)
if overlap:
    print(f"{overlap[0]} < f <= {overlap[1]}")
else:
    print("겹치는 부분이 없습니다.")