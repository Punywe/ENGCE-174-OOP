squares = [x**2 for x in range(10)] #เลขยกกำลัง
print(squares)

squares_dict = {x: x**2 for x in range(5)}#เลขยกกำลัง พร้อมโชว์เลขฐาน
print(squares_dict)

even_squares = {x**2 for x in range(10) if x % 2 == 0}#เลขยกกำลังที่หารเอาเศษแล้วเท่ากับ 0
print(even_squares) 