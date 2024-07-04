names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
city = ["New York", "Los Angeles", "chicago"]

for name, age, city in zip(names, ages, city):#zip คืออการนำเอา ค่าของแต่ละลิสมาเรียนต่อกันอย่างเป็นลำดับ
    print(f"{name} is {age} years old and lives in {city}")