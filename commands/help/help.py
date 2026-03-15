import discord
import config


def add_help_line(command: str, args: list[str], description: str, owner_only: bool) -> str:
    line = f"**{command}**"
    if len(args) > 0:
        for arg in range(len(args)):
            line += f" [{args[arg]}]"
    if owner_only:
        line += " (Owner only)"
    line += f"\n{description}\n"

    return line

def help() -> discord.Embed:
    embed = discord.Embed(
        title="Help",
        color=config.EMBED_COLOR
    )

    lines = [
        add_help_line("help", [], "Shows this help page", False),
        add_help_line("fish", [], "Makes the bot fish", False),
        add_help_line("points", [], "Get your current points", False),
        add_help_line("leaderboard", [], "Displays the point leaderboard", False),
        add_help_line("send", ["message"], "Makes the bot send a message", False),
        add_help_line("restart", [], "Restarts the bot", True),
        add_help_line("stop", [], "Stops the bot", True)
    ]

    embed.description = "\n".join(lines)

    return embed
