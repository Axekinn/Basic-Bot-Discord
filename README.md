# 🤖 Simple Discord Bot

<div align="center">

[![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/your-invite)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-6.2.0-blue?style=for-the-badge)]()

*A modern and versatile Discord bot with XP system, custom commands, moderation and much more!*

</div>

---

## 📋 Table of Contents

- [✨ Main Features](#-main-features)
- [🚀 Quick Installation](#-quick-installation)
- [⚙️ Configuration](#️-configuration)
- [📚 Modules and Commands](#-modules-and-commands)
- [🎯 Usage Guide](#-usage-guide)
- [🔧 Advanced Configuration](#-advanced-configuration)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Main Features

### 🏆 **Experience and Level System**
- **Automatic progression**: Gain XP per message sent
- **Level system** with 50+ tiers
- **Automatic roles** by level
- **Interactive leaderboard** with ranking
- **Admin commands** to manage XP

### 🎮 **Custom Commands**
- **Intuitive command creator** with interactive interface
- **Global and server commands**
- **Advanced search** and filtering system
- **Export commands** to Markdown file
- **Complete management** via modern interface

### 🔨 **Advanced Moderation**
- **Kick/Ban** with reasons and durations
- **Temporary mute** with automatic management
- **Warning system** with history
- **Bulk message cleanup**
- **Detailed moderation logs**

### 🎉 **Giveaway System**
- **Easy creation** of contests
- **Automatic management** of draws
- **Reaction system** to participate
- **Automatic notifications** of results

### 🎲 **Fun Commands**
- **Interactive Rock-Paper-Scissors**
- **Coin Flip** with buttons
- **Random fact generator**
- **Jokes** and entertainment

### 🎵 **Temporary Voice Channels**
- **Automatic creation** of voice channels
- **Custom permission management**
- **Automatic deletion** when empty

### 📊 **Voting System**
- **Interactive poll creation**
- **Modification** of existing votes
- **Real-time results**

### 🔍 **Information and Utilities**
- **Detailed server information**
- **Complete user profile**
- **Bot information** and statistics
- **Context menu** for quick actions

---

## 🚀 Quick Installation

### 📋 Prerequisites
- **Python 3.8+** installed
- **Discord Bot** created on [Discord Developer Portal](https://discord.com/developers/applications)
- **Git** (optional)

### 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Axekinn/Simple-Bot-Discord.git
cd Simple-Bot-Discord
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure files**
```bash
# Copy example files
cp .env.example .env
cp config.json.example config.json
cp commands.json.example commands.json
cp xp_data.json.example xp_data.json
cp giveaways.json.example giveaways.json
cp role_reactions.json.example role_reactions.json
```

4. **Configure the token**
```bash
# Edit the .env file
TOKEN=YOUR_DISCORD_BOT_TOKEN
```

5. **Start the bot**
```bash
python bot.py
```

---

## ⚙️ Configuration

### 🔑 `.env` File
```env
TOKEN=YOUR_DISCORD_BOT_TOKEN
```

### 📝 `config.json` File
```json
{
  "prefix": "!",
  "owner_id": "YOUR_DISCORD_ID",
  "description": "A simple and powerful Discord bot",
  "website": "https://your-website.com/",
  "discord_invite": "https://discord.gg/your-invite",
  "github": "https://github.com/your-username/your-repo"
}
```

---

## 📚 Modules and Commands

### 🏆 **XP Module (Experience)**

| Command | Description | Permissions |
|---------|-------------|-------------|
| `/xp [member]` | Shows XP and level of a member | Everyone |
| `/leaderboard` | Server ranking by level | Everyone |
| `/resetxp <member>` | Resets a member's XP | Administrator |
| `/setwords <member> <words>` | Sets total word count | Administrator |
| `/recalculatelevels` | Recalculates all levels | Administrator |
| `/xpinfo` | Information about XP system | Everyone |
| `/milestones` | Shows all level milestones | Everyone |
| `/setlevelup [channel]` | Configures notification channel | Administrator |
| `/setlevelrole <level> <role>` | Assigns a role to a level | Administrator |
| `/updateallroles` | Updates all roles by level | Administrator |

**🎯 Progression System**
- **XP Gain**: 1 XP per word written in a message
- **Cooldown**: 1 minute between XP gains
- **Level Formula**: `level = floor(sqrt(total_words / 100))`
- **Maximum levels**: 50+ tiers available

### 🛠️ **Custom Commands Module**

| Command | Description | Permissions |
|---------|-------------|-------------|
| `/create_command` | Command creation interface | Administrator |
| `/commands [scope] [filter]` | Interactive command browser | Everyone |

**🎨 Advanced Features**
- **Modern interface** with buttons and selectors
- **Advanced search** by name, description or content
- **Markdown export** of commands
- **Category management** (global/server)
- **Smart pagination** system

### 🔨 **Moderation Module**

| Command | Description | Permissions |
|---------|-------------|-------------|
| `/kick <user> [reason]` | Kicks a member | Kick Members |
| `/ban <user> [reason]` | Bans a member | Ban Members |
| `/unban <user>` | Unbans a member | Ban Members |
| `/timeout <user> <duration>` | Temporarily mutes | Moderate Members |
| `/untimeout <user>` | Removes timeout | Moderate Members |
| `/purge <number>` | Deletes messages | Manage Messages |
| `/warn <user> [reason]` | Warns a member | Kick Members |

**⚡ Features**
- **Automatic security checks**
- **Detailed action logs**
- **Complete error handling**
- **Built-in administrator protection**

### 🎉 **Giveaways Module**

| Command | Description | Permissions |
|---------|-------------|-------------|
| `/giveaway <duration> <prize>` | Creates a new giveaway | Manage Messages |
| `/gend <message_id>` | Ends a giveaway | Manage Messages |
| `/greroll <message_id>` | Rerolls the draw | Manage Messages |

**🎁 Features**
- **Automatic draw management**
- **Reaction interface** 🎉
- **Winner notifications**
- **Persistent data storage**

### 🎮 **Fun Module**

| Command | Description | Permissions |
|---------|-------------|-------------|
| `/randomfact` | Random fact in English | Everyone |
| `/coinflip` | Interactive coin flip | Everyone |
| `/rps` | Rock-paper-scissors | Everyone |

**🎯 Interactive Games**
- **Discord button interface**
- **Animations** and reactions
- **Score system** (coming soon)

### 🔍 **Information Module**

| Command | Description | Permissions |
|---------|-------------|-------------|
| `/help` | List of available commands | Everyone |
| `/botinfo` | Detailed bot information | Everyone |
| `/serverinfo` | Server information | Everyone |
| `/whois <member>` | Detailed member profile | Everyone |
| `/ping` | Bot latency | Everyone |
| `/invite` | Bot invitation link | Everyone |

### 🎵 **Voice Channel Module**

| Command | Description | Permissions |
|---------|-------------|-------------|
| `/voice setup <channel>` | Configures voice system | Administrator |

**🔊 Features**
- **Automatic creation** of temporary channels
- **Custom permissions** per user
- **Automatic deletion** on disconnect

### 📊 **Voting Module**

| Command | Description | Permissions |
|---------|-------------|-------------|
| `/vote_create <question>` | Creates a poll | Manage Messages |
| `/vote_edit <message_id>` | Edits an existing vote | Manage Messages |

### 🎭 **Role Reaction Module**

**Configuration** via `role_reactions.json` file
- **Automatic role assignment**
- **Custom reaction interface**
- **Multi-message management**

---

## 🎯 Usage Guide

### 🏆 **Setting Up XP System**

1. **Initial configuration**
```bash
/setlevelup #level-up
```

2. **Assign roles by level**
```bash
/setlevelrole level:5 role:@Active Member
/setlevelrole level:10 role:@Contributor
/setlevelrole level:25 role:@Expert
```

3. **System verification**
```bash
/milestones  # See all milestones
/xpinfo      # Detailed information
```

### 🛠️ **Creating Custom Commands**

1. **Launch interface**
```bash
/create_command
```

2. **Follow interactive wizard**
   - Choose scope (global/server)
   - Define command name
   - Add description
   - Configure response

3. **Test and manage**
```bash
/commands scope:server  # View server commands
```

### 🔨 **Moderation Setup**

1. **Recommended permissions**
   - Kick Members
   - Ban Members
   - Manage Messages
   - Moderate Members

2. **Typical usage**
```bash
/warn @user reason:Spam
/timeout @user duration:1h reason:Inappropriate behavior
/purge number:10
```

---

## 🔧 Advanced Configuration

### 🗄️ **Database**

The bot uses SQLite to store:
- **XP Data**: `xp_data.json`
- **Commands**: `commands.json`
- **Giveaways**: `giveaways.json`
- **Reactions**: `role_reactions.json`

### 📁 **File Structure**

```
Simple-Bot-Discord/
├── bot.py                 # Main file
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── config.json           # Bot configuration
├── commands.json         # Custom commands
├── xp_data.json         # Experience data
├── giveaways.json       # Giveaway data
├── role_reactions.json  # Role/reaction configuration
├── discord.log          # Bot logs
├── database/            # SQLite database
│   ├── __init__.py
│   ├── database.db
│   └── schema.sql
└── cogs/                # Bot modules
    ├── xp.py           # Experience system
    ├── command_builder.py  # Custom commands
    ├── moderation.py   # Moderation
    ├── giveaway.py     # Giveaways
    ├── fun.py          # Fun commands
    ├── general.py      # General commands
    ├── voice_creator.py # Temporary voice channels
    ├── vote.py         # Voting system
    ├── whois.py        # User information
    ├── role_reaction.py # Role reactions
    └── owner.py        # Owner commands
```

### 🔐 **Security**

- ✅ **Secure token** in `.env`
- ✅ **Sensitive files** in `.gitignore`
- ✅ **Permission checks** on all commands
- ✅ **Protection against** infinite loops
- ✅ **Complete error handling**

### 🚀 **Performance**

- **Local SQLite database** for speed
- **In-memory cache** for frequent data
- **Asynchronous loading** of modules
- **Discord API optimization**

---

## 🔧 Customization

### 🎨 **Modify Colors**
```python
# In each cog, modify embed colors
embed = discord.Embed(color=0x3498db)  # Blue
embed = discord.Embed(color=0xe74c3c)  # Red
embed = discord.Embed(color=0x2ecc71)  # Green
```

### 🏆 **Customize XP System**
```python
# In cogs/xp.py, line ~50
XP_PER_WORD = 1           # XP gained per word
XP_COOLDOWN = 60          # Cooldown in seconds
LEVEL_FORMULA = lambda w: math.floor(math.sqrt(w / 100))
```

### 🎭 **Add Commands**
```python
# Create a new file in cogs/
# Follow template in cogs/template.py
```

---

## 🛡️ Support and Troubleshooting

### ❓ **Common Issues**

**Bot offline?**
- Check token in `.env`
- Check bot permissions
- Check `discord.log` for errors

**Commands not working?**
- Check bot permissions
- Use `/` for slash commands
- Check intents configuration

**XP system inactive?**
- Check `message_content` permissions
- Verify intents are enabled
- Check logs for errors

### 📞 **Get Help**

- 🐛 **Report a bug**: [GitHub Issues](https://github.com/Axekinn/Simple-Bot-Discord/issues)
- 💬 **Discord**: [Join server](https://discord.gg/CUpf57y5Vg)
- 📧 **Email**: axekinn@proton.me

---

## 🤝 Contributing

We warmly welcome contributions! 

### 📝 **How to Contribute**

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### 🎯 **What We're Looking For**

- 🐛 **Bug fixes**
- ✨ **New features**
- 📚 **Documentation improvements**
- 🎨 **UI/UX enhancements**
- 🔧 **Performance optimizations**

### 📋 **Guidelines**

- Follow existing code style
- Test all new features
- Document code with comments
- Respect naming conventions

---

## 🏆 Contributors

A big thank you to all contributors who helped improve this bot!

<!-- Contributors section will be auto-generated -->

---

## 📊 Statistics

- ⭐ **Features**: 50+ commands
- 🔧 **Modules**: 12 cogs
- 🏆 **XP System**: 50+ levels
- 🎮 **Built-in games**: 3+
- 🔨 **Moderation tools**: 8+

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📈 Roadmap

### 🚀 **Version 7.0 (Next)**
- [ ] 🎵 **Complete music player**
- [ ] 📈 **Web dashboard** for configuration
- [ ] 🎯 **Mission system** and rewards
- [ ] 🔔 **Custom notifications**
- [ ] 📊 **Advanced server statistics**

### 🎯 **Version 7.1**
- [ ] 🎮 **Multiplayer mini-games**
- [ ] 💰 **Virtual economy** with shop
- [ ] 🎭 **Automatic temporary roles**
- [ ] 📱 **Mobile companion app**

### 🔮 **Future Versions**
- [ ] 🤖 **AI** for automatic moderation
- [ ] 🌍 **Complete multi-language** support
- [ ] ☁️ **Integrated cloud hosting**
- [ ] 📊 **Advanced analytics**

---

## 🙏 Acknowledgments

- **Discord.py** - For the excellent library
- **Krypton** - For the base template
- **Discord Community** - For testing and feedback
- **Contributors** - For their improvements

---

<div align="center">

**⭐ If this bot helped you, feel free to give the project a star! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/Axekinn/Simple-Bot-Discord?style=social)](https://github.com/Axekinn/Simple-Bot-Discord/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Axekinn/Simple-Bot-Discord?style=social)](https://github.com/Axekinn/Simple-Bot-Discord/network)

---

*Made with ❤️ by [Axekinn](https://github.com/Axekinn)*

</div>
