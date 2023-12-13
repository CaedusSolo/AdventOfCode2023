puzzle = """Time:        48     98     90     83
Distance:   390   1103   1112   1360"""

dataArr = puzzle.strip().split("\n")

times = dataArr[0].strip().split(":")[1].strip().split(" ")
distances = dataArr[1].strip().split(":")[1].strip().split(" ") 
time = ""
distance = ""

times = [time for time in times if time]
distances = [distance for distance in distances if distance]

for t in times:
    time += t 

for d in distances:
    distance += d 

time = int(time)
distance = int(distance)
ways = 0 

for i in range(1,time+1):
    speed = i 
    time_remaining = time - i 
    distance_travelled = speed * time_remaining 

    if distance_travelled > distance:
        ways += 1

print(ways) 