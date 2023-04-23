🎶 Cyber Music Bot 🎶

Cyber Music is a telegram bot project that's allow you to play music on telegram voice chat group.



    Codacy
       

Requirements 📝

FFmpeg
NodeJS nodesource.com
Python 3.8+ or 3.7
PyTgCalls
MongoDB
🧪 Get STRING_SESSION from below:

TAP THIS: GenerateString

🎖 History

Mentioned in Awesome Python
Features 🔮

Thumbnail Support
Playlist Support
Showing track names when skipping
Youtube, Local playback support
Settings panel
Control with buttons
Userbot auto join
Channel Music Play
Keyboard selection support for youtube play
Lyrics Scrapper
Unlimited Queue
Broadcast Bot
Statistic Collector
Group Tools (ban/unban/mute/unmute)
. Block / Unblock (restrict user for using your bot)
Commands 🛠

/play <song name> - play song you requested
/playlist - Show now playing list
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/vsong <song name> - download videos you want quickly
/lyric <song name> - lyrics scrapper
/vk <song name> - generate song without download
Admins Only 👷‍♂️

/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/musicplayer on - to disable music player in your group
/musicplayer off - to enable music player in your group
/userbotjoin - invite assistant to your chat
/userbotleave - remove assistant from your chat
/reload - Refresh admin list
/uptime - check the bot uptime status
/ping - check the bot ping status
/auth - authorized people to access the admin commands
/deauth - deauthorized people to access the admin commands
/control - open the music player control panel
Sudo User 🧙‍♂️

/stats - see the bot statistic
/pmpermit on | off turn on/off the assistant pmpermit
/userbotleaveall - order the assistant to leave all groups
/gcast - send a broadcast message from the assistant
Owner Only 👨🏻‍✈️

/broadcast - send a broadcast message from the bot
/block - block people for using your bot
/unblock - unblock people you blocked for using your bot
/blocklist - show the list of all people who's blocked for using your bot
pm-permit 💬

.yes - approve user for sending message to assistant
.no - disapprove user for sending message to assistant
🔎 Support Inline Search

Heroku Deployment 💜

The easy way to host this bot, deploy to Heroku

Deploy

Railway Deployment 🚄

For deployment on railway you can see the full of Necessary Variables Here, make sure you fill all of it.

Deploy+on+Railway

Deploy On VPS 💜

sudo apt update && apt upgrade -y
sudo apt install git curl python3-pip ffmpeg -y
pip3 install -U pip
curl -sL https://deb.nodesource.com/setup_16.x | bash -
sudo apt-get install -y nodejs
npm i -g npm
git clone https://github.com/aryazakaria01/CBMusicBot # Clone your repo.
cd CBMusicBot
pip3 install -U -r requirements.txt
cp example.env .env #Use vim to edit ENVs
vim .env #Fill up your ENVs ( Steps press i to enter in insert mode then edit the file. Press Esc to exit the editing mode then type :wq! and press Enter key to save the file.)
python3 main.py # Run the bot
Special Credits 💖


