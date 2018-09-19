#coding:utf-8
import sys, string, os, re, codecs   

path="/Users/fanjinlong/dev/ios/caipiao/Lottery/Lottery/" #路径  
prefix = "FF_SSECP" #前缀 
old_prefix = "CP"

dirname = "" 

def fileRename(filename, child, sufix):
    # 文件重命名
    fr = filename.find(old_prefix)
    if fr >= 0:
      filename = filename.replace(old_prefix,prefix)
      # print(filename)
      newfile = path+"/" + filename+sufix
      print(child)
      print(newfile)
      os.rename(child,newfile)
      
def textContentRename(path, child, sufix):
 
    #判断后缀名  
    # if (sufix == ".m" or sufix == ".h"):
    if (sufix == ".xib"):
        # 文本替换
        f = codecs.open(child, 'r', encoding='utf-8')
        w_str = ""
        for line in f:
            # print(line.decode('utf-8'))
            if re.search(old_prefix,line):
                line = re.sub(old_prefix,prefix,line)
                w_str += line
            else:
                w_str += line
        # print(w_str)
        wopen = codecs.open(child, 'w', encoding='utf-8')
        wopen.write(w_str)
        f.close()
        wopen.close()

        print(child)

def RenameFiles(path,prefix):  
    global dirname  
    #获取目录下所有文件，包括文件夹  
    parents = os.listdir(path)  
    for parent in parents:  
        #拼接一个当前文件的路径  
        child = os.path.join(path,parent)  
        #print(child)  
        if os.path.isdir(child):#判断是否为文件夹 是文件夹 递归调用函数  
            dirname = parent  
            RenameFiles(child,prefix)  
            #print(child)  
        else:#不是文件夹 递归调用函数  
            #获取文件名称 例 "aaa.png"  filename = aaa  
            filename = os.path.splitext(parent)[0]#parent.split('.')[0][-1]  
            # 获取文件后缀名 例 "aaa.png"  sufix =.png  
            sufix = os.path.splitext(child)[1]  
            # #判断后缀名  
            # if (sufix == ".m" or sufix == ".h"):
            # 	# 文本替换
            # 	f = codecs.open(child, 'r', encoding='utf-8')
            # 	w_str = ""
            # 	for line in f:
            # 		# print(line.decode('utf-8'))
            # 		if re.search(old_prefix,line):
            # 			line = re.sub(old_prefix,prefix,line)
            # 			w_str += line
            # 		else:
            # 			w_str += line
            # 	# print(w_str)
            # 	wopen = codecs.open(child, 'w', encoding='utf-8')
            # 	wopen.write(w_str)
            # 	f.close()
            # 	wopen.close()

            print('child',child)
            print("path",path)
            print("\n")
            textContentRename(path,child, sufix)
            # fileRename(filename, child,sufix)

	            # 文件重命名
            	# fr = filename.find('SYJ')
            	# if fr >= 0:
            	# 	filename = filename.replace('SYJ','FF')
            	# 	# print(filename)
            	# 	newfile = path+"/" + filename+sufix
            	# 	print(child)
            	# 	print(newfile)
            	# 	os.rename(child,newfile)

    
RenameFiles(path,prefix)  