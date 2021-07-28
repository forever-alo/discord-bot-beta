# discord-bot-beta
A discord bot for Forever Alo'

## Creating the bot

Go to [Discord Dev Portal](https://discord.com/developers)

- Create an App
- Create a Bot
  - Activate the presence intent to receive presence event data 
  - Activate the server members intent to receive member events and the member list
- Create a OAuth2 URL
  - Select "bot" scope
  - Select permissions
    - Manage Roles
    - Change Nickname
    - Manage Nicknames
    - Send Messages
    - Read Message History
- Naviagate to copied URL
  - If on discord-app-beta, assign permissions to Forever Alo'
  - If on discord-app-test, assign permissions to Testing Alo'

## Launching

### Conncet to the server, install conda
```
ssh root@PUBLIC_IP4_ADDRESS
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
```

### Add some swap space
```
sudo fallocate -l 1G /swapfile 
sudo chmod 600 /swapfile 
sudo mkswap /swapfile 
sudo swapon /swapfile 
sudo cp /etc/fstab /etc/fstab.bak 
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### Clone the codebase
```
git clone forever-alo:forever-alo/discord-bot-beta.git
cd discord-bot-beta
conda env create -f environment.yml
conda env update --name bot-environment -f environment.yml
conda activate bot-environment
```

### Launch the bot
```
supervisord -c supervisord.conf
```
