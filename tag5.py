def calcPos(StringLetters, lowest, highest):
    for string in StringLetters:
        if string == "B" or string == "R":
            lowest = lowest + (1 + highest - lowest)/2
        if string == "F" or string == "L":
            highest = highest - (1 + highest - lowest)/2
    solution = highest
    return solution

input = open("input5.txt")
seats = input.read().split("\n")
seatIDs = []

for seat in seats: 
    row = calcPos(seat[:7], 0, 127)
    col = calcPos(seat[7:], 0, 7)
    seatIDs.append(row*8+col)
    

seatIDs = sorted(seatIDs)
rangeSeats = range(min(seatIDs), max(seatIDs))
solution2 = (set(rangeSeats) - set(seatIDs))
print(solution2)
