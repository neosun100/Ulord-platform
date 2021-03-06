# -*- coding: utf-8 -*-
# @Date    : 2018/4/11
# @Author  : Shu
# @Email   : httpservlet@yeah.net

from ulord.extensions import ma
from ulord.models import Content, Consume, Tag

_all__ = ['content_schema', 'contents_schema']


class TagSchema(ma.ModelSchema):
    class Meta:
        fields = ('name',)


class ContentSchema(ma.ModelSchema):
    class Meta:
        # model = Content
        fields = (
            'id', 'claim_id', 'author', 'title', 'price', 'content_type', 'currency', 'des', 'status', 'create_timed',
            'update_timed', 'views', 'tags', 'create_timed_timestamp', 'update_timed_timestamp')
        # exclude=('txid','enabled','consumes','udfs_hash','appkey')
    # 参考 http://marshmallow.readthedocs.io/en/latest/nesting.html?highlight=Nested
    # 如果是使用model,就不需要nested了, 内部实现应该做了处理
    tags = ma.Nested(TagSchema, many=True, only='name')

content_schema = ContentSchema()
contents_schema = ContentSchema(many=True)


