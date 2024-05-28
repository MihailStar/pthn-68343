# 1
def func(num1: int, num2: int) -> bool:
    return num1 % num2 == 0


print("" if func(*(int(input()) for _ in range(2))) else "не ", "делится", sep="")
