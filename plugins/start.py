
from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Updates Channel", url="https://t.me/phoenix_empire")
      ],
      [ 
        InlineKeyboardButton(
            "Support Group", url="https://t.me/CFC_BOT_support")]
    ])
    welcomed = f"<b> Hey {message.from_user.first_name} , \n\nI'm YouTube DL Bot. I can download video or audio f\n rom Youtube. \n\nCreated by @heyaaman 🇱🇰/help for More info </b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagatio
