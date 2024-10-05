num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("다음 숫자를 입력하세요: "))

sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2 if num2 != 0 else "0으로 나눌 수 없습니다."

print(f"두 숫자의 합: {sum_result}")
print(f"두 숫자의 차: {diff_result}")
print(f"두 숫자의 곱: {product_result}")
print(f"두 숫자의 나눗셈: {quotient_result}")