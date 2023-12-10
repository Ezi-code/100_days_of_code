items = [1, 2, 3, 4, 5,1,6,7,8,9,10,10,10,11,12,13,14,15,16,17,18,19,20]

duplicate = ''
for i in items:
    if items.count(i) > 1:
        print(i)