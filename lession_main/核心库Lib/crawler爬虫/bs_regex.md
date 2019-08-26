find_all匹配的返回的结果是一个列表。
提取匹配结果后，使用text属性，提取文本内容，滤除br标签。
随后使用replace方法，剔除空格，替换为回车进行分段。&nbsp;在html中是用来表示空格的。replace('\xa0'*8,'\n\n')就是去掉八个空格符号，并用回车代替.
print(texts[0].text.replace('\xa0'*8,'\n\n'))

