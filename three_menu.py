#-*- coding:utf-8 -*-
#/usr/bin/env python
#定义一级、二级、三级菜单
One_menu = ['BJ','HN']
Two_menu = {'BJ':['CY','HD','FT'],'HN':['SQ','ZZ','LY']}
Tree_menu = {
    'CY':['CY_01','CY_02','CY_03'],
    'HD':['HD_01','HD_02','HD_03'],
    'FT':['FT_01','FT_02','FT_03'],
    'SQ':['SQ_01','SQ_02','SQ_03'],
    'ZZ':['ZZ_01','ZZ_02','ZZ_03'],
    'LY':['LY_01','LY_02','LY_03']
}
#取出字典中的列表通过字典和key
def menu_list(dic_name,kyes):
    name_list = dic_name[kyes]
    return name_list

try:
    #+++++++++++输出一级菜单+++++++++++ 
    for i in One_menu:
		#利用列表下标位当做当前菜单的选择值
        print '%d.%s'%(One_menu.index(i)+1,i)

    #+++++++++++输出二级菜单+++++++++++
	
    menu_two = int(raw_input('please input your two menu number:'))
	#定义选择范围
    number_list = range(len(One_menu)+1)
    if menu_two in number_list[1:]:
        two_list = menu_list(Two_menu,One_menu[menu_two-1])
        for i in two_list:
			#利用列表下标位当做当前菜单的选择值
            print '%d.%s'%(two_list.index(i)+1,i)
    else:
        print 'two number not found'
        exit()
    
    #+++++++++++输出三级菜单+++++++++++
    menu_three = int(raw_input('please input your three menu number:'))
	#讲二级菜单字典的key赋值到一个变量
    three_list = menu_list(Tree_menu,two_list[menu_three-1])
	#定义选择范围
    number_list = range(len(three_list)+1)
    if menu_three in number_list[1:]:
        for i in three_list:
			#利用列表下标位当做当前菜单的选择值
            print '%d.%s'%(three_list.index(i)+1,i)
    else:
        print 'three number not found'
        exit()
except ValueError:
    print 'please input int type'
