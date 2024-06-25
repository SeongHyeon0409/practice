import sys

# 문자열 입력
words = sys.stdin.readline().rstrip()

# 입력 문자열, 입력 문자열의 시작 인덱스
def solution(input_words, start_idx):

    # 전역 변수 수정 권한
    global result

    # 입력 배열이 비어있으면 리턴
    if input_words == "":
        return

    # 입력 문자열에서 가장 작은 문자 탐색
    min_char = min(input_words)
    # 가장 작은 문자의 인덱스 탐색
    min_char_idx = input_words.index(min_char)

    # 알파벳 위치(입력 문자열의 시작 인덱스 + 가장 작은 문자의 인덱스)에 알파벳 저장
    result[start_idx + min_char_idx] = min_char

    # 결과 배열 출력
    print(''.join(result))

    # 해당 문자 기준 뒷 문자열에 대해 위 함수 실행
    solution(input_words[min_char_idx + 1:], start_idx + min_char_idx + 1)

    # 해당 문자 기준 앞 문자열에 대해 위 함수 실행
    solution(input_words[:min_char_idx], start_idx)

# 결과 배열
result = [''] * len(words)

# 함수 호출 (입력 문자열, 입력 문자열의 시작 인덱스)
solution(words, 0)