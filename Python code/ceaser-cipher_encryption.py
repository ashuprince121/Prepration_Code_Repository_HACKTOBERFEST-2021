# This is the implementation of Ceaser Cipher Encryption Algorithm in Cryptography
# Input any plaintext and a shify key value which should be the integer
# Output will be a ciphertext generated according to the algorithm

import sys

k = int(input("Enter the value of k(shift): "))
print("Note - Press double enter after entering the input")
print("Enter plaintext: ")

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

output = ""  #to store encrypted text
j = 0

# only considered letters
# discareded all other characters
for line in text:
    for i in line:
        if(i.isupper()):
            output += chr((ord(i) + k - 65) % 26 + 65)
            j = j+1
            if(j > 0 and j % 5 == 0):
                output += " "
        if(i.islower()):
            output += chr((ord(i) + k - 97) % 26 + 97)
            j = j+1
            if(j > 0 and j % 5 == 0):
                output += " "
        if(j == 50):
            output += "\n"
            j = 0


print("Encrypted string is :\n", output)
