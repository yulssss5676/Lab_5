

n = int(input("Введіть кількість елементів у масиві: ")) # Кількість елементів у масиві?

array = [] # Створення порожнього списку

for i in range(n):
    element = int(input(f"Введіть елемент {i+1}: "))
    array.append(element) # Зчитування елементів з клавіатури

print("Елементи масиву у зворотному порядку:")
for i in range(n-1, -1, -1):
    print(array[i]) # Зворотній порядок


array = [[0 for j in range(7)] for i in range(7)] # Створення масиу 7x7

for i in range(7):
    for j in range(7):
        array[i][j] = j - 6 + i # Заповнення масиву

for row in array:
    for elem in row:
        print(f"{elem:3}", end=" ")
    print() # Виведення на екран

