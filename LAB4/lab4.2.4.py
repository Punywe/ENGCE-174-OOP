set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

union_set = set1 | set2
print("Union set:",union_set)
intersection_set = set1 & set2
print("Intersection set:",intersection_set)
difference_set = set1 - set2
print("Difference set:",difference_set)
symmetric_difference_set = set1 ^ set2 #เอาเซต1ที่ไม่อยู่ในเซต2และเอาเว็ต2ที่ไม่อยู่ในเซ็ต1
print("Symmetric difference_set:",symmetric_difference_set)

l = [4,6,5,2,8,1,1,3]
print(sum(l[:-1]))