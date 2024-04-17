def parse_file_name(file_name: str):
    head, number, tail = '', '', ''
    flag = False
    file_name_low = file_name.lower()
    for i in range(len(file_name_low)):
        alpha = file_name_low[i]
        if alpha.isdigit():
            flag = True
            number += alpha
        else:
            if flag:
                tail = file_name_low[i:]
                break
            head += alpha

    return [head, int(number), tail, file_name]

def solution(files):
    parsed_files = [parse_file_name(file) for file in files]
    parsed_files.sort(key=lambda x: (x[0], x[1]))

    return [file[-1] for file in parsed_files]


if __name__ == '__main__':
    print(solution(
        ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    ))
    print(solution(
        ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
    ))
