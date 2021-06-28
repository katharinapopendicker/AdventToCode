passwordsRead = open("input2.txt")
passwords = (passwordsRead.read().split('\n'))
validpw = 0

#Teil 1
for pw in passwords: 

     requirement, passw = pw.split(": ")
     numbers, letter = requirement.split(" ")
     least, most = numbers.split("-")
     least = int(least)
     most = int(most) 
     if least <= passw.count(letter) <= most: 
         validpw = validpw + 1

print(validpw)

#Teil 2 
solution2 = 0
for pw in passwords: 

     requirement, passw = pw.split(": ")
     numbers, letter = requirement.split(" ")
     least, most = numbers.split("-")
     least = int(least)
     most = int(most) 
     if passw[least-1] == letter and passw[most-1]!=letter or passw[most-1] == letter and passw[least-1] != letter:
         solution2 = solution2 + 1

print(solution2)

