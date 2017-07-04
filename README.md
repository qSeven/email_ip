This is a supper simple script to send you an email when your dynamic IP address changes.
I wanted to do this since I didn't want to use a DDNS service and was interested in writing a simple script.

First update the default configuration file.
If you re-name it, you will need to update the new name in the script.
The configuration file takes a gmail address and password to send the email.
Sorry that the password isn't encrypted or secured,
I suggest you use a seperate gmail account for sending emails with python if your are feeling insecure.

You can send the result to multiple emails by adding an rn in the recieivers.
These emails don't have to be a gmail email and can be anything in general.

After you configure the default.cfg file, just run with:

python email_ip.py

or if you want to run in the background.

nohup python email_ip  &
