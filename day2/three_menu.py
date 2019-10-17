# Author:haha
data={
    '四川省':{
        '成都市':{
            '青白江区':['大弯中学','川化中学'],
            '双流区':'双流中学',
        },
        '德阳市':{
            '广汉市':'广汉六中',
            '旌阳区':'旌阳中学'
        }
    },
    '贵州省': {
        '贵阳市': {
            '花溪区': ['花溪品华学校', '贵州民族大学'],
            '乌当区': '贵州师范学院',
        },
        '福泉市': {
            '马场坪街道': '福泉三中',
        }
}}

def three_run(data):
    flag=True
    while flag:
        for i in data:
            print('\t',i)
        choose_key1 = input('请选择1级菜单：')
        if choose_key1 in data:
            while flag:
                for i in data[choose_key1]:
                    print('\t\t',i)
                choose_key2 = input('请选择2级菜单：')
                if choose_key2 in data[choose_key1]:
                    while flag:
                        for i in data[choose_key1][choose_key2]:
                            print('\t\t\t',i)
                        choose_key3 = input('请选择3级菜单：')
                        if choose_key3 in data[choose_key1][choose_key2]:
                            while flag:
                                for i in data[choose_key1][choose_key2][choose_key3]:
                                    print('\t\t\t\t', i)
                                result = input('请选择学校：')
                                if result in data[choose_key1][choose_key2][choose_key3]:
                                    print('已选择：',result)
                                    flag=False
                                elif result == 'q':
                                    print('已退出')
                                    flag = False
                                elif result == 'b':
                                    print('返回上一级')
                                    break
                                else:
                                    print('输入错误，重新输入：')
                                    pass
                        elif choose_key3 == 'q':
                            print('已退出')
                            flag = False
                        elif choose_key3 == 'b':
                            print('返回上一级')
                            break
                        else:
                            print('输入错误，重新输入：')
                            pass
                elif choose_key2 == 'q':
                    print('已退出')
                    flag = False
                elif choose_key2 == 'b':
                    print('返回上一级')
                    break
                else:
                    print('输入错误，重新输入：')
                    pass
        elif choose_key1 == 'q':
            print('已退出')
            flag = False
        else:
            print('输入错误，重新输入：')
            pass



three_run(data)
