exec { 'apt-get-update':
  command => 'apt-get -y update',
  path    => '/usr/bin',
}
-> exec {'install':
  command => 'apt-get -y install nginx',
  path    => '/usr/bin',
}
-> exec {'create directory':
  command => 'mkdir -p /data/web_static/releases/test/ /data/web_static/shared/',
  path    => '/usr/bin',
}
-> exec {'create fake html':
  command => 'echo "Deploy web static with puppet" > /data/web_static/releases/test/index.html',
  path    => '/usr/bin',
}
-> exec {'create symbolic link':
  command => 'ln -sf /data/web_static/releases/test /data/web_static/current',
  path    => '/usr/bin',
}
-> exec {'modify configuration':
  command => 'sed -i "/server_name _;/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
  path    => '/usr/bin',
}
-> exec {'restart nginx':
  command => 'service nginx restart',
  path    => '/usr/bin',
}
-> exec {'give ownerships':
  command => 'chown -R ubuntu:ubuntu /data',
  path    => '/usr/bin',
}
