fi = open('input', 'r')

total = 0

number_constants = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' , '1', '2', '3', '4', '5', '6', '7', '8', '9']
number_constants_toint = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }

for line in fi:
    ltor_min = len(line)
    ltor_value = ''
    rtol_max = -1
    rtol_value = ''

    for number_constant in number_constants:
        position_ltor = line.find(number_constant)
        if position_ltor != -1 and position_ltor < ltor_min:
            ltor_min = position_ltor
            ltor_value = number_constants_toint[number_constant]
        
        position_rtol = line.rfind(number_constant)
        if position_rtol != -1 and position_rtol > rtol_max:
            rtol_max = position_rtol
            rtol_value = number_constants_toint[number_constant]
    
    total += (ltor_value * 10) + rtol_value

print(total)
