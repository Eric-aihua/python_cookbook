# -*- coding:utf-8 -*-
# @Author：sunaihua 
# 问题一：
# 将u
# '\u810f\u4e71'
# 转换为
# '\u810f\u4e71'

# 方法：
s_unicode = u'\u810f\u4e71'
s_str = s_unicode.encode('unicode-escape').decode('string_escape')
s_str = s_unicode.encode('utf-8')
print s_str
#
# 问题二：
# 将
# '\u810f\u4e71'
# 转换为u
# '\u810f\u4e71'
# 方法：
s_str = '\u810f\u4e71'
s_unicode = s_str.decode('unicode-escape')
# s_unicode = s_str.encode()
print s_unicode