# Shadow Bot 

## 🔨 Création du Bot
1) Rendez vous sur le [Developer Portal](https://discord.com/developer/applications) de discord
2) Créez un nouveau bot
3) Donnez lui toutes les permissions
4) Invitez le sur votre serveur
5) Placez le rôle du bot le plus haut dans la hiérarchie
6) Copiez son token

## 🔧 Installation du Bot
1) Téléchargez le Bot
2) Installez [Python](https://www.python.org)  <img align="center" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"  width="25" height="25">
3) Installez [PIP](https://pypi.org/project/pip/)
4) Installez les modules réquis a l'aide de la commande `pip install -r requirements.txt`
5) Lancez le bot avec le fichier `launch.py` ou `launch.bat`


## 📚 Documentation

### 📝 Informations Générales
Ce bot est développé en Python et créé a l'aide de l'API [discord-py-interactions](https://github.com/interactions-py/interactions.py) <img align="center" src="https://avatars.githubusercontent.com/u/98242689?s=200&v=4"  width="25" height="25">

Il est encore en développement et peut comporter des bugs. Si c'est le cas veuillez me contacter sur discord `ت⃟⃤ Shadow 🙃 | ψ#0817` ou en créant un `Pull Request`

### 🧰 La Configuration
dans le dossier du bot se trouve le fichier `config.json` sous cette forme:
```json
{
  "Token": "Le token de votre bot discord",
  "Commands Error": "Vous n'avez pas la permission d'executer cette commande !",
  "Mute Id": 944973307520909392,
  "Banned Words": ["discord.gg/","dsc.gg/","youtube.com/","youtu.be/"],
  "Welcome Channel Id": 1054327357265170473,
  "Welcome Default Role": 939981587796336680,
  "Log Channel Id": 1077203397863821322,
  "OpenAI API Key": "Votre clé d'API OpenAI",
  "Ticket Access Role Id": [1080766549440340058] 
}
```
Pour configurer correctement le bot, il suffit simplement de modifier les données écrites après les doubles points dans ce fichier JSON.
### Les commandes :

- `addrole` : permet aux administrateurs d'ajouter un rôle à un utilisateur
- `ask_gpt` : permet de poser une question à l'API de langage naturel GPT-3.5
- `avatar` : permet d'afficher l'avatar d'un utilisateur ou d'un bot
- `botinfo` : permet d'afficher des informations sur le bot
- `changelog` : permet d'afficher les modifications apportées au bot
- `changenick` : permet aux administrateurs de changer le surnom d'un utilisateur
- `delwarn` : permet de supprimer un avertissement donné à un utilisateur
- `embed` : permet d'envoyer un message sous forme d'embed
- `emojis` : permet d'afficher la liste des emojis du serveur
- `getwarn` : permet d'afficher les avertissements donnés à un utilisateur
- `imagine` : permet de créer une image grâce a l'API de Dall-E
- `info` : permet d'afficher des informations sur un utilisateur
- `mute` : permet de rendre muet un utilisateur
- `ping` : permet de vérifier le temps de réponse du bot
- `purge` : permet de supprimer plusieurs messages en même temps
- `rall` : permet générer un nombre aléatoire entre un interval donné
- `removerole` : permet de retirer un rôle à un utilisateur
- `roles` : permet d'afficher la liste des rôles du serveur
- `say` : permet de faire dire quelque chose au bot
- `serverinfo` : permet d'afficher des informations sur le serveur
- `ticket` : permet de créer un ticket pour une demande d'assistance
- `unmute` : permet de rendre la parole à un utilisateur rendu muet
- `warn` : permet de donner un avertissement à un utilisateur

Chaque commande dispose d'une syntaxe spécifique et peut prendre des arguments supplémentaires.
### 🎲 Autre
Ce bot possède également un système d'**anti-lien** / **anti-insultes** personalisable directement dans la `config`.


### 🚪 Mot De Fin
Merci d'utliser ce bot loin d'être parfait, mais qui fait quand même l'affaire.

**ShadowMikado**

### 🎉 Crédits
**@ShadowMikado**

**@TousMesPotesQuiDonnentLesIdées**
