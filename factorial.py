def calculate_factorial(num):
    if num < 0:
        return "음수는 팩토리얼을 계산할 수 없습니다."
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

try:
    input_num = int(input("팩토리얼을 계산할 정수를 입력하세요: "))
    factorial_result = calculate_factorial(input_num)
    if isinstance(factorial_result, str):
        print(factorial_result)
    else:
        print(f"{input_number}의 팩토리얼은 {factorial_result}입니다.")
except ValueError:
    print("유효한 정수를 입력해 주세요.")
