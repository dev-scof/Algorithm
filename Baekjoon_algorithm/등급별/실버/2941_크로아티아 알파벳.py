alpabet=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
text = input()
answer=0
for alpa in alpabet:
    if alpa in text:
        answer += text.count(alpa)
        text = text.replace(alpa, ',')
print(answer+len(text)-text.count(','))