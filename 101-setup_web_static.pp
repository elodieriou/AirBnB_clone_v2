# Puppet for setup web static
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
-> exec {'update_configuration':
  command => '/usr/bin/env sed -i "48i location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}
-> service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
-> exec {'give_ownerships':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}
