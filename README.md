# discord-bot-beta
A discord bot for Forever Alo'

```
ssh root@PUBLIC_IP4_ADDRESS
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
```

```
sudo fallocate -l 1G /swapfile 
sudo chmod 600 /swapfile 
sudo mkswap /swapfile 
sudo swapon /swapfile 
sudo cp /etc/fstab /etc/fstab.bak 
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

```
git clone forever-alo:forever-alo/discord-bot-beta.git
cd discord-bot-beta
conda env create -f environment.yml
conda env update --name bot-environment -f environment.yml
conda env activate bot-environment
```

```
supervisord -c supervisord.conf
```
