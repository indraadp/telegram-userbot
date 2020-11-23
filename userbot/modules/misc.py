# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD

import io
import sys
from os import execl
from random import randint
from time import sleep

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register
from userbot.utils import time_formatter


@register(outgoing=True, pattern=r"^\.random")
async def randomise(items):
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        return await items.edit(
            "`2 or more items are required! Check .help random for more info.`"
        )
    index = randint(1, len(itemo) - 1)
    await items.edit(
        "**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" + itemo[index] + "`"
    )


@register(outgoing=True, pattern=r"^\.sleep ([0-9]+)$")
async def sleepybot(time):
    counter = int(time.pattern_match.group(1))
    await time.edit("`I am sulking and snoozing...`")
    if BOTLOG:
        str_counter = time_formatter(counter)
        await time.client.send_message(
            BOTLOG_CHATID,
            f"You put the bot to sleep for {str_counter}.",
        )
    sleep(counter)
    await time.edit("`OK, I'm awake now.`")


@register(outgoing=True, pattern=r"^\.shutdown$")
async def killthebot(event):
    await event.edit("`Shutdown userbot...`")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n" "Bot shutdown")
    await bot.disconnect()


@register(outgoing=True, pattern=r"^\.restart$")
async def killdabot(event):
    await event.edit("`Restarting userbot...`")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTART \n" "Bot Restarted")
    await bot.disconnect()
    # Spin a new instance of bot
    execl(sys.executable, sys.executable, *sys.argv)
    # Shut the existing one down
    sys.exit()


@register(outgoing=True, pattern=r"^\.readme$")
async def reedme(e):
    await e.edit(
        "Here's something for you to read:\n"
        "\nSupport Group:"
        "\nJoin Userbot Indonesia Group: [Click Here](https://t.me/userbotindo)"
        "\nJoin RaphielGang Group: [Click Here](https://t.me/tgpaperplane)\n"
        "\nSome Setup Guides:"
        "\nSetup Guide - Indonesian: [Click Here](https://telegra.ph/UserIndoBot-05-21-3)"
        "\nSetup Guide - English: [Click Here](https://telegra.ph/How-to-host-a-Telegram-Userbot-07-01-2)"
        "\nSetup Guide - From MiHub: [Click Here](https://www.mihub.my.id/2020/05/jadiuserbot.html)"
        "\nGenerate String Session: [Click Here](https://string.projectalf.repl.run/)"
        "\nSetup Guide - Google Drive: [Click Here](https://telegra.ph/How-To-Setup-Google-Drive-04-03)"
        "\nSetup Guide - LastFM: [Click Here](https://telegra.ph/How-to-set-up-LastFM-module-for-Paperplane-userbot-11-02)\n"
        "\nVideo Tutorial:"
        "\nVideo Tutorial - [576p](https://mega.nz/#!ErwCESbJ!1ZvYAKdTEfb6y1FnqqiLhHH9vZg4UB2QZNYL9fbQ9vs)"
        "\nVideo Tutorial - [1080p](https://mega.nz/#!x3JVhYwR!u7Uj0nvD8_CyyARrdKrFqlZEBFTnSVEiqts36HBMr-o)"
    )


# Copyright (c) Gegham Zakaryan | 2019
@register(outgoing=True, pattern=r"^\.repeat (.*)")
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(" ", 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for _ in range(replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@register(outgoing=True, pattern=r"^\.repo$")
async def repo_is_here(wannasee):
    await wannasee.edit(
        "Source repo my Userbot: [Click Here](https://github.com/alfianandaa/ProjectAlf)"
    )


@register(outgoing=True, pattern=r"^\.raw$")
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await event.edit("`Check the userbot log for the decoded message data !!`")
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Here's the decoded message data !!`",
        )


CMD_HELP.update(
    {
        "random": ">`.random <item1> <item2> ... <itemN>`"
        "\nUsage: Get a random item from the list of items.",
        "sleep": ">`.sleep <seconds>`" "\nUsage: Let yours snooze for a few seconds.",
        "shutdown": ">`.shutdown`" "\nUsage: Shutdown bot",
        "repo": ">`.repo`" "\nUsage: Github Repo of this bot",
        "readme": ">`.readme`"
        "\nUsage: Provide links to setup the userbot and it's modules.",
        "repeat": ">`.repeat <no> <text>`"
        "\nUsage: Repeats the text for a number of times. Don't confuse this with spam tho.",
        "restart": ">`.restart`" "\nUsage: Restarts the bot !!",
        "raw": ">`.raw`"
        "\nUsage: Get detailed JSON-like formatted data about replied message.",
    }
)
