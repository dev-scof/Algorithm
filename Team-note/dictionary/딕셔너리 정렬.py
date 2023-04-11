# value로 정렬하기
student={'song':2, 'park':1, 'sa':6, 'kim':4}
print(sorted(student.items(), key=lambda x:x[1]))

# key로 정렬하기
Student={3:'song', 1:'lee', 2:'seo', 4:'kim'}
print(sorted(Student.items(), key=lambda x:x[0]))

# 정렬기준이 여러개인 경우
# 첫번째 정렬 옵션, 두번째 정렬 옵션
testTuple = [(1,2),(2,4),(3,4),(1,4),(1,1),(2,0)]
print(sorted(testTuple, key=lambda x:(x[0], x[1])))

# 키와 값을 바꾸기
temp_Student={"song":123, "park":111, "kim":555, "lee":222, "fff":142}
print({v : k for k, v in temp_Student.items()})

