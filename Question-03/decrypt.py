# Initial loop calculations
total = 0

# Nested loop to calculate total
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i - j

print("Total after loops:", total)

# Counter management with a while loop
counter = 0

# Loop until counter reaches a certain value
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2

print("Final total:", total)
print("Final counter:", counter)

# Encrypted text to decrypt
encrypted_text = """
tybony_inevnoyr = 100 zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhl3'}
qrs cebprff_ahzoref():
tybony tybony_inevnoyr ybpny_inevnoyr = 5
ahzoref= [1, 2, 3, 4, 5]
juvyr ybpny_inevnoyr > >:
vs ybpny_inevnoyr % 2 == 0: ahzoref.erzbir(ybpny_inevnoyr)
ybpny_inevnoyr = 1
erghea ahzoref
zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} erfhyg cebprff_ahzoref (ahzoref=zl_frg)
qrs zbqvsl_qvpg():
ybpny_inevnoyr = 10 zl_qvpg['xrl4'] = ybpny_inevnoyr
zbqvsl_qvpg(5)
qrs hcqngr_tybony():
tybony tybony_inevnoyr
tybony_inevnoyr += 10
sbe v va enatr(5):
cevag(v)
V += 1
vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10: cevag("Pbaqvgvba zrg!")
vs 5 abg va zl_qvpg:
cevag("5 abg sbhaq va gur qvpgvbanel!")
cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""

# Function to decrypt text using Caesar cipher
def decrypt(encrypted_text, key):
    decrypted_text = ""
    
    for char in encrypted_text:
        if char.isalpha():
            # Handle lowercase letters
            if char.islower():
                shifted = ord(char) - key
                if shifted < ord('a'):
                    shifted += 26
            # Handle uppercase letters
            else:
                shifted = ord(char) - key
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Keep non-alphabetical characters unchanged
    
    return decrypted_text

# Decrypt the encrypted text using 'total' as the key
decrypted_text = decrypt(encrypted_text, total)

# Output the decrypted text
print(decrypted_text)


