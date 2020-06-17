# -*- coding:utf-8 -*-

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from hbase import Hbase
from hbase.ttypes import *
# 创建100w测试数据

class HbaseClient():

    def __init__(self):
        self.transport = TSocket.TSocket('localhost', 9090)
        self.transport = TTransport.TBufferedTransport(self.transport)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = Hbase.Client(self.protocol)
        self.transport.open()
        contents = ColumnDescriptor(name='cf:', maxVersions=1)
        # client.deleteTable('test')
        self.table_name = 'performance_test'
        self.client.createTable(self.table_name, [contents])


    def create_test_data(self):
        for i in range(10000000):
            row = 'row-key1'
            mutations = [Mutation(column="cf:a", value="1")]
            self.client.mutateRow(self.table_name, row, mutations)


    # 单线程查询10万次
    def row_key_query_performance(self):
        pass


if __name__ == '__main__':
    hbase_client = HbaseClient()
    hbase_client.create_test_data()
    hbase_client.row_key_query_performance()
