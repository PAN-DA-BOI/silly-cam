#!/bin/bash

# Update and upgrade the system
sudo apt-get update
sudo apt-get upgrade -y

# Install necessary packages
sudo apt-get install -y bc
sudo apt-get install -y wiringpi
sudo apt-get install -y libjpeg-dev
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-pillow
sudo apt-get install -y python3-numpy
sudo apt-get install -y libatlas-base-dev
sudo apt-get install -y libopenjp2-7
sudo apt-get install -y libtiff5
sudo apt-get install -y libilmbase23
sudo apt-get install -y libopenexr23
sudo apt-get install -y libavcodec58
sudo apt-get install -y libavformat58
sudo apt-get install -y libswscale5
sudo apt-get install -y libv4l-dev
sudo apt-get install -y libxvidcore4
sudo apt-get install -y libx264-155
sudo apt-get install -y libfaac0
sudo apt-get install -y libfaac-dev
sudo apt-get install -y libmp3lame0
sudo apt-get install -y libtheora0
sudo apt-get install -y libvorbisenc2
sudo apt-get install -y libxvidcore4
sudo apt-get install -y libopencv-dev
sudo apt-get install -y python3-opencv

# Enable SPI interface
sudo raspi-config nonint do_spi 0

# Download and install the LCD driver
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
sudo ./LCD35-show

# Reboot the system
sudo reboot
