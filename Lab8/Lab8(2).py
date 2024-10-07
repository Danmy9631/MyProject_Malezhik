S1 = input("Введіть цілі числа, розділені пробілами: ")
result = ' '.join([f"x={num}" for num in S1.split()])
print(result)