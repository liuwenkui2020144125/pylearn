#total = 0
#count = 0
#average = 0
#input_num = []
smallest = None
biggest = None
while True:
    num = input("please input number")
    if num =='done':
        break;

    try:
        num = float(num)
    except:
        print("Invalid input")
        continue

    if biggest is None or biggest < num:
        biggest = num

    if smallest is None or smallest > num:
        smallest = num
#    for i in input_num:
#       total = total + i
#       count = count + 1
#average = total/count

#print(total, count, average)
print(biggest, smallest)