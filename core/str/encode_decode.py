# -*- coding: utf-8 -*-
__author__ = 'eric.sun'

import logging as logger_iTToparse




# print '绿盟科技'.decode("utf-8")
# print u'绿盟科技'.encode("utf-8")
print "\xe5\xad\x99\xe7\x88\xb1\xe5\x8d\x8e".decode("utf-8")
# print "\\xe5\\xae\\x89\\xe5\\x85\\xa8\\xe5\\x8d\\xab\\xe5\\xa3\\xab\\xe5\\x9c\\xa8\\xe7\\xba\\xbf\\xe5\\xae\\x89\\xe8\\xa3\\x85\\xe7\\xa8\\x8b\\xe5\\xba\\x8f".encode("utf-8")
# print "\xe6\x96\x87\xe4\xbb\xb6\xe6\xaf\x94\xe5\xad\x98\xe5\x9c\xa8".decode("utf-8").encode("utf-8")
# s1="360\xe5\xae\x89\xe5\x85\xa8\xe5\x8d\xab\xe5\xa3\xab\xe5\x9c\xa8\xe7\xba\xbf\xe5\xae\x89\xe8\xa3\x85\xe7\xa8\x8b\xe5\xba\x8f"
# print len(s1)
# print s1.decode("utf-8")
# print "\xe7\xbb\xbf\xe7\x9b\x9f\xe7\xa7\x91\xe6\x8a\x80".encode("utf-8").decode("utf-8")
# print u'/opt/disk/\u7eff\u76df\u79d1\u6280'.encode("utf-8")
# print u'\u7eff\u76df\u79d1\u6280'.decode("utf-8").encode("utf-8")


s = r"\\xe5\\xae\\x89\\xe5\\x85\\xa8\\xe5\\x8d\\xab\\xe5\\xa3\\xab\\xe5\\x9c\\xa8\\xe7\\xba\\xbf\\xe5\\xae\\x89\\xe8\\xa3\\x85\\xe7\\xa8\\x8b\\xe5\\xba\\x8f"
n='孙爱护'
s2=s.replace('\\\\',"\\")
print bytes(n)
# print s2.decode('utf-8')
# print str(s2, encoding = "utf-8")
# print unicode(s)
print s2.decode("utf-8").encode()
# print s.replace('\\',"\\").decode('utf-8')
# print type(s)
# print type(str(s))
# print str(repr(s).replace('\\\\',"\\")).decode('utf-8')
# print s.decode('utf-8')








