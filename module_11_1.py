import numpy as np
import pandas as pd
# чтение файла
file = pd.read_csv('hw_200.csv')
print(file)
# Показывает первые 20 строк
print(file.head(21))
# Показывает последние 20 строк
print(file.tail(21))
# Показывает информацию минимальных, максимальных,средних, количество строк и тому подобное
print(file.describe())
print()
# Создаем новую колонку, складывая 2 колонки
file['Total'] = file['Height'] + file['Weight']
print(file)

# Сохраняем новый файл
file.to_csv('hf_200v2.csv')
