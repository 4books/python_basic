import sys

string = "Life is too short, you need Python"

print(string[0])
print(string[5])
# 뒤에서 부터 문자 뽑을때
print(string[-3])

# 자르기
print(string[5:])
print(string[5:15])
print(string[5:-7])

# 문자열 찾기 및 카운트
print(string.find("Python"))
print(string.count("o"))

# join
a = ","
print(a.join("abcd"))

# list
l = [1, 2, 3]
print(str(l[0]) + 'D')

# dictionary (== Hash)
some_dic = {1: 'a', 2: 'b', 3: 'c'}
print(some_dic.keys())

for key in some_dic.keys():
    print(key)

print(some_dic.values())
print(some_dic.items())
print(some_dic.get(2))
# key 가 없으므로 none
print(some_dic.get(0))
some_dic.clear()
# key 가 없으므로 none
print(some_dic.get(1))

# set 집합
s1 = set("World")
print(s1)

s2 = set("Hello")
print(s2)

# 교집합
print(s1 & s2)
print(s1.intersection(s2))
# 합집합
print(s1 | s2)
print(s1.union(s2))
# 차집합
print(s1 - s2)  # d r W

s3 = {3, 2, 1, 6, 4, 5, 1, 1, 1}
print(s3)
l3 = list(s3)
print(l3)
l3.sort(reverse=True)  # 내림차순 소팅
print(l3)
l3.reverse()  # 뒤집는 것임
print(l3)

# 자동으로 같은 객체를 가르킴
a = 'hng'
b = 'hng'
print(a)
print(a is b)
print(a is not b)

print(sys.getrefcount('hng'))
c = 'hng'
print(sys.getrefcount('hng'))

del (a)
# print(a) #NameError: name 'a' is not defined

a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

if __name__ == '__main__':
    print('start')
