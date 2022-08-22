# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, ultroid_cmd

REPOMSG = """
• **BAY USERBOT** •\n
• Repo - [Click Here](https://telegram.dog/XTZ_HerokuBot?start=ZWxpZXZlL3VsdHJvIG1haW4)
• Jasa - [Click Here](@baytoddd)
• Support - @ygabutkan
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://telegram.dog/XTZ_HerokuBot?start=ZWxpZXZlL3VsdHJvIG1haW4"),
        Button.url("Addons", "https://github.com/elieve/elieve"),
    ],
    [Button.url("Support Group", "t.me/ygabutkan")],
]

ULTSTRING = """🎇 **Terimakasih Sudah Menggunakan BAY Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ultroid_cmd(
    pattern="github$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info("Error while repo command : " + str(er))
    await e.eor(REPOMSG)


@ultroid_cmd(pattern="bot$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://telegra.ph/file/f2f144d1f4979db77e5f9.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
