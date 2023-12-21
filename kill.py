from typing import TYPE_CHECKING
from mcdreforged.api.command import Literal

if TYPE_CHECKING:
    from mcdreforged.api.types import PluginServerInterface, PlayerCommandSource


def execute(source: 'PlayerCommandSource'):
    if source.is_player:
        source.get_server().execute('kill ' + source.player)

def on_load(server: 'PluginServerInterface', old):
    server.register_help_message('!!kill', '自杀')
    server.register_command(
        Literal('!!kill').runs(execute)
    )