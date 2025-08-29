import discord
from discord.ext import commands
from discord import app_commands
import json
import os
import math
import re

class XP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.xp_data = self.load_xp_data()
        
        # NOUVEAU SYSTÈME D'XP
        self.base_words_per_level = 100  # Mots de base pour le niveau 1
        self.xp_multiplier = 1.5  # Multiplicateur pour chaque niveau (progression exponentielle)
        self.min_words_per_message = 3  # Minimum de mots pour compter
        self.max_words_per_message = 50  # Maximum de mots comptés par message (anti-spam)
        self.max_level = 50  # Maximum level cap
        
        # Descriptions des niveaux (expanded with humorous high-level titles)
        self.level_descriptions = {
            1: "Bronze Beater",
            2: "Silver Stroker", 
            3: "Golden Gooner",
            4: "Platinum Pusher",
            5: "Emerald Edger",
            6: "Diamond Dasher",
            7: "Master Manipulator",
            8: "Elite Enhancer",
            9: "Supreme Stroker",
            10: "Platinum Puller",
            11: "Grandmaster Baiter",
            12: "Discord Devotee",
            13: "Chat Champion",
            14: "Keyboard Warrior",
            15: "🎯 Milestone Master",
            16: "Text Tornado",
            17: "Message Maniac",
            18: "Word Wizard",
            19: "Conversation King",
            20: "🏆 Communication Commander",
            21: "Typing Titan",
            22: "Digital Dialoguer",
            23: "Server Scholar",
            24: "Channel Chief",
            25: "💎 Legendary Linguist",
            26: "Eternal Enthusiast",
            27: "Perpetual Poster",
            28: "Chronic Chatter",
            29: "Obsessive Orator",
            30: "🔥 Ascended Addict",
            31: "Terminal Texter",
            32: "Compulsive Communicator",
            33: "Habitual Harbinger",
            34: "Relentless Responder",
            35: "⚡ Transcendent Talker",
            36: "Infinite Informant",
            37: "Boundless Babbler",
            38: "Endless Eloquent",
            39: "Ceaseless Conversant",
            40: "🌟 Ultimate Utterer",
            41: "Mythical Messenger",
            42: "Legendary Linguist",
            43: "Epic Expresser",
            44: "Godlike Gabber",
            45: "🎭 Supreme Socializer",
            46: "Omnipresent Orator",
            47: "Divine Discussant",
            48: "Celestial Chatterbox",
            49: "Transcendental Talker",
            50: "🏅 DISCORD DEITY - Touch Grass Tier"
        }
        # Pour les niveaux 11 et plus
        self.grandmaster_level = 11
        
        # Define milestone levels with massive requirement jumps
        self.milestone_levels = {15, 20, 25, 30, 35, 40, 45, 50}
        self.milestone_multipliers = {
            15: 3.0,   # Triple requirement
            20: 2.5,   # 2.5x requirement  
            25: 2.8,   # 2.8x requirement
            30: 3.2,   # 3.2x requirement
            35: 3.5,   # 3.5x requirement
            40: 4.0,   # Quadruple requirement
            45: 4.5,   # 4.5x requirement
            50: 5.0    # Quintuple requirement for max level
        }
        
        # Dictionnaire pour stocker les canaux de level up par serveur
        self.level_up_channels = {
            "797781758841847808": 1104041737850196019,
            "1289627804211609640": 1336777782952198274,
            "1145431991420989593": 1189851053718507583
        }
        # Charger la configuration des rôles depuis le fichier
        self.level_roles = self.load_level_roles()

    def get_level_description(self, level):
        """Retourne la description d'un niveau"""
        return self.level_descriptions.get(level, f"Beyond Level {level} - You've gone too far!")

    def calculate_words_for_level(self, level):
        """Calculate words needed for a specific level (new milestone system)"""
        if level <= 1:
            return self.base_words_per_level
        
        # Base calculation for levels 1-10 (original system)
        if level <= 10:
            return math.ceil(self.base_words_per_level * (self.xp_multiplier ** (level - 1)))
        
        # Special calculation for levels 11+ with milestone system
        if level <= 14:
            # Levels 11-14: Continue exponential growth but slower
            return math.ceil(self.base_words_per_level * (self.xp_multiplier ** 9) * (1.3 ** (level - 10)))
        
        # Milestone levels with massive jumps
        if level in self.milestone_levels:
            previous_level_words = self.calculate_words_for_level(level - 1)
            multiplier = self.milestone_multipliers[level]
            return math.ceil(previous_level_words * multiplier)
        
        # Non-milestone levels after 15
        if level > 14:
            # Find the last milestone
            last_milestone = max([m for m in self.milestone_levels if m < level])
            levels_since_milestone = level - last_milestone
            milestone_words = self.calculate_words_for_level(last_milestone)
            
            # Gradual increase between milestones
            return math.ceil(milestone_words * (1.4 ** levels_since_milestone))
        
        return self.base_words_per_level

    def load_xp_data(self):
        if os.path.exists("xp_data.json"):
            try:
                with open("xp_data.json", "r") as f:
                    data = json.load(f)
                print("XP data loaded successfully.")
                return data
            except Exception as e:
                print(f"Error loading XP data: {e}")
                return {}
        return {}

    def save_xp_data(self):
        try:
            with open("xp_data.json", "w") as f:
                json.dump(self.xp_data, f, indent=4)
        except Exception as e:
            print(f"Error saving XP data: {e}")

    def load_level_roles(self):
        """Load role configuration from file"""
        if os.path.exists("level_roles.json"):
            try:
                with open("level_roles.json", "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading role config: {e}")
        return {}

    def count_words(self, message_content):
        """Count words in a message (filter spam)"""
        # Clean content (remove mentions, emojis, URLs)
        clean_content = re.sub(r'<[@#:][^>]*>', '', message_content)  # Discord mentions and emojis
        clean_content = re.sub(r'https?://\S+', '', clean_content)  # URLs
        clean_content = re.sub(r'[^\w\s]', ' ', clean_content)  # Punctuation
        
        # Count unique words (avoid spam repetition)
        words = clean_content.lower().split()
        unique_words = set(words)
        
        # Return word count, but limited
        word_count = len(unique_words)
        return min(max(word_count, 0), self.max_words_per_message)

    def calculate_words_needed_for_level(self, target_level):
        """Calculate total words needed to reach a level"""
        if target_level <= 1:
            return 0
        
        total_words = 0
        for level in range(1, target_level):
            words_for_this_level = self.calculate_words_for_level(level)
            total_words += words_for_this_level
        
        return total_words

    def calculate_level_from_words(self, total_words):
        """Calculate level based on total words (with level cap)"""
        if total_words <= 0:
            return 1
        
        level = 1
        words_used = 0
        
        while level < self.max_level:
            words_needed_for_next = self.calculate_words_for_level(level)
            if words_used + words_needed_for_next > total_words:
                break
            words_used += words_needed_for_next
            level += 1
        
        return min(level, self.max_level)

    def get_progress_info(self, total_words):
        """Return progression information for a user"""
        current_level = self.calculate_level_from_words(total_words)
        words_used_for_current_levels = self.calculate_words_needed_for_level(current_level)
        
        # Handle max level case
        if current_level >= self.max_level:
            return {
                'level': current_level,
                'words_in_current_level': total_words - words_used_for_current_levels,
                'words_needed_for_next': 0,
                'words_remaining': 0,
                'progress_percentage': 100.0,
                'is_max_level': True
            }
        
        words_needed_for_next_level = self.calculate_words_for_level(current_level)
        words_progress_in_current_level = total_words - words_used_for_current_levels
        words_remaining = words_needed_for_next_level - words_progress_in_current_level
        
        return {
            'level': current_level,
            'words_in_current_level': words_progress_in_current_level,
            'words_needed_for_next': words_needed_for_next_level,
            'words_remaining': max(0, words_remaining),
            'progress_percentage': (words_progress_in_current_level / words_needed_for_next_level) * 100,
            'is_max_level': False
        }

    async def add_words(self, user_id, guild_id, word_count):
        """Add words to user's counter"""
        if word_count < self.min_words_per_message:
            return  # Don't count messages that are too short
        
        server_id = str(guild_id)
        user_id = str(user_id)

        # Initialize data structure if it doesn't exist
        if server_id not in self.xp_data:
            self.xp_data[server_id] = {}

        # Default data structure for a new user
        default_data = {
            "total_words": 0,
            "level": 1,
            "messages": 0  # Keep for compatibility
        }

        # Initialize or retrieve user data
        if user_id not in self.xp_data[server_id]:
            self.xp_data[server_id][user_id] = default_data.copy()
        else:
            # CORRECTION: Vérifier et ajouter les clés manquantes pour les anciens utilisateurs
            user_data = self.xp_data[server_id][user_id]
            if "total_words" not in user_data:
                user_data["total_words"] = 0
            if "level" not in user_data:
                user_data["level"] = 1
            if "messages" not in user_data:
                user_data["messages"] = 0

        # Add words and increment messages
        self.xp_data[server_id][user_id]["total_words"] += word_count
        self.xp_data[server_id][user_id]["messages"] = self.xp_data[server_id][user_id].get("messages", 0) + 1
        
        total_words = self.xp_data[server_id][user_id]["total_words"]
        current_level = self.xp_data[server_id][user_id]["level"]
        
        # Calculate new level
        new_level = self.calculate_level_from_words(total_words)
        
        # If level changed, update it
        if new_level != current_level:
            self.xp_data[server_id][user_id]["level"] = new_level
            # Notify only if level increased
            if new_level > current_level:
                await self.notify_level_up(user_id, server_id, new_level)

        self.save_xp_data()

    async def update_user_roles(self, user_id, guild_id, new_level):
        """Update user roles based on their level"""
        try:
            guild = self.bot.get_guild(int(guild_id))
            if not guild:
                return
                
            member = guild.get_member(int(user_id))
            if not member:
                return
                
            server_roles = self.level_roles.get(str(guild_id), {})
            if not server_roles:
                return
                
            # Find all level roles the user should have
            roles_to_add = []
            roles_to_remove = []
            
            for level_req, role_id in server_roles.items():
                role = guild.get_role(int(role_id))
                if not role:
                    continue
                    
                if new_level >= int(level_req):
                    # User should have this role
                    if role not in member.roles:
                        roles_to_add.append(role)
                else:
                    # User should not have this role
                    if role in member.roles:
                        roles_to_remove.append(role)
            
            # Add new roles
            if roles_to_add:
                await member.add_roles(*roles_to_add, reason="Level reached")
                print(f"[XP] Roles added to {member.name}: {[r.name for r in roles_to_add]}")
                
            # Remove old roles
            if roles_to_remove:
                await member.remove_roles(*roles_to_remove, reason="Insufficient level")
                print(f"[XP] Roles removed from {member.name}: {[r.name for r in roles_to_remove]}")
                
        except Exception as e:
            print(f"[XP] Error updating roles: {e}")

    async def notify_level_up(self, user_id, server_id, new_level):
        try:
            # Update roles
            await self.update_user_roles(user_id, server_id, new_level)
            
            channel_id = self.level_up_channels.get(server_id)
            if not channel_id:
                return

            channel = self.bot.get_channel(channel_id)
            if not channel:
                return

            user = await self.bot.fetch_user(int(user_id))
            if not user:
                return

            level_description = self.get_level_description(new_level)
            
            # Special announcement for level 50 (max level)
            if new_level == 50:
                embed = discord.Embed(
                    title="🎉🏆 LEGENDARY ACHIEVEMENT UNLOCKED! 🏆🎉",
                    description=f"**{user.mention} has officially reached the MAXIMUM LEVEL 50!**\n\n"
                               f"🎭 **{level_description}** 🎭\n\n"
                               f"💬 *\"Congratulations! You've mastered the art of Discord. "
                               f"Maybe it's time to get a hobby outside of Discord? Just kidding... "
                               f"or are we? 😏 You absolute legend!\"*\n\n"
                               f"🌟 **You have achieved digital immortality!** 🌟",
                    color=0xFF6B35  # Bright orange/red for maximum impact
                )
                embed.set_thumbnail(url=user.display_avatar.url)
                embed.add_field(name="🏅 Status", value="**DISCORD DEITY**", inline=True)
                embed.add_field(name="🎯 Achievement", value="**TOUCH GRASS TIER**", inline=True)
                embed.add_field(name="💎 Rarity", value="**MYTHICAL**", inline=True)
                embed.set_footer(text="🎮 Game over? More like game mastered! 🎮")
                
                # Send the special announcement
                await channel.send("@everyone", embed=embed)
                return
            
            # Special handling for milestone levels
            if new_level in self.milestone_levels:
                embed = discord.Embed(
                    title="🎯 MILESTONE ACHIEVED!",
                    description=f"{user.mention} has reached the prestigious **Level {new_level}**!\n"
                               f"🏆 **{level_description}** 🏆\n\n"
                               f"*This is a major milestone! The journey ahead becomes even more challenging...*",
                    color=discord.Color.purple()
                )
                embed.set_thumbnail(url=user.display_avatar.url)
                
                # Calculate next milestone or max level
                next_milestone = min([m for m in self.milestone_levels if m > new_level], default=self.max_level)
                if next_milestone < self.max_level:
                    embed.add_field(
                        name="🎯 Next Milestone", 
                        value=f"Level {next_milestone}", 
                        inline=True
                    )
                else:
                    embed.add_field(
                        name="🏁 Final Goal", 
                        value=f"Max Level {self.max_level}", 
                        inline=True
                    )
                
                embed.add_field(
                    name="⚡ Challenge Level", 
                    value="**EXTREME**" if new_level >= 40 else "**HIGH**" if new_level >= 25 else "**MODERATE**", 
                    inline=True
                )
                
            else:
                # Regular level up
                words_for_next = self.calculate_words_for_level(new_level)
                embed = discord.Embed(
                    title="🎉 Level Up!",
                    description=f"{user.mention} has reached level {new_level}!\n"
                               f"**{level_description}**\n"
                               f"Next level requires {words_for_next:,} more words!",
                    color=discord.Color.gold()
                )
                embed.set_thumbnail(url=user.display_avatar.url)

            await channel.send(embed=embed)

        except Exception as e:
            print(f"[XP] Notification error: {e}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or not message.guild:
            return
        
        # Count words in the message
        word_count = self.count_words(message.content)
        if word_count > 0:
            await self.add_words(message.author.id, message.guild.id, word_count)

    @app_commands.command(
        name="rank",
        description="Display your rank or another user's rank and progress"
    )
    @app_commands.describe(
        user="The user to check (leave empty to see your own rank)"
    )
    async def rank(self, interaction: discord.Interaction, user: discord.Member = None):
        server_id = str(interaction.guild_id)
        target_user = user or interaction.user
        user_id = str(target_user.id)

        # Initialize default data
        default_data = {
            "total_words": 0,
            "level": 1,
            "messages": 0
        }

        # Get user data or use default
        if server_id not in self.xp_data:
            self.xp_data[server_id] = {}
        
        data = self.xp_data[server_id].get(user_id, default_data.copy())
        
        # CORRECTION: S'assurer que toutes les clés existent
        total_words = data.get("total_words", 0)
        messages = data.get("messages", 0)
        level = data.get("level", 1)
        
        # Si l'utilisateur existe mais n'a pas total_words, le migrer
        if user_id in self.xp_data[server_id] and "total_words" not in data:
            # Estimation basée sur les anciens messages
            estimated_words = messages * 5  # 5 mots par message en moyenne
            self.xp_data[server_id][user_id]["total_words"] = estimated_words
            total_words = estimated_words
            # Recalculer le niveau
            new_level = self.calculate_level_from_words(total_words)
            self.xp_data[server_id][user_id]["level"] = new_level
            level = new_level
            self.save_xp_data()
        
        # Calculate progression information
        progress_info = self.get_progress_info(total_words)
        level_description = self.get_level_description(progress_info['level'])

        embed = discord.Embed(
            title=f"📊 Statistics for {target_user.display_name}",
            color=target_user.color
        )
        embed.set_thumbnail(url=target_user.display_avatar.url)
        
        # Find user rank
        all_users = [(uid, udata) for uid, udata in self.xp_data[server_id].items()]
        sorted_users = sorted(all_users, key=lambda x: x[1].get("total_words", 0), reverse=True)
        rank = next((index + 1 for index, (uid, _) in enumerate(sorted_users) if uid == user_id), 0)
        
        embed.add_field(name="Rank", value=f"```#{rank}```", inline=True)
        embed.add_field(name="Level", value=f"```{progress_info['level']}```", inline=True)
        embed.add_field(name="Title", value=f"```{level_description}```", inline=True)
        embed.add_field(name="Total Words", value=f"```{total_words:,}```", inline=True)
        embed.add_field(name="Messages", value=f"```{messages:,}```", inline=True)
        embed.add_field(name="Avg Words/Message", value=f"```{total_words/max(messages,1):.1f}```", inline=True)
        
        # Special handling for max level
        if progress_info.get('is_max_level', False):
            embed.add_field(
                name="🏆 MAX LEVEL ACHIEVED! 🏆",
                value="🎭 **DISCORD DEITY STATUS** 🎭\n"
                      "👑 You have conquered the leaderboard! 👑\n"
                      "🌟 Digital immortality achieved! 🌟",
                inline=False
            )
        else:
            # Progress bar for non-max level users
            progress = progress_info['progress_percentage'] / 100
            bar_length = 15
            filled = int(progress * bar_length)
            bar = "█" * filled + "░" * (bar_length - filled)
            
            # Check if next level is a milestone
            next_level = progress_info['level'] + 1
            milestone_indicator = ""
            if next_level in self.milestone_levels:
                milestone_indicator = "\n🎯 **MILESTONE AHEAD!** - Massive requirement jump!"
            
            embed.add_field(
                name="Next Level Progress",
                value=f"{bar} {progress_info['progress_percentage']:.1f}%\n"
                      f"{progress_info['words_in_current_level']:,}/{progress_info['words_needed_for_next']:,} words\n"
                      f"{progress_info['words_remaining']:,} words remaining{milestone_indicator}",
                inline=False
            )

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="leaderboard", description="Display server ranking")
    async def leaderboard(self, interaction: discord.Interaction):
        server_id = str(interaction.guild_id)
        
        if server_id not in self.xp_data:
            await interaction.response.send_message("No data for this server!", ephemeral=True)
            return

        # Filter and sort users by total words
        valid_users = []
        for user_id, data in self.xp_data[server_id].items():
            if isinstance(data, dict):
                total_words = data.get("total_words", 0)
                level = data.get("level", 1)
                valid_users.append((user_id, total_words, level))

        sorted_users = sorted(valid_users, key=lambda x: x[1], reverse=True)[:10]

        embed = discord.Embed(
            title=f"🏆 Leaderboard - {interaction.guild.name}",
            description="Based on total words written",
            color=discord.Color.gold()
        )

        if not sorted_users:
            embed.description = "No valid data to display"
        else:
            for rank, (user_id, total_words, level) in enumerate(sorted_users, 1):
                user = interaction.guild.get_member(int(user_id))
                if user:
                    level_description = self.get_level_description(level)
                    medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(rank, "")
                    embed.add_field(
                        name=f"{medal} #{rank} @{user.name}",  # Changé de user.mention à @{user.name}
                        value=f"Level {level} - {level_description}\n{total_words:,} words",
                        inline=False
                    )

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="resetxp", description="Reset a member's XP")
    @app_commands.checks.has_permissions(administrator=True)
    async def resetxp(self, interaction: discord.Interaction, member: discord.Member):
        server_id = str(interaction.guild_id)
        user_id = str(member.id)

        if server_id in self.xp_data and user_id in self.xp_data[server_id]:
            # Complete reset
            self.xp_data[server_id][user_id] = {
                "total_words": 0,
                "level": 1,
                "messages": 0
            }
            
            self.save_xp_data()
            
            # Update roles after reset
            await self.update_user_roles(user_id, server_id, 1)
            
            await interaction.response.send_message(
                f"The statistics and roles of {member.name} have been completely reset.",
                ephemeral=True
            )
        else:
            await interaction.response.send_message(
                f"{member.name} has no statistics to reset.",
                ephemeral=True
            )

    @app_commands.command(name="setwords", description="Set a member's total word count")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        member="The member to modify",
        words="The new total word count"
    )
    async def setwords(self, interaction: discord.Interaction, member: discord.Member, words: int):
        server_id = str(interaction.guild_id)
        user_id = str(member.id)
        
        # Validation
        if words < 0:
            await interaction.response.send_message("Word count cannot be negative!", ephemeral=True)
            return
        
        # Initialize structure if necessary
        if server_id not in self.xp_data:
            self.xp_data[server_id] = {}
        
        if user_id not in self.xp_data[server_id]:
            self.xp_data[server_id][user_id] = {"total_words": 0, "level": 1, "messages": 0}
        
        # Calculate old and new level
        old_level = self.xp_data[server_id][user_id].get("level", 1)
        new_level = self.calculate_level_from_words(words)
        
        # Update data
        self.xp_data[server_id][user_id]["total_words"] = words
        self.xp_data[server_id][user_id]["level"] = new_level
        
        self.save_xp_data()
        
        # Update roles
        await self.update_user_roles(user_id, server_id, new_level)
        
        old_description = self.get_level_description(old_level)
        new_description = self.get_level_description(new_level)
        
        await interaction.response.send_message(
            f"✅ {member.name}'s words set to {words:,}\n"
            f"Level {old_level} ({old_description}) → {new_level} ({new_description})",
            ephemeral=True
        )

    @app_commands.command(name="recalculatelevels", description="Recalculate all users' levels based on their words")
    @app_commands.checks.has_permissions(administrator=True)
    async def recalculatelevels(self, interaction: discord.Interaction):
        await interaction.response.defer()
        
        server_id = str(interaction.guild_id)
        if server_id not in self.xp_data:
            await interaction.followup.send("No XP data for this server!", ephemeral=True)
            return
        
        updated_count = 0
        level_changes = []
        
        for user_id, data in self.xp_data[server_id].items():
            if isinstance(data, dict):
                total_words = data.get("total_words", 0)
                old_level = data.get("level", 1)
                new_level = self.calculate_level_from_words(total_words)
                
                if old_level != new_level:
                    data["level"] = new_level
                    # Update roles
                    await self.update_user_roles(user_id, server_id, new_level)
                    
                    # Get username for report
                    member = interaction.guild.get_member(int(user_id))
                    username = member.display_name if member else f"User {user_id}"
                    old_desc = self.get_level_description(old_level)
                    new_desc = self.get_level_description(new_level)
                    level_changes.append(f"{username}: {old_level} ({old_desc}) → {new_level} ({new_desc})")
                    
                updated_count += 1
        
        self.save_xp_data()
        
        response = f"✅ Recalculated levels for {updated_count} users."
        if level_changes:
            response += f"\n\n**Level changes:**\n" + "\n".join(level_changes[:10])
            if len(level_changes) > 10:
                response += f"\n... and {len(level_changes) - 10} more"
        
        await interaction.followup.send(response, ephemeral=True)

    @app_commands.command(name="xpinfo", description="Show information about the XP system")
    async def xpinfo(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="📈 XP System Information - Milestone Edition",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="How it works",
            value=f"• XP is based on **words**, not messages\n"
                  f"• Minimum {self.min_words_per_message} words per message to count\n"
                  f"• Maximum {self.max_words_per_message} words counted per message\n"
                  f"• Spam and repetition are filtered out\n"
                  f"• **Maximum level: {self.max_level}**",
            inline=False
        )
        
        embed.add_field(
            name="🎯 Milestone System",
            value="**MAJOR REQUIREMENT JUMPS AT:**\n"
                  f"• Level 15: {self.milestone_multipliers[15]}x multiplier\n"
                  f"• Level 20: {self.milestone_multipliers[20]}x multiplier\n"
                  f"• Level 25: {self.milestone_multipliers[25]}x multiplier\n"
                  f"• Level 30: {self.milestone_multipliers[30]}x multiplier\n"
                  f"• Level 35: {self.milestone_multipliers[35]}x multiplier\n"
                  f"• Level 40: {self.milestone_multipliers[40]}x multiplier (QUAD!)\n"
                  f"• Level 45: {self.milestone_multipliers[45]}x multiplier\n"
                  f"• Level 50: {self.milestone_multipliers[50]}x multiplier (FINAL!)",
            inline=False
        )
        
        # Calculate examples for key levels including milestones
        examples = []
        key_levels = [1, 5, 10, 11, 14, 15, 20, 25, 30, 40, 50]
        for level in key_levels:
            if level <= self.max_level:
                total_words = self.calculate_words_needed_for_level(level + 1) if level < self.max_level else self.calculate_words_needed_for_level(level)
                words_for_level = self.calculate_words_for_level(level)
                description = self.get_level_description(level)
                milestone_marker = " 🎯" if level in self.milestone_levels else ""
                examples.append(f"Level {level}{milestone_marker}: {words_for_level:,} words ({description})")
        
        embed.add_field(
            name="🏆 Level Requirements (Words per Level)",
            value="\n".join(examples[:8]),  # First 8 examples
            inline=False
        )
        
        embed.add_field(
            name="🚀 High-Level Examples",
            value="\n".join(examples[8:]),  # Remaining examples
            inline=False
        )
        
        embed.add_field(
            name="🎭 Special Features",
            value="• **Milestone Levels**: Massive difficulty spikes!\n"
                  "• **Level 50 Achievement**: Epic announcement\n"
                  "• **Humorous Titles**: From Bronze Beater to Discord Deity\n"
                  "• **Progressive Challenge**: Gets harder as you climb\n"
                  "• **Touch Grass Tier**: The ultimate Discord achievement",
            inline=False
        )
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="milestones", description="Show all milestone levels and their requirements")
    async def milestones(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🎯 Milestone Progression Chart",
            description="The journey to Discord Deity status...",
            color=discord.Color.purple()
        )
        
        # Group milestones by difficulty tier
        tiers = {
            "🥉 **MODERATE TIER**": [15, 20],
            "🥈 **HIGH TIER**": [25, 30, 35], 
            "🥇 **EXTREME TIER**": [40, 45],
            "🏆 **LEGENDARY TIER**": [50]
        }
        
        for tier_name, levels in tiers.items():
            tier_info = []
            for level in levels:
                words_needed = self.calculate_words_for_level(level)
                total_words = self.calculate_words_needed_for_level(level)
                title = self.get_level_description(level)
                multiplier = self.milestone_multipliers.get(level, 1.0)
                
                if level == 50:
                    tier_info.append(f"**Level {level}** - {title}\n"
                                   f"   └ {words_needed:,} words ({multiplier}x) - MAX LEVEL!")
                else:
                    tier_info.append(f"**Level {level}** - {title}\n"
                                   f"   └ {words_needed:,} words ({multiplier}x multiplier)")
            
            embed.add_field(
                name=tier_name,
                value="\n".join(tier_info),
                inline=False
            )
        
        embed.add_field(
            name="💡 Pro Tips",
            value="• Each milestone multiplies the previous level's requirement\n"
                  "• Level 15 is your first major challenge - prepare!\n"
                  "• Level 40+ is where legends are born\n"
                  "• Level 50 grants you **Discord Deity** status",
            inline=False
        )
        
        embed.set_footer(text="🎮 The grind is real, but the glory is eternal! 🎮")
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="setlevelup", description="Configure the level notification channel")
    @app_commands.checks.has_permissions(administrator=True)
    async def setlevelup(self, interaction: discord.Interaction, channel: discord.TextChannel = None):
        channel = channel or interaction.channel
        server_id = str(interaction.guild_id)
        
        self.level_up_channels[server_id] = channel.id
        await interaction.response.send_message(
            f"Level notification channel set to {channel.mention}",
            ephemeral=True
        )

    @app_commands.command(name="updateallroles", description="Update all users' roles based on their level")
    @app_commands.checks.has_permissions(administrator=True)
    async def updateallroles(self, interaction: discord.Interaction):
        await interaction.response.defer()
        
        server_id = str(interaction.guild_id)
        if server_id not in self.xp_data:
            await interaction.followup.send("No XP data for this server!", ephemeral=True)
            return
        
        updated_count = 0
        for user_id, data in self.xp_data[server_id].items():
            if isinstance(data, dict) and "level" in data:
                level = data["level"]
                await self.update_user_roles(user_id, server_id, level)
                updated_count += 1
        
        await interaction.followup.send(
            f"✅ Updated roles for {updated_count} users based on their current level.",
            ephemeral=True
        )

    @app_commands.command(name="setlevelrole", description="Configure a role for a specific level")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        level="The level required for this role",
        role="The role to assign at this level"
    )
    async def setlevelrole(self, interaction: discord.Interaction, level: int, role: discord.Role):
        server_id = str(interaction.guild_id)
        
        if server_id not in self.level_roles:
            self.level_roles[server_id] = {}
        
        self.level_roles[server_id][level] = role.id
        
        # Save configuration
        try:
            with open("level_roles.json", "w") as f:
                json.dump(self.level_roles, f, indent=4)
        except Exception as e:
            print(f"Error saving role config: {e}")
        
        await interaction.response.send_message(
            f"✅ Role {role.mention} configured for level {level}",
            ephemeral=True
        )

    @app_commands.command(name="migratedata", description="Migrate old XP data to new format")
    @app_commands.checks.has_permissions(administrator=True)
    async def migratedata(self, interaction: discord.Interaction):
        await interaction.response.defer()
        
        server_id = str(interaction.guild_id)
        if server_id not in self.xp_data:
            await interaction.followup.send("No XP data for this server!", ephemeral=True)
            return
        
        migrated_count = 0
        
        for user_id, data in self.xp_data[server_id].items():
            if isinstance(data, dict):
                # Vérifier et ajouter les clés manquantes
                updated = False
                
                if "total_words" not in data:
                    # Convertir les anciens messages en mots (estimation)
                    old_messages = data.get("messages", 0)
                    # Estimation : 5 mots par message en moyenne
                    estimated_words = old_messages * 5
                    data["total_words"] = estimated_words
                    updated = True
                
                if "level" not in data:
                    # Recalculer le niveau basé sur les mots
                    total_words = data.get("total_words", 0)
                    data["level"] = self.calculate_level_from_words(total_words)
                    updated = True
                
                if "messages" not in data:
                    data["messages"] = 0
                    updated = True
                
                if updated:
                    migrated_count += 1
        
        if migrated_count > 0:
            self.save_xp_data()
            await interaction.followup.send(
                f"✅ Migrated {migrated_count} users to the new XP format.\n"
                f"Old messages were converted to words (5 words per message average).",
                ephemeral=True
            )
        else:
            await interaction.followup.send(
                "✅ All users are already using the new XP format.",
                ephemeral=True
            )

async def setup(bot):
    await bot.add_cog(XP(bot))