# -*- coding:utf-8 -*-

from pymongo import *


try:
    # 构造json对象
    # doc = {'name': '孙悟空', 'home': '花果山'}
    doc1 = {'name': '猪八戒', 'home': '高老庄'}
    doc2 = {'name': '唐僧', 'home': '长安'}
    doc = [doc1, doc2]

    # 使用init方法创建连接对象-MongoClient对象
    client = MongoClient('localhost', port=27017)

    # 通过client对象获取数据库对象-Database对象
    db = client.tt1

    # 通过db对象获取集合对象-Collections对象
    collections = db.stu

    # 插入单条文档对象
    # db.stu.insert_one(doc)
    # 插入多条文档对象
    # db.stu.insert_many(doc)
    # print 'insert done'

    # 查询单条文档对象
    # result = db.stu.find_one()
    # print '%s--%s' % (result['name'], result['home'])
    # 查询多条文档对象
    # cursor = db.stu.find()
    # for result in cursor:
    #     print '%s--%s' % (result['name'], result['home'])

    # 修改单条文档对象
    # db.stu.update_one({'name': '猪八戒'}, {'$set': {'gender': True}})
    # 修改多条文档对象
    # db.stu.update_many({'gender': True}, {'$set': {'age': 500}})
    # print 'update done'

    # 删除单条文档对象
    # db.stu.delete_one({'name': '唐僧'})
    # 删除多条文档对象
    # db.stu.delete_many({'gender': True})
    # print 'delete done'
except Exception as e:
    print e


try:
    client = MongoClient('localhost', 27017)
    db = client.tt1

    # 批量插入数据
    # for i in range(1000):
    #     db.stu.insert_one({'_id': i, 'name': 'py%s' % i})
    # print 'insert done'

    # 批量查询数据
    # cursor = db.stu.find({'$where': 'function(){return this._id % 100 == 0}'}, {'_id': 0, 'name': 1})
    # for result in cursor:
    #     print result['name']
except Exception as e:
    print e
