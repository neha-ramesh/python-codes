'''Encryption is a security technique where the text message is converted into unreadable form called as Cipher text.

Generate a cipher text using polygraphic substitution method based on linear algebra. Each letter is represented by a number modulo 26.

To encrypt a message, each block of n letters (considered as an n-component vector) is multiplied by an invertible n × n matrix, against modulus 26.

The matrix used for encryption is the cipher key, and it should be chosen randomly from the set of invertible n × n matrices (modulo 26).

Generate a cipher text for a text message of 3 letter alphabet. Hence the key should be 3*3 matrix.

Check whether given key satisfies 9 characters in it. If not, popup the message for entering 9 letter key.

Example:

Encryption:

We have to encrypt the message ‘ACT’.The key is ‘GYBNQKURP’ which 9 in characters hence can be written as the 3x3 matrix:

Corresponding output is “POH”

Input Format

Text message: ACT

Key: GYBNQKURP

Output Format

Cipher text: POH'''

txt=input()
key=input()

l=[]

for i in range(len(txt)):
    m=[]
    m.append(ord(txt[i])-65)
    l.append(m)

n=[]
for i in range(len(key)):
    if i in (2,5,8):
        k=[]
        k.append(ord(key[i-2])-65)
        k.append(ord(key[i-1])-65)
        k.append(ord(key[i])-65)
        n.append(k)

result = [[sum(a * b for a, b in zip(n_row, l_col))
                        for l_col in zip(*l)]
                                for n_row in n]

e=result[0][0]%26
f=result[1][0]%26
g=result[2][0]%26
print(chr(e+65),end="")
print(chr(f+65),end="")
print(chr(g+65))
