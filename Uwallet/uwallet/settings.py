# -*- coding: utf-8 -*-
# @Date    : 18-4-16 下午8:07
# @Author  : hetao
# @Email   : 18570367466@163.com


# 正在使用的环境 0: 开发环境, 1: 测试环境, 2: 生产环境
ENVIRONMENT = 0

# ===========================================================
# 本地调试
# ===========================================================
# mongodb
DATABASE_HOST = '192.168.14.147'
# redis
REDIS_HOST = '192.168.14.240'


# ===========================================================
# 通用配置
# ===========================================================

# mongodb
DATABASE_ENGINE = 'mongodb'  # 留着备用
DATABASE_PORT = 27017

# redis
REDIS_NAME = 2
REDIS_NAME_PRO = 1
REDIS_PORT = 6379

# 钱包的字段名称
WALLET_FIELDS = ('seed', 'transactions', 'txi', 'txo', 'pruned_txo', 'claimtrie_transactions', )

