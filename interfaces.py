#!/usr/bin/env python3

from wazo_confd_client import Client as Confd
from wazo_auth_client import Client as Auth
from xivo import agi

agi = agi.AGI()

username=""
password=""

a = Auth('localhost', username=username, password=password, verify_certificate=False)
t = a.token.new('wazo_user', expiration=3600)
token = t['token']

c = Confd('localhost', token=token, verify_certificate=False)

def find_interface_by_extension(extension, context):
    ext_id = c.extensions.list(search=extension, context=context)['items'][0]['id']
    return c.extensions.get(ext_id)['lines']

def get_interface(extension, context):
    interfaces = []
    lines = find_interface_by_extension(extension, context)
    for line in lines:
        interfaces.append("{}".format(line['name']))
    return interfaces

extension = agi.get_variable("WAZO_EXTEN")
context = agi.get_variable("WAZO_CONTEXT")

interfaces = get_interface(extension, context)

if interfaces:
    agi.set_variable("WAZO_INTERFACES", '&'.join(interfaces))
