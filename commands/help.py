import  hikari
import  lightbulb
from    cmd_log     import cmd_log
from    permcheck   import permcheck
from    commandhelp import  command_help

plugin = lightbulb.Plugin("Help")

@plugin.command()
@lightbulb.option("command", "The command to which you need help", type=str, default="help")
@lightbulb.command("help", "Help to commands")
@lightbulb.implements(lightbulb.PrefixCommand)
async def help(ctx: lightbulb.Context) -> None:

    await cmd_log(ctx)

    if await permcheck(ctx):
        await ctx.respond("{}".format(command_help(ctx.options["command"])))
    else:
        ctx.respond("No Perms")

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)