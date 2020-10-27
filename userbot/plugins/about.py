# Ported from other Telegram UserBots for TeleBot//Made for TeleBot
# Kangers, don't remove this line
# @Lovedeep_ViRk

"""Available Commands:
.info
"""

import asyncio

from userbot.utils import admin_cmd


@telebot.on(admin_cmd(pattern="info"))
@telebot.on(sudo_cmd(pattern="info", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "Visit this page to know more about TeleBot.":
    await eor(event, "Thanks")
    animation_chars = ["**DeepTeleBot**", "[More Info](https://telegra.ph/DeepTeleBot-10-27"]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await eor(event, animation_chars[i % 18])
