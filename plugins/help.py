from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Şu anda sadece tek link, (Oynatma listesi yok) Sadece Youtube URL'sini Gönderin"
    await message.reply_text(helptxt)
