str = 'X-DSPAM-Confidence: 0.8475'

col = str.find(':')
# print(col)
piece = str[col+2:]
# print(piece)
value = float(piece)
print(value)