

n = int(input("������ ������� �������� � �����: ")) # ʳ������ �������� � �����?

array = [] # ��������� ���������� ������

for i in range(n):
    element = int(input(f"������ ������� {i+1}: "))
    array.append(element) # ���������� �������� � ���������

print("�������� ������ � ���������� �������:")
for i in range(n-1, -1, -1):
    print(array[i]) # �������� �������


array = [[0 for j in range(7)] for i in range(7)] # ��������� ����� 7x7

for i in range(7):
    for j in range(7):
        array[i][j] = j - 6 + i # ���������� ������

for row in array:
    for elem in row:
        print(f"{elem:3}", end=" ")
    print() # ��������� �� �����

