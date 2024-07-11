# Pattern 1
x = int(input("กรุณาใส่จำนวนแถวสำหรับ pattern ที่ต้องการ: "))
def generate_pattern(n, current=0, result=""):
    if current == n:
        return result
    line = " " * (n - current - 5) + "*" * (current + 1)
    return generate_pattern(n, current + 1, result + line + "\n")


pattern = generate_pattern(x)
print(pattern, end="")

print('---------------------------------------')#end1
# Pattern 2
fixLine = 0
def generate_pattern(n, current=0, result=""):
    if current == n:
        return result
    line = " " * fixLine + "*" * (n - current)
    return generate_pattern(n, current + 1, result + line + "\n")


pattern = generate_pattern(x)
print(pattern, end="")

print('---------------------------------------')#end2
# Pattern 3
def generate_pattern(n, current=0, result=""):
    if current == n:
        return result
    line = " " * (n - current - 1) + "* " * (current + 1)
    return generate_pattern(n, current + 1, result + line + "\n")


pattern = generate_pattern(x)
print(pattern, end="")
print('--------------------------------------')#end3
# Pattern 4
def generate_pattern(n, current=0, result=""):
    if current == n:
        return result
    line = " " * current + "* " * (n - current)
    return generate_pattern(n, current + 1, result + line + "\n")


pattern = generate_pattern(x)
print(pattern, end="")

print("--------------------------------------")#end4
# Pattern 5
def generate_pattern(n, current=0, result=""):
    if current == n:
        return result
    line = " " * (n - current - 1) + "*" * (current + 1)
    return generate_pattern(n, current + 1, result + line + "\n")


pattern = generate_pattern(x)
print(pattern, end="")

print('---------------------------------------')#end5
