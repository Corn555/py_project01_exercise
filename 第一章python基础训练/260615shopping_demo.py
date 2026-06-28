# 案例：购物车管理系统开发需求
# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。
# 具体功能要求：
# 1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车：要求用户输入要删除的购物车商品名称，根据名称删除购物车中的商品。
# 4.查询购物车：将购物车中的商品信息展示出来，格式为：商品名称：xxx，商品价格：xxx，商品数量：xxx。
# 5.退出购物车：结束程序运行。

# 初始化购物车
shopping_cart = {}

while True:
    print("欢迎使用购物车管理系统！！！")
    demo = """#########################
           1.添加购物车：
           2.修改购物车：
           3.删除购物车：
           4.查询购物车：
           5.退出购物车：
    #########################
    """
    print(demo)

    choice = (input("请输入1-5："))

    match choice:
        case '1':
            name = input("请输入商品名称： ")
            price = float(input("请输入商品价格： "))  # 转为浮点数
            amount = int(input("请输入商品数量： "))
            shopping_cart[name] = {"price": price, "amount": amount}
            print(f"商品{name}已添加")

        case '2':
            name = input("请输入要修改的商品名称: ")
            if name in shopping_cart:
                price = float(input("请输入修改商品价格： "))  # 转为浮点数
                amount = int(input("请输入修改商品数量： "))
                shopping_cart[name] = {"price": price, "amount": amount}
                print("商品修改成功！")
            else:
                print("商品不存在！！！")

        case '3':
            name = input("请输入要删除的商品名称: ")
            if name not in shopping_cart:
                print("商品不存在！！！")
            else:
                del shopping_cart[name]
                print("商品删除完成！！！")

        case '4':
            if not shopping_cart:
                print("没有添加商品！！！")
            else:
                for name in shopping_cart.keys():
                    goods_info = shopping_cart[name]
                    print(f"商品名称：{name}，商品价格：{goods_info['price']}，商品数量：{goods_info['amount']}")

        case '5':
            print("退出系统！")
            break

        case _:
            print("输入无效，请输入1-5的数字！")



