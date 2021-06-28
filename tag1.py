numbersRead = open("input1.txt")
numbers = (numbersRead.read().split('\n'))
numbersRead.close()
numbers = [int(i) for i in numbers]
for num1 in numbers: 
    for num2 in numbers: 
        if num1 + num2 == 2020: 
            solution = num1*num2
            print(solution)
            break 
     
for num in numbers: 
    for numb in numbers: 
        if 2020-num-numb in numbers: 
            print(num*numb*(2020-num-numb))
            break 
        

