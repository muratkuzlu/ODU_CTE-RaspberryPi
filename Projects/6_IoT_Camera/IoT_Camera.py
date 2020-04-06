"""
Raspberry Pi Camera Setup
● Step 1:- First, turn off your Pi and then locate the camera
connector, a long black connector between the HDMI port and
Audio Jack. The connector is marked with ‘CAMERA’ on the
board.
● Step 2:- To connect camera pull up on the ends of the black
plastic connector and insert camera cable as shown in the image.
Camera cable’s metal pads should face the metal pads inside the
connector. Now press down on the ends of the black connector.
● Step 3:- We need to enable the camera. Go to the ‘Preferences’
and ‘Raspberry Pi Configuration’ tab.
● Step 4:- Then, a screen will open, and on that screen click
on ‘Interfaces’. Click ‘Enabled’ on the ‘Camera’ row.
● Step 5:- After this, reboot your Raspberry Pi.
● Step 6:- After the reboot, test the camera to check whether its
working or not by using the following command:
"""
raspistill -o cam_test.jpg
"""
● Step 7:- If the camera works properly, the onboard
red LED of the camera will glow
whenever you click as photo.
● Step 8:- If you see the command fail error, go
back and check that you have enabled the
camera or not and make sure the camera cable
is connected firmly with the board.

Stream video to Adafruit IO dashboard
Step 1 Adafruit IO Setup
• For Adafruit IO setup, first sign up on Adafruit
IO website (https://io.adafruit.com ) by clicking
on ‘Get started for Free’ at the top right corner of the
screen.
• Now after this you need to create a feed, which you
can do by clicking on ‘Feed’ . Click on ‘Actions’ to
proceed and then click on ‘Create a New Feed’.
• After creating a feed now you need to create a
‘Dashboard’. To create dashboard click on the “Create
Dashboard” button in the upper right corner and give
name to the new dashboard like Pi Camera Dashboard.
• Now to add block click on ‘+ sign’ on the top right
corner of the screen and scroll down to the image
block and click on Create.
• In the ‘Choose feed’ window, click on the feed
named camera_feed and click on ‘Next step’.
• After that click on Create Block to create the image
block. Also, you can use Adafruit IO for developing
various IoT projects.

Step 2 Raspberry Pi Setup
• To setup the Pi, you need to install the Node.js on your Raspberry Pi. For installing the Node.js go to home directory
using ‘cd ~’ command and then download a pre-built Node.js package from the node-arm project and install it on the
terminal.
"""
cd ~
wget http://node-arm.herokuapp.com/node_latest_armhf.deb
sudo dpkg -i node_latest_armhf.deb
"""
• To check, whether the Node.js is installed or not use the below commands:
"""
node –v
npm –v
"""
• This will show you the current version of Node.js.
• After installing the Node.js, now you need to install ‘adafruit-io-camera’ on your Pi. This tool is used to monitor the Pi
camera and send pictures to an Adafruit IO feed.
"""
sudo apt-get update
sudo apt-get install -y imagemagick
sudo npm install --global --no-optional forever forever-service adafruit-io-camera
"""
• After this use your ‘Username’ and ‘AIO Key’ (password) to provide a path to your Adafruit IO account.
"""
adafruit-io camera config --username YOUR USERNAME --key AIO KEY
"""
• Enter your username and AIO key on the place of ‘YOUR USERNAME’ and ‘AIO KEY’ respectively.

• Now start your camera using the following command:
"""
adafruit-io camera start -f camera_feed -m false -r 2
"""
• Here ‘camera_feed’ is the name of feed that you have
created earlier. You can change it according to your feed
name.
• Now navigate to your Adafruit IO dashboard. It takes some
time for the camera to start and upload images on the
dashboard.
"""
