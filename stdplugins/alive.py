""".on cmd to see if your userbot is ALIVE or Dead"""

import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd
import uniborg
from os import remove
from platform import python_version, uname
from shutil import which
from telethon import version

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE

from shutil import which
from os import remove
from telethon import version

from platform import python_version, uname
from sample_config import Config


# ================= CONSTANT =================
DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================


# @register(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd("on"))
async def amireallyalive(on):
    """ For .on command, check if the bot is running.  """
    await on.edit(
<<<<<<< HEAD
                     " 🤖Hey `I am ON Ashwin.`🤖\n"
                     " \n"
                     f"📱Telethon version: {version.__version__} \n"
                     f"🐍Python: {python_version()} \n"
                     f"------------------------------------ \n"
                     f"👦🏻User: {DEFAULTUSER} \n"
                     " \n"
                     "🤖`I will never die.`🤖")    
=======
                     " Hey `i am 𝐎𝓷 My 𝕄𝕒𝕤𝕥𝕖𝕣`\n"
                     " \n"
                     f"тєℓєтнση νєяѕιση: {version.__version__} \n"
                     f"P̳y̳t̳h̳o̳n̳ ̳v̳e̳r̳s̳i̳o̳n̳: {python_version()} \n"
                     f"------------------------------------ \n"
                     f"U̴̧̡̫̤̦̇͆͛̿͑̈́̂̊̚͝s̷̡͓͎͘e̷̹̙̝̽̾͂ŕ̴̡̛̺̖̝̬̣͖͕̐̅͌͂͌̕: {DEFAULTUSER} \n"
                     f"🅲🆁🅴🅰🆃🅾🆁: @🄼🄰🅈🅄🅁_🄺🄰🅁🄰🄽🄸🅈🄰 \n"
                     f"𝓞𝔀𝓷𝓮𝓻: `@𝓣𝓱𝓻𝓮𝓮_𝓒𝓾𝓫𝓮_𝓣𝓮𝓚𝓷𝓸𝔀𝓪𝔂𝓼` \n"
                     f"ᗯEᗷᔕITE: 𝖍𝖙𝖙𝖕𝖘://𝖜𝖜𝖜.𝖋𝖆𝖈𝖊𝖇𝖔𝖔𝖐.𝖈𝖔𝖒/𝕿𝖊𝖐𝖓𝖔𝖜𝖆𝖞𝖘 \n"
                     f"U҉s҉e҉r҉b҉o҉t҉: @ₜₑₛₜing_bₒₜ \n"
                     "`𝘪 𝙘𝙖𝙣'𝙩 Ðïê`")    
>>>>>>> 6dbcf1165458cda768187ead535423b5791a29b1
