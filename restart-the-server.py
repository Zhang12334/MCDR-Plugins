from typing import TYPE_CHECKING
from mcdreforged.api.command import Literal
import json
import os


PLUGIN_METADATA = {
    'id': 'restart_the_server',
    'version': '1.0.0',
    'name': 'By Zhang1233'
}

if TYPE_CHECKING:
    from mcdreforged.api.types import PluginServerInterface, PlayerCommandSource
     
     
def re(source: 'CommandSource', server: 'ServerInterface'):
    if source.is_player and source.get_permission_level() >= 3:
        source.get_server().execute('say 正在重启服务器..')
        source.get_server().execute('save-all')        
        source.get_server().restart()  
    else:
        source.get_server().execute('msg ' + source.player+' 你说得对，但你并没有权限')
        source.get_server().execute('say ' + source.player+'，权限不足还想搞事情，被我逮到了吧.gif')              
               
def on_load(server: 'PluginServerInterface', old):
    server.register_help_message('!!restart', '重启服务器')
    server.register_command(
        Literal('!!restart').runs(re)
    )
    server.register_command(
        Literal('!!RESTART').runs(re)
    )
    #权限须大于等于3