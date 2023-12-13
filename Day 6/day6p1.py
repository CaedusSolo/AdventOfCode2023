puzzle = """
Time:        48     98     90     83
Distance:   390   1103   1112   1360""" 

dataArr = puzzle.strip().split("\n")

times = dataArr[0].strip().split(":")[1].strip().split(" ")
distances = dataArr[1].strip().split(":")[1].strip().split(" ")

times = [int(i) for i in times if i]
distances = [int(j) for j in distances if j] 
a = 1

#   Time = 7 ms, record to beat = 9 mm

#   Hold the button for 1 millisecond at the start of the race. Then, the boat will travel at a speed of 
#   1 millimeter per millisecond for 6 milliseconds, reaching a total distance traveled of 6 millimeters.

#   Hold the button for 2 milliseconds, giving the boat a speed of 2 millimeters 
#   per millisecond. It will then get 5 milliseconds to move, reaching a total distance of 10 millimeters.

for time in times:
    current_index = times.index(time)
    ways = 0

    for i in range(1,time+1):
        speed = i
        time_remaining = time - i
        distance = time_remaining * speed 

        if distance > distances[current_index]:
            ways += 1 
    
    a *= ways

print(a)