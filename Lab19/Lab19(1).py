import pandas as pd
import numpy as np

# Частина коду з створенням matrix.csv закоментована, тому що файл matrix.csv вже створений
#def matrix_csv(file_path, size):
#    matrix = np.random.randint(1, 10, size=(size, size))
#    
#    df = pd.DataFrame(matrix)
#    df.to_csv(file_path, header=False, index=False)

#matrix_csv('matrix.csv', 2)

df = pd.read_csv('matrix.csv', header=None)

sum_diag1 = df.values.diagonal().sum()

sum_diag2 = df.values[:, ::-1].diagonal().sum()

with open('suma.txt', 'w') as file:
    file.write(f"Сума головної діагоналі: {sum_diag1}\n")
    file.write(f"Сума допоміжної діагоналі: {sum_diag2}\n")
