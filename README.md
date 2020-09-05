# ServerBot Readme
This is telegram bot for server monitoring. 
This bot can send messages to your telegram id
Tested on ubuntu 18.04 & python 3.6.9

# What this bot can do?

###  Monitoring

 1. CPU load 
 2. RAM load
 3. Network

### Historical data
 1. CPU Utilization
 2. RAM Load
 3. Disk I/O
 4. Network perfomance 
 5. Ping test 

### Alert
 1. High CPU Utilization
 2. High RAM load
 3. Network degradation

### Server
 1. Check CPU load + Historical data
 2. Check RAM load + Historical data
 3. Check disk usage
 4. Check disk i/o + Historical data
 5. Check server ping + Historical data
 6. Alalyze server traceroute
 7. Get top processes
 8. Check uptime
 9. Check network load + Historical data
 10. Check server network speed to different countries (Some countries may not work because speedtest servers may have problems. On Hetzner, many countries didn't work. In the future, I will add much more servers for tests)

### Installation in 5 simple steps (2-3 minutes, and your bot is ready)
 1. Create your personal telegram bot and get Api Token.
 2. Send to your new bot command /start and go to the next step.
 3. Run command below
```sh
cd $HOME && git clone -v https://github.com/boo50/ServerBot.git serverbot && cd ./serverbot && chmod +x ./installsbot.sh
```
 4. Open ./config.py and insert your bot API and your telegram id.
 5. Run 
```sh
./installsbot.sh
```

### What to do if something not working?
If you get History load error, remove bot files from /tmp
sudo rm -rf /tmp/*.log
sudo rm -rf /tmp/*.png

Find in bot.py telebot.logger.setLevel(logging.ERROR) and change ERROR to DEBUG, restart serverbot service and execute
  ```sh
$ journalctl -e -u serverbot > ~/serverbot/servicelog.log
```
