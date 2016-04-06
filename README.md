# ts3_client_versions
This script sends a private message to anyone online who has not got the 3.0.19 version of the client. (3.0.19 being hardcoded in)

Handy usage is setting this to crontab to be run every 60 minutes or so, to be annoying enough to force an update but still not annoying enough to drive the user elsewhere.



CLI Output looks like this:

server:/tmp# /tmp/ts3_client_versions.py
[+] Getting client list...
[+] List length: 14418
[+] Number of clients: 179
06-04-2016 17:00:57 TS3 [+] Client info: Username1                              3.0.19
06-04-2016 17:00:58 TS3 [+] Client info: Username2                              3.0.19
06-04-2016 17:00:58 TS3 [+] Client info: Username3                              3.0.18.2
06-04-2016 17:00:59 TS3 [+] Client info: Username4                              3.0.18.2
06-04-2016 17:00:59 TS3 [+] Client info: Username5                              3.0.19
06-04-2016 17:01:00 TS3 [+] Client info: Username6                              3.0.18.2
