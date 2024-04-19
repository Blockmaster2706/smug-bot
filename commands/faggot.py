import  hikari
import  lightbulb
from    cmd_log     import cmd_log
from    permcheck   import permcheck

plugin = lightbulb.Plugin("Faggot")

@plugin.command()
@lightbulb.option("user", "The user to faggot", type=hikari.OptionType.USER, required=True)
@lightbulb.command("faggot", "Calls someone else a faggot.")
@lightbulb.implements(lightbulb.SlashCommand)
async def faggot(ctx: lightbulb.Context) -> None:

    await cmd_log(ctx)

    if await permcheck(ctx):
        await ctx.respond("Faggot! " + ctx.options.user.mention, user_mentions=True)
        return
    else:
        ctx.respond("No Perms")

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)