from typing import TYPE_CHECKING
from mcdreforged.api.command import Literal
import json
import os

if TYPE_CHECKING:
    from mcdreforged.api.types import PluginServerInterface, PlayerCommandSource
     
     
def start_fly(source: 'CommandSource'):
    if source.is_player and source.get_permission_level() >= 2:
        source.get_server().execute('fly ' + source.player+' true')
        source.get_server().execute('say ' + source.player+'开启了飞行')
    else:
        source.get_server().execute('msg ' + source.player+' 你说得对，但你并没有权限')
        source.get_server().execute('say ' + source.player+'权限不足')              
        

def stop_fly(source: 'CommandSource'):
    if source.is_player and source.get_permission_level() >= 2:
        source.get_server().execute('fly ' + source.player+' false')
        source.get_server().execute('say ' + source.player+'关闭了飞行')
    else:
        source.get_server().execute('msg ' + source.player+' 你说得对，但你并没有权限')
        source.get_server().execute('say ' + source.player+'权限不足')        
        
               
def on_load(server: 'PluginServerInterface', old):
    server.register_help_message('!!fly', '飞行')
    server.register_command(
        Literal('!!fly').runs(start_fly)
    )
    server.register_help_message('!!unfly', '关闭飞行')
    server.register_command(
        Literal('!!unfly').runs(stop_fly)
    )
    #需要把可飞行玩家的权限设置为helper