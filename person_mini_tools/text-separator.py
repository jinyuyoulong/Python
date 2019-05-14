import os

# #封装第一个函数：分割文件中的一个模块
# def save_file(boy,girl,count):
#     file_name_boy='boy_'+str(count)+'.txt'     
#     file_name_girl='girl_'+str(count)+'.txt'
 
#     boy_file=open(file_name_boy,'w')  #创建文件
#     girl_file=open(file_name_girl,'w')
 
#     boy_file.writelines(boy)
#     girl_file.writelines(girl)
 
#     boy_file.close()
#     girl_file.close()
 
# #封装第二个函数：分割文件
# def split_file(file_name):
#     f = open(file_name)
 
#     boy = [] #用于存储临时读取出来的内容
#     girl= []
#     count = 1 #需要读取三次
 
#     for each_line in f:
#             if each_line[:6] !='======':
#              #我们这里进行字符串分割操作
#                 (role,line_spoken) = each_line.split('：',1)#利用冒号分割为两部分
#                 if role=='小甲鱼':
#                     boy.append(line_spoken)
#                 if role=='小客服':
#                     girl.append(line_spoken)
                    
#             else:
#             #文件的分别保存操作
#                 save_file(boy,girl,count)
#                 boy = []
#                 girl = []
#                 count += 1
    
#     #第三部分没有保存到文件中，因为没有分隔符了
#     save_file(boy,girl,count)
    
#     #关闭文件
#     f.close()
 
 
# #调用函数
# split_file('record.txt')

def separator():
	fp = open('input.txt')
	arr = fp.split('<<<<<<')
	print(arr)
