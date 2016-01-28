Homework 02
===========

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









