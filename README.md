# 🤖 Simple Bot Discord

<div align="center">

[![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/your-invite)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-6.2.0-blue?style=for-the-badge)]()

*Un bot Discord moderne et polyvalent avec système d'XP, commandes personnalisées, modération et bien plus !*

</div>

---

## 📋 Table des Matières

- [✨ Fonctionnalités Principales](#-fonctionnalités-principales)
- [🚀 Installation Rapide](#-installation-rapide)
- [⚙️ Configuration](#️-configuration)
- [📚 Modules et Commandes](#-modules-et-commandes)
- [🎯 Guide d'Utilisation](#-guide-dutilisation)
- [🔧 Configuration Avancée](#-configuration-avancée)
- [🤝 Contribution](#-contribution)
- [📄 Licence](#-licence)

---

## ✨ Fonctionnalités Principales

### 🏆 **Système d'Expérience et Niveaux**
- **Progression automatique** : Gain d'XP par message envoyé
- **Système de niveaux** avec 50+ paliers
- **Rôles automatiques** par niveau
- **Leaderboard interactif** avec classement
- **Commandes administrateur** pour gérer l'XP

### 🎮 **Commandes Personnalisées**
- **Créateur de commandes** intuitif avec interface interactive
- **Commandes globales et par serveur**
- **Système de recherche** et filtrage avancé
- **Export des commandes** en fichier Markdown
- **Gestion complète** via interface moderne

### 🔨 **Modération Avancée**
- **Kick/Ban** avec raisons et durées
- **Mute temporaire** avec gestion automatique
- **Système d'avertissements** avec historique
- **Nettoyage de messages** en masse
- **Logs de modération** détaillés

### 🎉 **Système de Giveaways**
- **Création facile** de concours
- **Gestion automatique** des tirages
- **Système de réactions** pour participer
- **Notifications** automatiques des résultats

### 🎲 **Commandes Fun**
- **Pierre-Papier-Ciseaux** interactif
- **Pile ou Face** avec boutons
- **Générateur de faits** aléatoires
- **Blagues** et divertissement

### 🎵 **Salon Vocal Temporaire**
- **Création automatique** de salons vocaux
- **Gestion des permissions** personnalisée
- **Suppression automatique** quand vide

### 📊 **Système de Votes**
- **Création de sondages** interactifs
- **Modification** des votes existants
- **Résultats** en temps réel

### 🔍 **Informations et Utilitaires**
- **Informations serveur** détaillées
- **Profil utilisateur** complet
- **Informations bot** et statistiques
- **Menu contextuel** pour actions rapides

---

## 🚀 Installation Rapide

### 📋 Prérequis
- **Python 3.8+** installé
- **Bot Discord** créé sur le [Discord Developer Portal](https://discord.com/developers/applications)
- **Git** (optionnel)

### 📦 Installation

1. **Cloner le repository**
```bash
git clone https://github.com/Axekinn/Simple-Bot-Discord.git
cd Simple-Bot-Discord
```

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

3. **Configuration des fichiers**
```bash
# Copier les fichiers d'exemple
cp .env.example .env
cp config.json.example config.json
cp commands.json.example commands.json
cp xp_data.json.example xp_data.json
cp giveaways.json.example giveaways.json
cp role_reactions.json.example role_reactions.json
```

4. **Configurer le token**
```bash
# Éditer le fichier .env
TOKEN=VOTRE_TOKEN_BOT_DISCORD
```

5. **Lancer le bot**
```bash
python bot.py
```

---

## ⚙️ Configuration

### 🔑 Fichier `.env`
```env
TOKEN=VOTRE_TOKEN_BOT_DISCORD
```

### 📝 Fichier `config.json`
```json
{
  "prefix": "!",
  "owner_id": "VOTRE_ID_DISCORD",
  "description": "Un bot Discord simple et puissant",
  "website": "https://votre-site.com/",
  "discord_invite": "https://discord.gg/votre-invite",
  "github": "https://github.com/votre-username/votre-repo"
}
```

---

## 📚 Modules et Commandes

### 🏆 **Module XP (Experience)**

| Commande | Description | Permissions |
|----------|-------------|-------------|
| `/xp [membre]` | Affiche l'XP et le niveau d'un membre | Tous |
| `/leaderboard` | Classement du serveur par niveau | Tous |
| `/resetxp <membre>` | Remet à zéro l'XP d'un membre | Administrateur |
| `/setwords <membre> <mots>` | Définit le nombre de mots total | Administrateur |
| `/recalculatelevels` | Recalcule tous les niveaux | Administrateur |
| `/xpinfo` | Informations sur le système d'XP | Tous |
| `/milestones` | Affiche tous les paliers de niveaux | Tous |
| `/setlevelup [salon]` | Configure le salon de notifications | Administrateur |
| `/setlevelrole <niveau> <rôle>` | Assigne un rôle à un niveau | Administrateur |
| `/updateallroles` | Met à jour tous les rôles par niveau | Administrateur |

**🎯 Système de Progression**
- **Gain d'XP** : 1 XP par mot écrit dans un message
- **Cooldown** : 1 minute entre les gains d'XP
- **Formule de niveau** : `niveau = floor(sqrt(mots_total / 100))`
- **Niveaux maximum** : 50+ paliers disponibles

### 🛠️ **Module Commandes Personnalisées**

| Commande | Description | Permissions |
|----------|-------------|-------------|
| `/create_command` | Interface de création de commandes | Administrateur |
| `/commands [scope] [filter]` | Navigateur de commandes interactif | Tous |

**🎨 Fonctionnalités Avancées**
- **Interface moderne** avec boutons et sélecteurs
- **Recherche avancée** par nom, description ou contenu
- **Export Markdown** des commandes
- **Gestion par catégories** (globales/serveur)
- **Système de pagination** intelligent

### 🔨 **Module Modération**

| Commande | Description | Permissions |
|----------|-------------|-------------|
| `/kick <utilisateur> [raison]` | Expulse un membre | Kick Members |
| `/ban <utilisateur> [raison]` | Bannit un membre | Ban Members |
| `/unban <utilisateur>` | Débannit un membre | Ban Members |
| `/timeout <utilisateur> <durée>` | Met en sourdine temporaire | Moderate Members |
| `/untimeout <utilisateur>` | Retire la sourdine | Moderate Members |
| `/purge <nombre>` | Supprime des messages | Manage Messages |
| `/warn <utilisateur> [raison]` | Avertit un membre | Kick Members |

**⚡ Fonctionnalités**
- **Vérifications de sécurité** automatiques
- **Logs détaillés** des actions
- **Gestion des erreurs** complète
- **Protection administrateur** intégrée

### 🎉 **Module Giveaways**

| Commande | Description | Permissions |
|----------|-------------|-------------|
| `/giveaway <durée> <prix>` | Crée un nouveau giveaway | Manage Messages |
| `/gend <message_id>` | Termine un giveaway | Manage Messages |
| `/greroll <message_id>` | Relance le tirage | Manage Messages |

**🎁 Fonctionnalités**
- **Gestion automatique** des tirages
- **Interface avec réactions** 🎉
- **Notifications** des gagnants
- **Sauvegarde persistante** des données

### 🎮 **Module Fun**

| Commande | Description | Permissions |
|----------|-------------|-------------|
| `/randomfact` | Fait aléatoire en anglais | Tous |
| `/coinflip` | Pile ou face interactif | Tous |
| `/rps` | Pierre-papier-ciseaux | Tous |

**🎯 Jeux Interactifs**
- **Interface avec boutons** Discord
- **Animations** et réactions
- **Système de scores** (à venir)

### 🔍 **Module Informations**

| Commande | Description | Permissions |
|----------|-------------|-------------|
| `/help` | Liste des commandes disponibles | Tous |
| `/botinfo` | Informations détaillées sur le bot | Tous |
| `/serverinfo` | Informations sur le serveur | Tous |
| `/whois <membre>` | Profil détaillé d'un membre | Tous |
| `/ping` | Latence du bot | Tous |
| `/invite` | Lien d'invitation du bot | Tous |

### 🎵 **Module Salon Vocal**

| Commande | Description | Permissions |
|----------|-------------|-------------|
| `/voice setup <salon>` | Configure le système vocal | Administrator |

**🔊 Fonctionnalités**
- **Création automatique** de salons temporaires
- **Permissions personnalisées** par utilisateur
- **Suppression automatique** à la déconnexion

### 📊 **Module Votes**

| Commande | Description | Permissions |
|----------|-------------|-------------|
| `/vote_create <question>` | Crée un sondage | Manage Messages |
| `/vote_edit <message_id>` | Modifie un vote existant | Manage Messages |

### 🎭 **Module Rôles par Réaction**

**Configuration** via fichier `role_reactions.json`
- **Attribution automatique** de rôles
- **Interface avec réactions** personnalisées
- **Gestion multi-messages**

---

## 🎯 Guide d'Utilisation

### 🏆 **Mise en Place du Système XP**

1. **Configuration initiale**
```bash
/setlevelup #niveau-up
```

2. **Attribution de rôles par niveau**
```bash
/setlevelrole niveau:5 rôle:@Membre Actif
/setlevelrole niveau:10 rôle:@Contributeur
/setlevelrole niveau:25 rôle:@Expert
```

3. **Vérification du système**
```bash
/milestones  # Voir tous les paliers
/xpinfo      # Informations détaillées
```

### 🛠️ **Création de Commandes Personnalisées**

1. **Lancer l'interface**
```bash
/create_command
```

2. **Suivre l'assistant interactif**
   - Choisir le scope (global/serveur)
   - Définir le nom de la commande
   - Ajouter la description
   - Configurer la réponse

3. **Tester et gérer**
```bash
/commands scope:server  # Voir les commandes du serveur
```

### 🔨 **Configuration de la Modération**

1. **Permissions recommandées**
   - Kick Members
   - Ban Members
   - Manage Messages
   - Moderate Members

2. **Utilisation type**
```bash
/warn @utilisateur raison:Spam
/timeout @utilisateur durée:1h raison:Comportement inapproprié
/purge nombre:10
```

---

## 🔧 Configuration Avancée

### 🗄️ **Base de Données**

Le bot utilise SQLite pour stocker :
- **Données d'XP** : `xp_data.json`
- **Commandes** : `commands.json`
- **Giveaways** : `giveaways.json`
- **Réactions** : `role_reactions.json`

### 📁 **Structure des Fichiers**

```
Simple-Bot-Discord/
├── bot.py                 # Fichier principal
├── requirements.txt       # Dépendances Python
├── .env                  # Variables d'environnement
├── config.json           # Configuration du bot
├── commands.json         # Commandes personnalisées
├── xp_data.json         # Données d'expérience
├── giveaways.json       # Données des giveaways
├── role_reactions.json  # Configuration rôles/réactions
├── discord.log          # Logs du bot
├── database/            # Base de données SQLite
│   ├── __init__.py
│   ├── database.db
│   └── schema.sql
└── cogs/                # Modules du bot
    ├── xp.py           # Système d'expérience
    ├── command_builder.py  # Commandes personnalisées
    ├── moderation.py   # Modération
    ├── giveaway.py     # Giveaways
    ├── fun.py          # Commandes fun
    ├── general.py      # Commandes générales
    ├── voice_creator.py # Salons vocaux temporaires
    ├── vote.py         # Système de votes
    ├── whois.py        # Informations utilisateur
    ├── role_reaction.py # Rôles par réaction
    └── owner.py        # Commandes propriétaire
```

### 🔐 **Sécurité**

- ✅ **Token sécurisé** dans `.env`
- ✅ **Fichiers sensibles** dans `.gitignore`
- ✅ **Vérifications de permissions** sur toutes les commandes
- ✅ **Protection contre** les boucles infinies
- ✅ **Gestion d'erreurs** complète

### 🚀 **Performance**

- **Base de données locale** SQLite pour rapidité
- **Cache en mémoire** pour les données fréquentes
- **Chargement asynchrone** des modules
- **Optimisation** des requêtes Discord API

---

## 🔧 Personnalisation

### 🎨 **Modifier les Couleurs**
```python
# Dans chaque cog, modifier les couleurs d'embed
embed = discord.Embed(color=0x3498db)  # Bleu
embed = discord.Embed(color=0xe74c3c)  # Rouge
embed = discord.Embed(color=0x2ecc71)  # Vert
```

### 🏆 **Personnaliser le Système XP**
```python
# Dans cogs/xp.py, ligne ~50
XP_PER_WORD = 1           # XP gagné par mot
XP_COOLDOWN = 60          # Cooldown en secondes
LEVEL_FORMULA = lambda w: math.floor(math.sqrt(w / 100))
```

### 🎭 **Ajouter des Commandes**
```python
# Créer un nouveau fichier dans cogs/
# Suivre le template dans cogs/template.py
```

---

## 🛡️ Support et Dépannage

### ❓ **Problèmes Courants**

**Bot hors ligne ?**
- Vérifier le token dans `.env`
- Vérifier les permissions du bot
- Consulter `discord.log` pour les erreurs

**Commandes ne fonctionnent pas ?**
- Vérifier les permissions du bot
- Utiliser `/` pour les slash commands
- Vérifier la configuration des intents

**Système XP inactif ?**
- Vérifier les permissions `message_content`
- Vérifier que les intents sont activés
- Consulter les logs pour erreurs

### 📞 **Obtenir de l'Aide**

- 🐛 **Signaler un bug** : [Issues GitHub](https://github.com/Axekinn/Simple-Bot-Discord/issues)
- 💬 **Discord** : [Rejoindre le serveur](https://discord.gg/CUpf57y5Vg)
- 📧 **Email** : axekinn@proton.me

---

## 🤝 Contribution

Nous accueillons chaleureusement les contributions ! 

### 📝 **Comment Contribuer**

1. **Fork** le repository
2. **Créer** une branche feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** les changements (`git commit -m 'Add some AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. **Ouvrir** une Pull Request

### 🎯 **Ce qu'on recherche**

- 🐛 **Corrections de bugs**
- ✨ **Nouvelles fonctionnalités**
- 📚 **Amélioration de la documentation**
- 🎨 **Améliorations UI/UX**
- 🔧 **Optimisations de performance**

### 📋 **Guidelines**

- Suivre le style de code existant
- Tester toutes les nouvelles fonctionnalités
- Documenter le code avec des commentaires
- Respecter les conventions de nommage

---

## 🏆 Contributeurs

Un grand merci à tous les contributeurs qui ont aidé à améliorer ce bot !

<!-- Contributors section will be auto-generated -->

---

## 📊 Statistiques

- ⭐ **Fonctionnalités** : 50+ commandes
- 🔧 **Modules** : 12 cogs
- 🏆 **Système XP** : 50+ niveaux
- 🎮 **Jeux intégrés** : 3+
- 🔨 **Outils modération** : 8+

---

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 📈 Roadmap

### 🚀 **Version 7.0 (Prochaine)**
- [ ] 🎵 **Lecteur de musique** complet
- [ ] 📈 **Dashboard web** pour configuration
- [ ] 🎯 **Système de missions** et récompenses
- [ ] 🔔 **Notifications** personnalisées
- [ ] 📊 **Statistiques avancées** du serveur

### 🎯 **Version 7.1**
- [ ] 🎮 **Mini-jeux** multijoueurs
- [ ] 💰 **Économie virtuelle** avec magasin
- [ ] 🎭 **Rôles temporaires** automatiques
- [ ] 📱 **Application mobile** companion

### 🔮 **Futures Versions**
- [ ] 🤖 **IA** pour modération automatique
- [ ] 🌍 **Multi-langues** complet
- [ ] ☁️ **Cloud hosting** intégré
- [ ] 📊 **Analytics** avancées

---

## 🙏 Remerciements

- **Discord.py** - Pour l'excellente librairie
- **Krypton** - Pour le template de base
- **Communauté Discord** - Pour les tests et retours
- **Contributeurs** - Pour leurs améliorations

---

<div align="center">

**⭐ Si ce bot vous a aidé, n'hésitez pas à donner une étoile au projet ! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/Axekinn/Simple-Bot-Discord?style=social)](https://github.com/Axekinn/Simple-Bot-Discord/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Axekinn/Simple-Bot-Discord?style=social)](https://github.com/Axekinn/Simple-Bot-Discord/network)

---

*Made with ❤️ by [Axekinn](https://github.com/Axekinn)*

</div>
