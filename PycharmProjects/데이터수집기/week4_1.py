f = open('test.txt', 'w')

#w(write): 파일을 새로 쓸 때 사용
#r(read): 이미 존재하는 파일에서 데이터를 읽을 때 사용
#a(append): 이미 존재하는 파일에 내용을 이어 쓰고 싶을 때 사용

f.write("Hello World!\n")
f.write("Good bye.")

f.close()

