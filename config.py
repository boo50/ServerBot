#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Config
BotAPIKey = 'x:y' # API Keythat you get from @BotFather
tg = 1111 # Your id, you can get it by sending command /id to bot @TONTgIDBot
serverbotpath = '/home/$USER/serverbot' # User folder with this bot.
serverbotpathdb = '/home/$USER/serverbot/db' # User folder with bot database. 
srvping = '1.1.1.1' # Ping test server
traceroutetest = '1.1.1.1' # Traceroute test server

# Alarms
memloadalarm = 95 # RAM Utilization alarm starts at
pingcalarm = 15 # When ping will be more than X ms, you will get alarm.
cpuutilalarm = 97 # CPU Utilization alarm starts at
#timediffalarm = -55 # Time Diff alarm start at
#minstakes = 10001 # Min Stake
#balchecks = 1800 # How often to check your balance, in seconds. 300 = 5 min, 1200 = 20min, 3600 = 1 hour.
#stakecheck = 60 # Stake check every minute
#stakesendcheck = 9000 # When first stake send check do after election stars. 1800=30min after election start, 3600 = 1hour, 7200 = 2 hours, 9000 = 2.5 hours
#repeattimealarmtd = [5,15,25,30,60,90,120,180,320, 640, 1280, 2560, 5120, 10240, 20480, 40960, 81920] # Notify every x second about time diff check failed
#repeattimealarmnode = [5,15,25,30,60,90,120,180,320, 640, 1280, 2560, 5120, 10240, 20480, 40960, 81920] # Notify every x second about validator node down
repeattimealarmsrv = [5,15,25,30,60,90,120,180,320, 640, 1280, 2560, 5120, 10240, 20480, 40960, 81920] # Notify every x second about high CPU, RAM load and ping

# DB Scans
#cfgAlertsNotifications = 1 # Validator engine Monitopring
cfgAlertsNotificationsRam = 1 # RAM Monitoring + history
cfgAlertsNotificationsCPU = 1 # CPU Monitoring + history
#cfgAlertsNotificationst = 1 # Time Diff Monitopring
cfgmonitoringnetwork = 1 # Netowrk Monitopring
cfgAlertsNotificationsping = 1 # RAM, Ping & CPU Monitopring
cfgmonitoringdiskio = 1 # Disk I/O Monitopring
#cfgmonitoringslowlog = 0 # Slow log Monitopring
#cfgstakechange = 0 # Autostake. Check balance and edit stake to max
#cfgmonitoringadnlkey = 1 # Adnl key db checker
#cfgmonitoringstakesendcheck = 1 # Check stake send
