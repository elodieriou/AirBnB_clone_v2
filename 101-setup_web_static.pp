# Puppet for setup
exec { 'update':
  command => 'sudo apt-get update',
  path    => '/usr/bin',
}

package { 'nginx':
  ensure  => present,
  name    => 'nginx',
  require => Exec['update'],
}

exec { 'mkdir':
  command => 'mkdir -p /data/web_static/releases/test/ /data/web_static/shared/',
  path    => '/usr/bin',
}

file { '/data/web_static/releases/test/index.html':
  ensure => 'present',
  path   => '/data/web_static/releases/test/index.html',
}

file_line { 'deployWebStatic':
  message => 'Deploy web static !',
  path    => '/data/web_static/releases/test/index.html',
  line    => 'Deploy web static',
}

file { '/data/web_static/releases/test/':
  ensure => 'link',
  target => '/data/web_static/current',
}

exec { 'change_owner_and_group':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => '/usr/bin',
}

exec { 'modify_file':
  command => 'sed -i '48i\\t location /hbnb_static { \n\t\t alias /data/web_static/current/; }' /etc/nginx/sites-available/default',
  path    => '/usr/bin',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
