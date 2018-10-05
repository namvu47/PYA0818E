# count digit and letter in an input

_input = str(input('Nhap vao 1 cau bat ky: \n'))
countDigit = 0
countLetter = 0

for i in range (0, len(_input)):
    if  _input[i].isdigit():
        countDigit += 1
    elif _input[i].isalpha():
        countLetter += 1
    else:
        pass

print(f'Number of Digit: {countDigit}')
print(f'Number of Letter: {countLetter}')
