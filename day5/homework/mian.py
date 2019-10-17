import re

operator={
    '+':lambda a,b:float(a)+float(b),
    '-': lambda a, b: float(a) - float(b),
    '*': lambda a, b: float(a) * float(b),
    '/': lambda a, b: float(a) / float(b)
}
def run(str_data):
    no_space_strdata=no_space_data(str_data)#去掉空格键
    while True:
        no_space_strdata=make_symbol(no_space_strdata)#去掉数据中+-号重叠的情况
        inner_brackets=re.search('\([^()]*\)',no_space_strdata)#找出最里层括号数据，包含括号
        #如果存在括号，则计算括号里面的数据，没有则直接计算
        if inner_brackets:
            no_bracket=inner_brackets.group().strip('()')
            print('no_brecker:',no_bracket)
            result=figure_brackets(no_bracket)#计算括号里面的数据
            no_space_strdata=no_space_strdata.replace(inner_brackets.group(),str(result))#将计算结果替换包含括号的数据
            print('new_data：',no_space_strdata)
        else:
            print('没有括号了！')
            result=figure_brackets(no_space_strdata)#计算数据
            no_space_strdata=no_space_strdata.replace(no_space_strdata,str(result))#算出最终结果
            print('最后的计算结果：',no_space_strdata)
            break

def make_symbol(data):
    '''
    去掉数据中+-号叠加的情况
    :param data:
    :return:
    '''
    if '--' in data:
        data = data.replace('--', '+')
    elif '+-' in data:
        data = data.replace('+-', '-')
    return data

def figure_brackets(data):
    symbol_list=re.findall('[+-]',data)#列出数据的符号列表
    print('symbol_list:',symbol_list)
    split_data_list=re.split('[+-]',data)#用+-符号打断数据，剩余的都是*/计算
    print('split_data_list:',split_data_list)
    #如果*/数据列表第一个字符为空，说明第一个数字是负数，就将第二个字符变为负数，符号列表和数据列表都将第一个字符删除
    if split_data_list[0]=='':
        split_data_list[1]='-'+split_data_list[1]
        del split_data_list[0]
        del symbol_list[0]
    print('-split_data_list:',split_data_list)
    #消除括号后，存在3*-2之类的情况，将后面一项的数据结合，并消除后面一项及符号
    for index,i in enumerate(split_data_list):
        if i.endswith('*') or i.endswith('/'):
            split_data_list[index]=split_data_list[index]+symbol_list[index]+split_data_list[index+1]
            del split_data_list[index+1]
            del symbol_list[index]

    new_split_data_list=figure_oneoflist(split_data_list)#计算列表中的乘除法
    print('new_split_data_list:',new_split_data_list)
    result=figure_brackets_data(new_split_data_list,symbol_list)#计算括号中的加减法
    return result

def figure_oneoflist(data_list):
    '''
    计算列表中的乘除法
    :param data_list:
    :return:
    '''
    for index,i in enumerate(data_list):
        symbol_list = re.findall('[*/]', i)  # 列出数据的符号列表
        print('*/symbol_list:', symbol_list)
        if len(symbol_list)>0:
            split_data_list = re.split('[*/]', i)
            print('*/split_data_list',split_data_list)
            #依次计算元素中的乘除法
            oneof_result=split_data_list[0]
            for i in range(len(symbol_list)):
                if symbol_list[i]=='*':
                    oneof_result=operator_priority('*',oneof_result,split_data_list[i+1])
                elif symbol_list[i]=='/':
                    oneof_result=operator_priority('/',oneof_result,split_data_list[i+1])
        else:
            oneof_result=data_list[0]
        data_list[index]=oneof_result
    return data_list

def figure_brackets_data(data_list,symbol_list):
    '''
    计算加减法
    :param data_list:
    :param symbol_list:
    :return:
    '''
    if len(symbol_list)>0:
        result=data_list[0]
        for i in range(len(symbol_list)):
            if symbol_list[i]=='+':
                result=operator_priority('+',result,data_list[i+1])
            elif symbol_list[i]=='-':
                result=operator_priority('-',result,data_list[i+1])
    else:
        result=data_list[0]
    return result

def no_space_data(str_data):
    '''
    去掉空格键
    :param str_data:
    :return:
    '''
    data=''
    for i in str_data:
        if i!=' ':
            data += i
        else:
            continue
    return data

def operator_priority(operator_type,data_a,data_b):
    if operator_type in operator:
        result=operator[operator_type](data_a,data_b)
    else:
        print('符号不正确！')
        result=None
    return result

if __name__ == '__main__':
    data = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2)  )'
    run(data)