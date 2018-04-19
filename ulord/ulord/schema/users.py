# -*- coding: utf-8 -*-
# @Date    : 2018/4/11
# @Author  : Shu
# @Email   : httpservlet@yeah.net

from ulord.extensions import ma
from ulord.models import Application,Role,Type

_all__=['app_schema','apps_schema','role_schema','roles_schema','type_schema', 'types_schema']

class AppSchema(ma.ModelSchema):
    class Meta:
        # fields=('id','name','des')
        model=Application
        exclude=('user_id','user')

app_schema=AppSchema()
apps_schema=AppSchema(many=True)


class RoleSchema(ma.ModelSchema):
    class Meta:
        # fields=('id','name','des')
        model=Role
        exclude=('user',)

role_schema=RoleSchema()
roles_schema=RoleSchema(many=True)



class TypeSchema(ma.ModelSchema):
    class Meta:
        fields=('id','parent_id','name','des')
        # model = Type
        # exclude = ('app',)


type_schema = TypeSchema()
types_schema = TypeSchema(many=True)