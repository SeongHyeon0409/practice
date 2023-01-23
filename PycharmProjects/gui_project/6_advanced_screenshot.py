import time
import keyboard
from PIL import ImageGrab

def screenshot():
    # 2020년 6월 1일 10시 20분 30초 -> _20200601_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

print("f9를 입력하면 스크린샷을 찍습니다. esc -> 프로그램 종료")
keyboard.add_hotkey("F9", screenshot)
keyboard.wait("esc") # 사용자가 esc를 누를 때까지 프로그램 수행