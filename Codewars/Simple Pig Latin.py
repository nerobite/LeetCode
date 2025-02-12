"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""
data = "Quis custodiet ipsos custodes ?"
def pig_it(text):
    text = text.split()
    res = []
    for i in text:
        i = list(i)
        if i[0] not in ['.', '!', '?']:
            first = i.pop(0)
            i.append(first)
            i.append('ay')
            res.append(''.join(i))
        else:
            res.append(i[0])
    return ' '.join(res)

test = pig_it(data)
print(test)