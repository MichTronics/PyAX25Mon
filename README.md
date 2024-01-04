### PyAX25Mon 

This program receive TCP Kiss frames from Direwolf. <br>
And decode the Kiss frames to AX25 Frames and print out <br>
all info and bits of that AX25 Frame in the console. <br>

![Screenshot_23](https://github.com/MichTronics/PyAX25Mon/assets/60797474/aa12140c-5f4b-4a57-9d96-d83eb6458fa7)

## Linux

Install Python3 and Pip and Git
Then clone this repo with :

git clone https://github.com/MichTronics/PyAX25Mon.git

then :

cd /PyAX25Mon
pip install -r requirements.txt

then you need to configure the config.ini file with the good ipaddress and port of Direwolf machine.
then you can run the py file wtih :

python3 PyAX25Mon.py

## Windows

Download and unpack this Release :

https://github.com/MichTronics/PyAX25Mon/releases/download/v0.1/PyAX25Mon.zip

and then run :

PyAX25Mon.exe

