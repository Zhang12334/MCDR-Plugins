from typing import TYPE_CHECKING
from mcdreforged.api.command import Literal
import json
import os

PLUGIN_METADATA = {
    'id': 'eula_killer',
    'version': '1.0.0',
    'name': 'By Zhang1233'
}

if TYPE_CHECKING:
    from mcdreforged.api.types import PluginServerInterface, PlayerCommandSource
       
def on_load(server: 'PluginServerInterface', old):
    if os.path.exists("server/eula.txt"):
        server.logger.info('EULA寄咯~')
    else:
        with open("server/eula.txt", "w") as f:
            f.write(json.dumps(eula=true))     # 创建一个EULA并且往死里开他娘的意大利炮
        server.logger.info('开炮！！！！！')