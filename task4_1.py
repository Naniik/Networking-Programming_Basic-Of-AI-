from telethon import TelegramClient
from config import api_id, api_hash

chat = "https://t.me/+2kgeO_FP6KBlNjBi"

client = TelegramClient(
    "test", api_id, api_hash,
    device_model="SM-S926B/DS", system_version="Android 16", app_version="13.1.1",
        lang_code="uk", system_lang_code="uk-UA",
)


async def main():
    async for user in client.iter_participants(chat):
        print(user.id, user.username, user.first_name, user.last_name)


with client:
    client.loop.run_until_complete(main())