stack=[]
wo=''
for word in input():
    if word=='<':
        stack.append('<')
    elif word=='>':
        stack.append('>')
        rv_words=[]
        for spl in wo.split():
            rv_words.append(''.join(reversed(spl)))
        print(' '.join(rv_words), end='')

        print(''.join(stack), end='')
        stack=[]
        wo=''
    elif stack!=[]:
        stack.append(word)
    elif stack==[]:
        wo+=word
rv_words=[]
for spl in wo.split():
    rv_words.append(''.join(reversed(spl)))
print(' '.join(rv_words), end='')