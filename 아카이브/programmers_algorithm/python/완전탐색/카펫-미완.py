def solution(brown, yellow):
    answer = []
    height =3
    while True:
        width = (yellow/(height-2))+2
        if width == int(width):
            width = int(width)
            if (height+width-2)*2 == brown:
                if height<width:
                    height,width = width,height
                return [height,width]
        height+=1
print(solution(24,24))
