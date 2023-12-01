fi = open('input', 'r')

total = 0

for line in fi:
    first_number = -1
    second_number = -1
    
    for char in line:
        if char.isdigit():
            if first_number == -1:
                first_number = int(char)
                second_number = int(char)
            else:
                second_number = int(char)
            
    if first_number == -1 and second_number == -1:
        first_number = 0
        second_number = 0
        print('no numbers found for ' + line)
    
    total += (first_number * 10) + second_number

print(total)
