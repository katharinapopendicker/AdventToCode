import re 
input = open("input4.txt")
passports = input.read().split("\n\n")
valid = 0
for p in passports:
    if ("hgt" in p) & ("byr" in p) & ("iyr" in p) & ("eyr" in p) & ("hcl" in p) & ("ecl" in p) & ("pid" in p):
        valid = valid+1
print(valid)

#teil2 
validTrue = 0
for p in passports: 
    split = p.split()
    #print(split)
    valid2 = 0
    for keys in split:
        key,value=keys.split(":")
        print(key, value)
        if key == "byr":
            if 1920<=int(value)<=2002:
                valid2 += 1
        elif key == "iyr":
            if 2010<=int(value)<=2020:
                valid2+=1
        elif key == "eyr":
            if 2020<=int(value)<=2030:
                valid2+=1
        elif key == "hgt":
            print(value[-2], value[:-2])
            if (value[-2] == "c" and value[-1] == "m" and 150 <= int(value[:-2]) <= 193) or (value[-2] == "i" and value[-1] == "n" and 59 <= int(value[:-2]) <= 76):
                valid2+=1
        elif key == "hcl":
            if re.match('^#[0-9a-f]{6}$', value):
                valid2+=1
        elif key == "ecl":
            if value == "amb" or value=="blu" or value=="gry" or value=="brn" or value=="grn" or value=="hzl" or value=="oth":
                valid2+=1
        elif key == "pid":
            if re.match('^[0-9]{9}$', value):
                valid2+=1
        print(valid2)
    if valid2 == 7:
        validTrue += 1
    valid2 = 0
        

print(validTrue)



