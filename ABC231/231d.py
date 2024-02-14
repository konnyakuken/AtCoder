N,M = map(int,input().split())
one_person = 0
number_array = list()
if(M ==1 or M == 0):
    print("Yes")
    exit()

for i in range(M):
    A,B = map(int,input().split())
    number_array+=[A,B]

number_array.sort()
count = 0
now_number = number_array[0]
people_count = 0
is_same = False
for person in number_array:
    if(person == now_number):
        if(2 < count):
            print("No")
            exit()
        count +=1
        is_same = True
    else:
        if(count == 1):
            one_person += 1
            if(2 < one_person):
                print("No")
                exit()
        elif(2 < count):
            print("No")
            exit()
        people_count +=1
        count = 1
        now_number = person
        is_same = False
if(is_same == True and count == 2):
    people_count +=1

if(people_count%2 == 1 and one_person == 0):
    print("No")
else:
    print("Yes")



