S1=input("Введіть перший рядок: ")
S2=input("Введіть другий рядок: ")
result=S1
for i in S2:
    result=result.replace(i, '')
print("Символи з першого рядка, яких немає у другому: ", result)
