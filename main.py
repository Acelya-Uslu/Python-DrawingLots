import random
import time

count=0
total=int(input("How many people participate in draw?"))

def draw(count,total):
    while total > count:
        list1 = []
        count += 1
        name= input("Name:")
        list1.append(name)


    winner=random.choice(list1)

    duration=3
    while True:
        print(duration)
        time.sleep(1)
        duration-=1
        if duration==0:
            print("---",winner+"---")
            break
        else:
            continue

draw(count,total)