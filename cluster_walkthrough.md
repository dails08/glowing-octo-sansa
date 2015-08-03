Spin up four (or however many) machines in Softlayer.  Use RHEL 6 64bit, 2 cpus, 16GB memory, and a 300 disk (I don't know how to add a SAN disk with the command line yet).  Name one of them "salt" (this makes setting up Salt easier) and the others something recognizeable like "minion1", "cluster1" or whatever.

Edit the /etc/hosts file on the Salt machine to include entries for each of the cluster machines.  Include the ip address, the fqdn, and the alias.  Each line should look something like:
111.22.33.444 minion1.whatever.com minion1

Edit the /etc/hosts file on each of the minions to include an entry for the Salt machine.  This should be the only time you'll ever have to shell into the cluster minions (until way later when you want to run stuff on that machine specifically)

Shell into the first one and follow the instructions to install Salt from here with the exception I mention after the link: 

http://docs.saltstack.com/en/latest/topics/installation/rhel.html

When you run salt-master run it with the command "salt-master -d" so it runs in the background.  Run "salt-minion -d" as well (run both master and minion on the Salt machine and just minion on the others.  Start the master first.)

I think the salt deamons will stop when you close the terminal.  You can run it with the "nohup" command to keep it running.  I think I have it set up so it does that automatically now, but I have to check.

Ten seconds after you start the last salt-minion, go back to your salt-master and type:

salt-keys -L

There should be a bunch of unaccepted keys.  Type:

salt-keys -A

This accepts all the keys.  You can test the connectivity of the minions by typing:

salt "*" test.ping

Which should return True from each minion.

Next, update Java using salt:

salt "*" wget 
