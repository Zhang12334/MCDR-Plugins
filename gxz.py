from typing import TYPE_CHECKING
from mcdreforged.api.command import Literal
import json
import os
import time
names = locals()

PLUGIN_METADATA = {
    'id': 'gxz_ofs',
    'version': '1.0.0',
    'name': 'By Zhang1233'
}

if TYPE_CHECKING:
    from mcdreforged.api.types import PluginServerInterface, PlayerCommandSource
    

def load_gxz(player: str):
    # 判断JSON文件是否存在
    openaddress = 'config/player_gxz/'+str(player)+'.json'    
    if os.path.exists(openaddress):
        with open(openaddress, "r") as f:
            # 读取文件
            [value] = json.loads(f.read())["value"]
            return value
    else:
        with open(openaddress, "w") as f:
            f.write(json.dumps({"value":[0]}))     # 创建一个空的配置文件
        return 0
        
def load_opentime(player: str):        
    opentime = 'config/player_gxz/'+str(player)+'_opentime.json'
    if os.path.exists(opentime):
        with open(opentime, "r") as f:
            # 读取文件
            [value] = json.loads(f.read())["value"]
            return value
    else:
        with open(opentime, "w") as f:
            f.write(json.dumps({"value":[0]}))     # 创建一个空的配置文件
        return 0        
    
def on_player_joined(server: 'PluginServerInterface', player: str, info: 'Info'):
    if 'bot_' in player:
        print("非玩家数据，已终止记录")
    else:
        load_gxz(player)
        allopentime = load_opentime(player)
        if allopentime >=10800:
            jianwanzhihou = allopentime-10800
            opentime = 'config/player_gxz/'+str(player)+'_opentime.json'
            with open(opentime, "w") as f:
                f.write(json.dumps({"value":[jianwanzhihou]}))     # 覆写
            openaddress = 'config/player_gxz/'+str(player)+'.json'
            all_gxz = load_gxz(player) + 1
            with open(openaddress, "w") as f:
                f.write(json.dumps({"value":[all_gxz]}))     # 覆写贡献值
        names[str(player)+'_jointime'] = time.time()#记录加入时间
    
def on_player_left(server: 'PluginServerInterface', player: str):
    if 'bot_' in player:
        print("非玩家数据，已终止记录")
    else:
        load_gxz(player)
        opentime = 'config/player_gxz/'+str(player)+'_opentime.json'
        names[str(player)+'_leavetime'] = time.time()#记录离开时间
        names[str(player)+'_thisjointime'] = names[str(player)+'_leavetime'] - names[str(player)+'_jointime']
        timebefore = load_opentime(player)
        time_add = names[str(player)+'_thisjointime'] + timebefore
        with open(opentime, "w") as f:
            f.write(json.dumps({"value":[time_add]}))     # 覆写
    
    
       
           
def chaxun(source: 'CommandSource'):
    value = load_gxz(source.player)
    if value == 0:
        source.get_server().execute('say 快来看，杂鱼'+source.player+'连一个贡献值都没有哦~')
    else:
        source.get_server().execute('say '+source.player+'的贡献值为'+str(value))

def on_load(server: 'PluginServerInterface', old):
    server.register_help_message('GXZ', '摸鱼服贡献值系统')
    server.register_command(
        Literal('!!gxz_cx').runs(chaxun)
    )