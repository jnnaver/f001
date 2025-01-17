import turtle

def draw_polygon(sides):
    # 터틀 설정E
    my_turtle = turtle.Turtle()
    my_turtle.speed(5)  # 그리기 속도 설정
    side_length = 100  # 각 변의 길이 설정
    
    # 각도 계산
    exterior_angle = 360 / sides
    
    # 다각형 그리기
    for _ in range(sides):
        my_turtle.forward(side_length)
        my_turtle.right(exterior_angle)

def main():
    # 사용자 입력 받기
    while True:
        try:
            sides = int(input("다각형의 각수를 입력해주세요 (3 이상): "))
            if sides < 3:
                print("입력한 숫자가 유효하지 않습니다. 3 이상의 숫자를 입력해주세요.")
                continue
            break  # 유효한 입력이 들어옴
        except ValueError:
            print("유효한 숫자를 입력해주세요.")
    
    draw_polygon(sides)
    turtle.done()

if __name__ == "__main__":
    main()
