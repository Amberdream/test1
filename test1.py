# _*_ coding:utf-8_*_

# 这个程序用来测试列表中每个元素的个数，用字典保存

# 创建一个列表，元素有重复项
list = [1,2,3,4,5,5,5,2,26,6,3,7,8,7,9]

# 利用集合删除重复的元素
b = set(list)

print(b)

# 计算 list 中每个元素的个数

dict = {}

for i in b:
    num = list.count(i)

    dict[i] = num

print(dict)

# 计算字符串中每个元素的个数

str = 'hello_world'

# 先把字符串转换成列表

length = len(str)

list = []

for i in range(length):
    list.append(str[i])

# 去除重复的元素
l = set(list)
print(l)

dict1 = {}

for item in l:
    num = list.count(item)

    dict1[item] = num

print(dict1)

name = 'liu'
gender = 'male'

print(name + gender)









