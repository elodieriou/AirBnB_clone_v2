
# puppet manifest preparing a server for static content deployment
exec { 'update':
  command => 'apt-get -y update',
  path    => '/usr/bin',
}
-> package { 'nginx':
  ensure  => present,
  name    => 'nginx',
  require => Exec['update'],
}
-> exec {'create_directory':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/ /data/web_static/shared/',
}
-> file { 'Hello World':
  ensure => 'present',
  path => '/data/web_static/releases/test/index.html',
  content => 'Hello World\n',
}
-> exec {'create_symbolic_link':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}
-> file_line { 'add_alias':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}
-> exec {'i':
  command => '/usr/bin/env service nginx restart',
}
-> exec {'g':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}
