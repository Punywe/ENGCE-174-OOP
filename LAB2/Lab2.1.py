# รับค่าจากผู้ใช้
height = int(input("กรุณาใส่จำนวนแถวสำหรับ pattern ที่ต้องการ: "))

# Pattern 1
for i in range(1, height):
    print('*' * i)
print('-------------')

# Pattern 2
for n in range(height, 1, -1):
    print('*' * n)
print('-------------')

# Pattern 3
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")#end คือทำให้ลูปไม่ขึ้นบรรทัดใหม่
    for k in range(i + 1):
        print("*", end=" ")
    print()
print('-------------')

# Pattern 4
for i in range(height, 0, -1):
    for j in range(height - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
print('-------------')

# Pattern 5
for i in range(height):
    for J in range(height - i - 1):
        print(" ", end="")
    for K in range(i + 1):
        print("*", end="")
    print()
print('-------------')
