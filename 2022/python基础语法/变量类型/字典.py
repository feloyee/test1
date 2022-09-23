dict = {}
dict['one'] = 22222
dict[3] = "abcd"

print(dict)  # 打印字典内容
print(type(dict))  # 打印变量类型
print(id(dict))  # 打印变量存储的内存地址

print(list(dict))  # 强制转换类型为列表
print(type(list(dict)))
print(dict[3])
# print(dict[0]) # 查询字典内容不存在是会报错
