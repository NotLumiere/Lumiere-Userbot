# Ayiin - Userbot
# Credits (C) 2022-2023 @AyiinXd
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


import asyncio
from secrets import choice
from time import sleep

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import BLACKLIST_CHAT, CMD_HELP
from AyiinXd.ayiin import asupan_sagapung, exolink
from AyiinXd.ayiin import ayiin_cmd, edit_or_reply


kazuuserbot = "https://telegra.ph/file/762510fa43ef987980d55.jpg"
asupung = "https://telegra.ph/file/3a1c13d469901625e7c76.jpg"
exorcist2 = "https://telegra.ph/file/f0383ed4de3a719e2eada.jpg"


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern="Kazu(?: |$)(.*)")
async def _(yins):
    if yins.chat_id in BLACKLIST_CHAT:
        return await yins.edit("**[𝙱𝙻𝙾𝙲𝙺𝙴𝙳]** - Perintah Itu Dilarang Di Gc Ini.")
    await edit_or_reply(yins, "`𝙺𝙰𝚉𝚄-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 Nih Boss Senggol Dong...`")
    sleep(2)
    text = str(yins.pattern_match.group(1).split(" ", 1)[0])
    link = str(yins.pattern_match.group(1).split(" ", 2)[0])
    ayiin = text.replace(".", " ")
    user = await yins.client.get_me()
    link_2 = choice(exolink)
    thumb = kazuuserbot
    output = (
        f"**ʀᴇǫᴜᴇsᴛ ʙʏ :** @{user.username}\n\n"
        f"**{ayiin}**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**               𝙺𝙰𝚉𝚄-𝚄𝚂𝙴𝚁𝙱𝙾𝚃**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n\n"
        f"**⌲ 𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈**\n"
        f"**⌲ {link_2} {link}**\n\n"
        f"**       𝙐𝙎𝙀𝙍𝘽𝙊𝙏 𝙋𝙍𝙀𝙈𝙄𝙐𝙈**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**          @punyaionnibos**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n"
        f"**    𝙅𝘼𝙉𝙂𝘼𝙉 𝙇𝙐𝙋𝘼 𝙎𝙃𝘼𝙍𝙀 **\n\n"
        f"**PUNYA KAZU-USERBOT**\n\n"
        f"**𝙶𝚁𝙾𝚄𝙿 : @kazusupportgrp**\n"
        f"**𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @punyaionnibos**\n"
    )
    if thumb:
        try:
            logo = thumb
            await yins.delete()
            msg = await yins.client.send_file(yins.chat_id, logo, caption=output)
            await asyncio.sleep(300)
            await msg.delete()
        except BaseException:
            await yins.edit(
                output + "\n\n **Logo yang diberikan tidak valid.**"
                "\n**Pastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(100)
            await yins.delete()
    else:
        await edit_or_reply(yins, output)


@ayiin_cmd(pattern="Naya(?: |$)(.*)")
async def _(asupng):
    if asupng.chat_id in BLACKLIST_CHAT:
        return await asupng.edit("**[𝙱𝙻𝙾𝙲𝙺𝙴𝙳]** - Perintah Itu Dilarang Di Gc Ini.")
    await edit_or_reply(asupng, "`Kynan Nih Boss Senggol Dong...`")
    sleep(1)
    text = str(asupng.pattern_match.group(1).split(" ", 1)[0])
    link = str(asupng.pattern_match.group(1).split(" ", 2)[0])
    ayiin = text.replace(".", " ")
    user = await asupng.client.get_me()
    link_2 = choice(asupan_sagapung)
    image = asupung
    output = (
        f"**ʀᴇǫᴜᴇsᴛ ʙʏ :** @{user.username}\n\n"
        f"**{ayiin}**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**               𝙽𝙰𝚈𝙰-𝙿𝚈𝚁𝙾**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n\n"
        f"**⌲ 𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈**\n"
        f"**⌲ {link_2} {link}**\n\n"
        f"**       𝙐𝙎𝙀𝙍𝘽𝙊𝙏 𝙋𝙍𝙀𝙈𝙄𝙐𝙈**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**          @Kynansupport**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n"
        f"**    𝙅𝘼𝙉𝙂𝘼𝙉 𝙇𝙐𝙋𝘼 𝙎𝙃𝘼𝙍𝙀 **\n\n"
        f"**Punya 𝙽𝙰𝚈𝙰-𝙿𝚈𝚁𝙾**\n\n"
        f"**𝙶𝚁𝙾𝚄𝙿 : @kynansupport**\n"
        f"**𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @kontenfilm**\n"
    )
    if image:
        try:
            logo = image
            await asupng.delete()
            msg = await asupng.client.send_file(asupng.chat_id, logo, caption=output)
            await asyncio.sleep(300)
            await msg.delete()
        except BaseException:
            await asupng.edit(
                output + "\n\n **Logo yang diberikan tidak valid."
                "\nPastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(100)
            await asupng.delete()
    else:
        await edit_or_reply(asupng, output)

# ========================×========================
#               For Admin Collaborator
# ========================×========================


@ayiin_cmd(pattern="^Kazu(?: |$)(.*)")
async def yinscollab(exor):
    if exor.chat_id in BLACKLIST_CHAT:
        return await exor.edit("**[𝙱𝙻𝙾𝙲𝙺𝙴𝙳]** - Perintah Itu Dilarang Di Gc Ini.")
    await edit_or_reply(exor, "`𝙺𝙰𝚉𝚄-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 Nih Boss Senggol Dong...`")
    sleep(1)
    if exor.pattern_match.group(1):
        text, link = exor.pattern_match.group(1).split()
    ayiin = text.replace(".", " ")
    thumbnail = kazuuserbot 
    output = (
        f"**ʀᴇǫᴜᴇsᴛ ʙʏ :** @{user.username}\n\n"
        f"**{ayiin}**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**               𝙺𝙰𝚉𝚄-𝚄𝚂𝙴𝚁𝙱𝙾𝚃**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n\n"
        f"**⌲ 𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈**\n"
        f"**⌲ {link_2} {link}**\n\n"
        f"**       𝙐𝙎𝙀𝙍𝘽𝙊𝙏 𝙋𝙍𝙀𝙈𝙄𝙐𝙈**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**          @punyaionnibos**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n"
        f"**    𝙅𝘼𝙉𝙂𝘼𝙉 𝙇𝙐𝙋𝘼 𝙎𝙃𝘼𝙍𝙀 **\n\n"
        f"**PUNYA KAZU-USERBOT**\n\n"
        f"**𝙶𝚁𝙾𝚄𝙿 : @kazusupportgrp**\n"
        f"**𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @punyaionnibos**\n"
    )
    if thumbnail:
        try:
            logo = thumbnail
            await exor.delete()
            msg = await exor.client.send_file(exor.chat_id, logo, caption=output)
            await asyncio.sleep(300)
            await msg.delete()
        except BaseException:
            await exor.edit(
                output + "\n\n **Logo yang diberikan tidak valid.**"
                "\n**Pastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(100)
            await exor.delete()
    else:
        await edit_or_reply(exor, output)


@ayiin_cmd(pattern="^Naya(?: |$)(.*)")
async def _(asupng):
    if asupng.chat_id in BLACKLIST_CHAT:
        return await asupng.edit("**[𝙱𝙻𝙾𝙲𝙺𝙴𝙳]** - Perintah Itu Dilarang Di Gc Ini.")
    await edit_or_reply(asupng, "`Kynan Nih Boss Senggol Dong...`")
    sleep(1)
    link = asupng.pattern_match.group(1)
    image = asupung
    output = (
        f"**ʀᴇǫᴜᴇsᴛ ʙʏ :** @{user.username}\n\n"
        f"**{ayiin}**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**               𝙽𝙰𝚈𝙰-𝙿𝚈𝚁𝙾**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n\n"
        f"**⌲ 𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈**\n"
        f"**⌲ {link_2} {link}**\n\n"
        f"**       𝙐𝙎𝙀𝙍𝘽𝙊𝙏 𝙋𝙍𝙀𝙈𝙄𝙐𝙈**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**          @Kynansupport**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n"
        f"**    𝙅𝘼𝙉𝙂𝘼𝙉 𝙇𝙐𝙋𝘼 𝙎𝙃𝘼𝙍𝙀 **\n\n"
        f"**Punya 𝙽𝙰𝚈𝙰-𝙿𝚈𝚁𝙾**\n\n"
        f"**𝙶𝚁𝙾𝚄𝙿 : @kynansupport**\n"
        f"**𝚂𝚄𝙿𝙿𝙾𝚁𝚃 : @kontenfilm**\n"
    )
    if image:
        try:
            logo = image
            await asupng.delete()
            msg = await asupng.client.send_file(asupng.chat_id, logo, caption=output)
            await asyncio.sleep(800)
            await msg.delete()
        except BaseException:
            await asupng.edit(
                output + "\n\n **Logo yang diberikan tidak valid.**"
                "\n**Pastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(100)
            await asupng.delete()
    else:
        await edit_or_reply(asupng, output)


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "collab": f"**Plugin:** `Menampilkan Collaboration dari Lumiere-Userbot`\
        \n\n  »  **Perintah :** `{cmd}Kazu`\
        \n  »  **Kegunaan :** Untuk Mendapatkan Info Tentang 𝙺𝙰𝚉𝚄-𝚄𝚂𝙴𝚁𝙱𝙾𝚃.\
        \n\n  »  **Perintah :** `{cmd}Naya`\
        \n  »  **Kegunaan :** Untuk Mendapatkan Info Tentang 𝙽𝙰𝚈𝙰-𝙿𝚈𝚁𝙾.\
    "
    }
)


CMD_HELP.update(
    {
        "lumicollab": f"**Plugin : **``\
        \n\n  »  **Perintah:** `Ini Khusus Buat Kazu dan Kynan Tod Bukan Publik.`\
        \n  »  **Silahkan Ketik** `{cmd}help collab` **Untuk Mendapatkan info tentang collab.**\
    "
    }
)
