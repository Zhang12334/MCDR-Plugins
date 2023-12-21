from typing import TYPE_CHECKING
from mcdreforged.api.command import Literal
import json
import os

if TYPE_CHECKING:
    from mcdreforged.api.types import PluginServerInterface, PlayerCommandSource
    

def load_config():
    # 判断JSON文件是否存在
    if os.path.exists("player.json"):
        with open("player.json", "r") as f:
            # 读取文件
            player = json.loads(f.read())["player"]
            return player
    else:
        fly_player = []
        with open("player.json", "w") as f:
            f.write(json.dumps({"player": []}))     # 创建一个空的配置文件
        return []
    
def on_player_joined(server: 'PluginServerInterface', player: str, info: 'Info'):
    if player in load_config():
        server.say('{},又来摸鱼啦？'.format(player))
    else:
        server.say('欢迎新玩家{}! 一起加入到摸鱼大家庭来吧awa'.format(player))
        with open("player.json", "r") as f:
            config = json.loads(f.read())
            config["player"].append(player)
        with open("player.json", "w") as f:
            f.write(json.dumps(config))


def on_load(server: 'PluginServerInterface', old):
    server.register_help_message('!!welcome', '一个欢迎插件')