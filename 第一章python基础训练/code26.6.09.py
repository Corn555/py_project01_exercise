# #字面量的写法
# total = 1000
#
# password = input("请输入密码：")
#
# num = input("请输入取款金额：")
#
# print(f"剩余金额为： {total - int(num) }")


# num1 = input("请输入第一个数字：")
# num2 = input("请输入第二个数字：")
#
# print(f"两个数之和为：{int(num1)+int(num2)}")



# a = int(input("第一个边长："))
# b = int(input("第一个边长："))
# c = int(input("第一个边长："))
#
# if a + b > c and b + c > a and c + a > b:
#     if a == b == c:
#         print("能构成等边三角")
#     elif a == b or b == c or a == c:
#         print("能构成等腰三角")
#     else:
#         print("能构成普通三角")
# else:
#     print("不能构成三角")


# total = 0
# for i in range(1,101):
#     if i % 2 == 1:
#         total += i

# print(total)


# total = 0
#
# for i in range(100,501):
#     if i % 3 == 0:
#         total += i
#
# print(total)


# #99乘法表
# #i表示行，j表示列
# for i in range(1, 10):
#     for j in range(1, 10):
#         if j <= i:
#             print(f"{j} * {i} = {(i * j)}", end='  ')
#     print()




# #1.
# total = 0
# for i in range(1,1001):
#     if i % 5 == 0:
#         total += i
# print(total)
#
#
# #2.akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd
# total_a = 0
# total_k = 0
#
# s = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
#
# for i in s:
#     if i =="a":
#         total_a += 1
#     elif i =="k":
#         total_k += 1
#
# print(f"a: {total_a}, k: {total_k}")






# 定义正确的账号密码
username = ""
password = ""

# # 给用户5次登录机会
# for i in range(5):
#     # 每次循环都让用户重新输入账号密码
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#
#     # 判断是否匹配任意一个账号
#     if username == "admin" and password == "666888":
#         print("correct!!!")
#         break
#     elif username == "zhangsan" and password == "123456":
#         print("correct!!!")
#         break
#     elif username == "taoge" and password == "888666":
#         print("correct!!!")
#         break
#     else:
#         print("incorrect!!!")
#         # 如果不是最后一次机会，提示剩余次数
#         if i < 4:
#             print(f"你还有 {4 - i} 次机会")
#         else:
#             print("错误次数已用完，无法再登录！")







# #生成1-20平方的列表
# sum_list = []
#
# for i in range(1,21):
#     sum_list.append(i*i)
#
# print(sum_list)




# #从一个数字列表提取所有偶数，并计算平方组成一个新的表格
# num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
# new_list = []
#
# for num in num_list:
#     if num % 2 == 0:
#         new_list.append(num*num)
#
# print(new_list)





# # 合并如下三个列表，并对合并后的列表进行元素的去重，然后排好序后输出到控制台
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
#
# sum_list = list1 + list2 + list3
# sum_list2 = []
#
# for item in sum_list:
#     if item not in sum_list2:
#         sum_list2.append(item)
#
# sum_list2.sort()
#
# print(sum_list2)
#
#
#
# # 将如下列表中能被 3 或 5 整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
#          18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# new_list = []
#
# new_list = [i**2 for i in list1 if i % 3 == 0 or i % 5 == 0]
# print(new_list)
#
#
#
#
# # 将如下列表中的正数提取出来，封装为一个新的列表。
# list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
# new_list = [i for i in list1 if i > 0]
# print(new_list)


































