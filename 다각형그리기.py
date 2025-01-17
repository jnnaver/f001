import turtle

def 다각형그리기함수(변갯수):
    # 터틀 설정E
    터들객체 = turtle.Turtle()
    터들객체.speed(5)  # 그리기 속도 설정
    변길이 = 100  # 각 변의 길이 설정
    
    # 각도 계산
    외각 = 360 / 변갯수
    
    # 다각형 그리기
    for _ in range(변갯수):
        터들객체.forward(변길이)
        터들객체.right(외각)

def main():
    # 사용자 입력 받기
    while True:
        try:
            변갯수 = int(input("다각형의 각수를 입력해주세요 (3 이상): "))
            if 변갯수 < 3:
                print("입력한 숫자가 유효하지 않습니다. 3 이상의 숫자를 입력해주세요.")
                continue
            break  # 유효한 입력이 들어옴
        except ValueError:
            print("유효한 숫자를 입력해주세요.")
    
    다각형그리기함수(변갯수)
    turtle.done()

if __name__ == "__main__":
    main()
