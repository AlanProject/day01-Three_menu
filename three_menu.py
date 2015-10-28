#/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'root'
#获取输入值
input_data = raw_input('请输入你要查找的城市：')
def menu(input_data):
    #定义一级菜单
    One_menu = ['北京','河南','甘肃']
    #定义二级菜单
    Two_menu = {'北京':'海淀','河南':'商丘','甘肃':'肃州区'}
    #定义三级菜单
    Three_menu = {'海淀':'西二旗','商丘':'宁陵','肃州区':'丰乐'}
    #判断城市是否存在于一级菜单中
    if input_data in One_menu:
        #根据一级菜单列表和二级菜单的key 三级菜单的key和二级菜单的value的对应关系进行数据抽取
        print '''
        %s
            %s
                %s
            '''%(input_data,Two_menu[input_data],Three_menu[Two_menu[input_data]])
if __name__ == '__main__':
    menu(input_data)
