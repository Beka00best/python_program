#made by Bukhatov Bekzat in python 3.7.8
#Please use python 3
#Hamming code for 8 bits and check one error for 12 bits
import re
def decimalToBinary(n):

    return bin(n).replace("0b","")

def find2DegreesCode(m):  
    for i in range(m): 
        if(2**i >= m + i + 1): 
            return i 
  
  
def advancedArray(array, r): 
    j = 0
    k = 0
    m = len(array) 
    res = '' 
    for i in range(1, m + r + 1): 
        if(i == 2**j): 
            res = res + '0'
            j += 1
        else: 
            res = res + array[k] 
            k += 1 
    return res


def encodeHamming(byte_hamming):
    byte_hamming[0] = int(byte_hamming[2]) ^ int(byte_hamming[4]) ^ int(byte_hamming[6])  ^ int(byte_hamming[8]) ^ int(byte_hamming[10])
    byte_hamming[1] = int(byte_hamming[2]) ^ int(byte_hamming[5]) ^ int(byte_hamming[6])  ^ int(byte_hamming[9]) ^ int(byte_hamming[10])
    byte_hamming[3] = int(byte_hamming[4]) ^ int(byte_hamming[5]) ^ int(byte_hamming[6])  ^ int(byte_hamming[11])
    byte_hamming[7] = int(byte_hamming[8]) ^ int(byte_hamming[9]) ^ int(byte_hamming[10]) ^ int(byte_hamming[11])
    return "".join(map(str,byte_hamming))

def errorFindHamming(y):
    error = [0] * 4
    error[0] = int(y[0]) ^ int(y[2]) ^ int(y[4]) ^ int(y[6]) ^ int(y[8]) ^ int(y[10])
    error[1] = int(y[1]) ^ int(y[2]) ^ int(y[5]) ^ int(y[6]) ^ int(y[9]) ^ int(y[10])
    error[2] = int(y[3]) ^ int(y[4]) ^ int(y[5]) ^ int(y[6]) ^ int(y[11]) 
    error[3] = int(y[7]) ^ int(y[8]) ^ int(y[9]) ^ int(y[10]) ^ int(y[11]) 

    if sum(error) == 0:
        return 0
    else:
        error = ''.join(map(str,reversed(error)))
        return int(error, 2)

def Check(array):
    if re.match('^[0-1]*$', array):
        pass
    else:
        print("Please, try again and enter bits")
        exit(0)

def exchange(array, c):
    n = len(array)
    c = c - 1
    if array[c] == 1:
        array = array[:c] + '0' + array[c + 1:]
        return array
    else:
        array = array[:c] + '1' + array[c + 1:]
        return array

print("Interpreter with python3")
data = input('Enter 8 bits ')     
m = len(data)
if m != 8:
    print('You did not enter 8 bits, Try again')
    exit(0)
Check(data)
r = find2DegreesCode(m) 
arr = advancedArray(data, r)
arr = list(arr)
array = encodeHamming(arr)
print("Given data " + data)
print("Code Hamming " + array)
error = input("Hamming code with one mistake 12 bits ")
m = len(error)
if m != 12:
    print('You did not enter 12 bits, Try again')
    exit(0)
Check(error)
error = list(error)
err = errorFindHamming(error)
if int(err) < 9:
    print("Error line code " + str(err))
    array = exchange(array, err) 
    print("Fixed code " + array)
else:
    print("Incorrectly entered a string, Try again ")
    print(str(err))

