#!/usr/bin/env bash
# Prepare your web servers

# Install Nginx if not already exist
if [ ! -x /usr/sbin/nginx ]; then
  sudo apt-get update
  sudo apt-get -y install nginx
fi

# Create folders if not already exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake html file to test Nginx configuration
echo "Deploy web static !" > /data/web_static/releases/test/index.html

# Create a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/
sudo chgrp -R ubuntu:ubuntu /data/

# Update Nginx configuration
sed -i '48i\\t location /hbnb_static { \n\t\t alias /data/web_static/current/; }' /etc/nginx/sites-available/default

# Restart Nginx
service nginx start
