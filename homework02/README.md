Homework 02
===========

Activity 01
-----------

1. 
#create workspace on source machine
mkdir /tmp/kherring-workspace

#Generate 10MB file full of random data
dd if=/dev/urandom of=testFile s=10485760 count=1

#Create 10 hard links to 10MB file
ln testFile data0
ln testFile data1
ln testFile data2
ln testFile data3
ln testFile data4
ln testFile data5
ln testFile data6
ln testFile data7
ln testFile data8
ln testFile data9

#create workspace on target machine
mkdir /tmp/kherring-workspace

2. du -bh on source: 11M; somewhat surprising since -ls -lh lists the total in the directory as 111MB (the extra 1MB is from the sftpFile) but makes since since data0-data9 are really just links pointing to a file that's 10MB, and are not 10MB themselves.

3. du -bh on targer: 111M; the number is difference because for each data0-data9 the actual file they were linking was copied onto the target directory instead of jsut a link, taking up significantly more space.

4. 
# Transfer data files using scp
scp [data]* testFile kherring@student01.cse.nd.edu:/tmp/kherring-workspace

# Transfer data files using sftp

sftp kherring@student01.cse.nd.edu

# Contents of file used for sftp

cd /tmp/kherring-workspace
lcd /tmp/kherring-workspace
put data*
exit

# Transfer data files using rsync

rsync -a ../kherring-workspace kherring@student01.cse.nd.edu:/tmp

5. For sftp and scp, each file is transfered once when the command is run multiple times, however for rsync the files are only synced with the initial push.

6. rsync because it is the most convenient to use and does not copy files every time if it's not necessary.

Activity 01
-----------

1. Scan 'xavier.h4x0r.space' for HTTP port

nmap -p9000-10000 xavier.h4x0r.space -Pn

# Output: 
Nmap scan report for xavier.h4x0r.space (129.74.161.24)
Host is up (0.00039s latency).
Not shown: 997 closed ports
PORT      STATE    SERVICE
9097/tcp  open     unknown
9111/tcp  open     DragonIDSConsole
9876/tcp  open     sd
10000/tcp filtered snet-sensor-mgmt

2. Connect to HTTP server:

curl xavier.h4x0r.space:9876

#output: 

 _________________________________________ 
/ Halt! Who goes there?                   \
|                                         |
| If you seek the ORACLE, you must query  |
| the DOORMAN at /{netid}/{passcode}!     |
|                                         |
| To retrieve your passcode you must      |
| decode the file at                      |
| ~pbui/pub/oracle/${USER}/code using the |
| BASE64 command.                         |
|                                         |
\ Good luck!                              /
 ----------------------------------------- 
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$ 
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P 
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$# 
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$* 
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R" 
        "*$bd$$$$      '*$$$$$$$$$$$o+#" 
             """"          """""""

3. Decode passcode:

 cd ~pbui/pub/oracle/kherring
 base64 -d code

# Output

5bd2905795d466ec809dde4f9eb946c2

3. Contact Doorman

curl xavier.h4x0r.space:9876/kherring/5bd2905795d466ec809dde4f9eb946c2

# Output:

 _________________________________________ 
/ Ah yes, kherring... I've been waiting   \
| for you.                                |
|                                         |
| The ORACLE looks forward to talking to  |
| you, but you must first retrieve a      |
| secret message from the SLEEPER.        |
|                                         |
| He can be found in plain sight at       |
| ~pbui/pub/oracle/SLEEPER... You will    |
| need to wake him up and then signal him |
| to HANGUP his connection. If he         |
| recognizes you, he will give you the    |
| message in coded form.                  |
|                                         |
| Once you have the message, proceed to   |
| port 9111 and deliver the message to    |
| the ORACLE.                             |
|                                         |
| Hurry! The ORACLE is wise, but she is   |
\ not patient!                            /
 ----------------------------------------- 
  \
   \   \
        \ /\
        ( )
      .( o ).

4. Awaken the SLEEPER

cd ~pbui/pub/oracle/
./SLEEPER

# in another terminal:

pkill -1 SLEEPER

# Output: 

 _______________________________ 
< Uh... What? What do you want? >
 ------------------------------- 
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/

 ________________________________________ 
/ Hmm... I recognize you kherring...     \
| Here's the message you need to give to |
| the ORACLE:                            |
|                                        |
\ eHVyZWV2YXQ9MTQ1NDAxMTU5Mw==           /
 ---------------------------------------- 
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/

5. Give message to the oracle:

telnet xavier.h5x0r.space 9111

# Output 

 ________________________ 
< Hello, who may you be? >
 ------------------------ 
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$ 
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P 
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$# 
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$* 
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R" 
        "*$bd$$$$      '*$$$$$$$$$$$o+#" 
             """"          """"""" 
NAME? kherring
 ___________________________________ 
/ Hmm... kherring?                  \
|                                   |
| That name sounds familiar... what |
\ message do you have for me?       /
 ----------------------------------- 
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$ 
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P 
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$# 
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$* 
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R" 
        "*$bd$$$$      '*$$$$$$$$$$$o+#" 
             """"          """"""" 



 ______________________________________ 
/ Ah yes... kherring!                  \
|                                      |
| You're smarter than I thought. I can |
| see why the instructor likes you.    |
|                                      |
| You met the SLEEPER about 9 minutes  |
\ ago... What took you so long?        /
 -------------------------------------- 
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$ 
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P 
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$# 
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$* 
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R" 
        "*$bd$$$$      '*$$$$$$$$$$$o+#" 
             """"          """"""" 
REASON? 

REASON? At work
 ______________________________________ 
/ Hmm... Sorry, kid. You got the gift, \
| but it looks like you're waiting for |
| something.                           |
|                                      |
| Your next life, maybe. Who knows?    |
\ That's the way these things go.      /
 -------------------------------------- 
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$ 
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P 
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$# 
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$* 
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R" 
        "*$bd$$$$      '*$$$$$$$$$$$o+#" 
             """"          """"""" 

Congratulations kherring! You have reached the end of this journey.

I hope you learned something from the ORACLE :]

-insert matrix animation here-




