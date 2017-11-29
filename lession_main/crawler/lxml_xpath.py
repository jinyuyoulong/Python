#coding: utf-8

# 路径表达式	结果
# bookstore	选取 bookstore 元素的所有子节点。
# /bookstore	选取根元素 bookstore。注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！
# bookstore/book	选取属于 bookstore 的子元素的所有 book 元素。
# //book	选取所有 book 子元素，而不管它们在文档中的位置。
# bookstore//book	选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
# //@lang	选取名为 lang 的所有属性。

# 谓语（Predicates）

# 谓语用来查找某个特定的节点或者包含某个指定的值的节点。

# 谓语被嵌在方括号中
# 路径表达式	结果
# /bookstore/book[1]	选取属于 bookstore 子元素的第一个 book 元素。
# /bookstore/book[last()]	选取属于 bookstore 子元素的最后一个 book 元素。
# /bookstore/book[last()-1]	选取属于 bookstore 子元素的倒数第二个 book 元素。
# /bookstore/book[position()<3]	选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
# //title[@lang]	选取所有拥有名为 lang 的属性的 title 元素。
# //title[@lang=’eng’]	选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
# /bookstore/book[price>35.00]	选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。
# /bookstore/book[price>35.00]/title	选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。

# 通配符 
# *
# @*
# node()

# XPath 运算符 : | + - * div = != < <= > >= or and mod

from lxml import etree

html = etree.parse('hello.html')
# （2）获取 <li> 标签的所有 class
# result = html.xpath('//li/@class')
# （3）获取 <li> 标签下 href 为 link1.html 的 <a> 标签
# result = html.xpath('//li/a[@href="link1.html"]')
# （4）获取 <li> 标签下的所有 <span> 标签
# 因为 / 是用来获取子元素的，而 <span> 并不是 <li> 的子元素，所以，要用双斜杠
# result = html.xpath('//li//span')
# （5）获取 <li> 标签下的所有 class，不包括 <li>
# result = html.xpath('//li/a//@class')
# （6）获取最后一个 <li> 的 <a> 的 href
# result = html.xpath('//li[last()]/a/@href')
# （7）获取倒数第二个元素的内容
# result = html.xpath('//li[last()-1]/a')
# print result[0].text
# （8）获取 class 为 bold 的标签名
result = html.xpath('//*[@class="bold"]')
print result[0].tag
