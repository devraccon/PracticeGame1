
num1 = 1
num2 = 2
if num1 == num2:
    print("num1 과 num2는 같습니다.")
else:
    print("num1 과 num2는 같지 않습니다.")

str1 = "한국어"
str2 = "한국어"
str3 = "영어"

if str1 == str2:
    print("str1과 str2는 같습니다.")
else:
    print("str1과 str2는 같지 않습니다.")

if str1 == str3:
    print("str2 와 str3는 같습니다.")
else:
    print("str2 와 str3는 같지 않습니다.")


list1 = [1,2,3,4,5]
for l in list1:
    print(l)

list2 = range(10)

for l2 in list2:
    print(l2)


num3 = 10
# while 조건문 의 값이 true(참) 일때 까지 반복한다.
while num3 > 0:
    print(num3)
    num3 = num3 - 1
