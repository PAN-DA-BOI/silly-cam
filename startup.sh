#!/bin/bash

# Create a systemd service file
sudo bash -c 'cat > /etc/systemd/system/camera.service' << EOL
[Unit]
Description=Camera Script
After=graphical.target

[Service]
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/pi/.Xauthority
ExecStart=/usr/bin/python3 /path/to/your/camera_script.py
WorkingDirectory=/home/pi
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=graphical.target
EOL

# Reload the systemd daemon
sudo systemctl daemon-reload

# Enable the service to start on boot
sudo systemctl enable camera.service

# Start the service
sudo systemctl start camera.service
