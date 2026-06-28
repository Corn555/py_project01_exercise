# #设计一个计算三角形面积函数
# def triangle_square(length, high):
#     square = length * length / 2
#     return square
#
# print(triangle_square(4,4))
#



# #设计一个字符串传出元音字母的个数
# def str_aeiou():
#     num = 0
#     str_aeiou1 = input("请输入一串:")
#     for i in str_aeiou1:
#         if i in 'aeiou' or i in 'AEIOU':
#             num += 1
#     return num
#
# print(str_aeiou())




# 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# 分数 >= 90：A
# 分数 >= 75：B
# 分数 >= 60：C
# 分数 < 60：D
def cal_grade(score_list):
    res = []

    for score in score_list:
        if  90 <= score <= 100:
             res.append('A')
        elif 75 <= score < 90:
             res.append('B')
        elif 60 <= score < 75:
             res.append('C')
        elif 0<= score < 60:
             res.append('D')
        else:
             res.append("NULL")

    return res


s_list = [3,74,78,98,99,120,-1]
print(cal_grade(s_list))


# 练习 2定义一个函数，用于判断一个字符串是否是回文串，返回 bool 值。
# 把字符串反转，如果和原字符串相同，就是回文串。（如："level"，"radar"，"黄山落叶松叶落山黄"）
# def is_palindrome(str1):
#     # 1. 反转字符串
#     new_str = ""
#     # 倒序遍历字符
#     for char in str1[::-1]:
#         new_str += char
#     # 2. 判断是否相等
#     if str1 == new_str:
#         return True
#     else:
#         return False
#
# # 调用测试
# print(is_palindrome("radar"))
# print(is_palindrome("python"))



# 定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。练习
# 参数total_sec：外部传入总秒数
def trans_time(total_sec):
    hours = total_sec // 3600

    remain_s = total_sec % 3600

    minutes = remain_s // 60

    seconds = remain_s % 60

    return f"{hours}h {minutes}min {seconds}s"

# 调用时传数字
print(trans_time(99000))


#定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
def triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        if a == b == c:
            return "这是个等边三角形"
        elif a == b or b == c or a == c:
            return  "这是个等腰三角形"
        else:
            return  "一个普通的三角形"
    else:
        return "无法组成三角形！！！"

print(triangle(3,9,4))









