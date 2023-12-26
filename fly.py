from typing import TYPE_CHECKING
from mcdreforged.api.command import Literal
import json
import os
names = locals()
PLUGIN_METADATA = {
    'id': 'fly',
    'version': '1.0.0',
    'name': 'By Zhang1233&stay_miku'
}

if TYPE_CHECKING:
    from mcdreforged.api.types import PluginServerInterface, PlayerCommandSource
             
def check_variable(variable_name):
	if 'variable_name' in locals():
		return 1
	else:
	    return 0 
	  
def on_player_joined(server: 'PluginServerInterface', player: str, info: 'Info'):
     names[str(player)+'_status'] = 0
     
def fly(source: 'CommandSource'):
    if source.is_player and source.get_permission_level() >= 2:#验证通过，开始执行
    #是否存在变量
        if check_variable(str(source.player)+'_status') == 1:#如果存在 默认值为1
            playerset = names.get(str(source.player)+'_status') 
        else:
            names[str(source.player)+'_status'] = 0
            playerset = 0
            
    #权限验证通过
        if playerset == 0:#如果没飞过
            source.get_server().execute('fly ' + source.player+' true')
            source.get_server().execute('say ' + source.player+'开启了飞行')
            names[str(source.player)+'_status'] = 1            
        else:#如果飞过了
            source.get_server().execute('fly ' + source.player+' false')
            source.get_server().execute('say ' + source.player+'关闭了飞行')
            names[str(source.player)+'_status'] = 0

    else:
    #权限验证不通过
        source.get_server().execute('msg ' + source.player+' 你说得对，但你并没有权限')
        source.get_server().execute('say ' + source.player+'权限不足')              
        
        
               
def on_load(server: 'PluginServerInterface', old):
    server.register_help_message('!!fly', '飞行')
    server.register_command(
        Literal('!!fly').runs(fly)
    )
    #需要把可飞行玩家的权限设置为helper