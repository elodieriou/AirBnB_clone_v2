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

file { '/data':
  ensure => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/date/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'Deploy web static',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
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
