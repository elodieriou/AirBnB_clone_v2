#!/usr/bin/env bash
# Prepare your web servers

# Install Nginx if not already exist
sudo apt-get update
sudo apt-get -y install nginx

# Create folders if not already exist
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Create a fake html file to test Nginx configuration
echo "Deploy web static !" > /data/web_static/releases/test/index.html

# Create a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/
chgrp -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/server_name _;/a \\n\t location /hbnb_static { \n\t\t alias /data/web_static/current/; }' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx start
