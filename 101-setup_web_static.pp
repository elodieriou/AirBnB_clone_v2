# Puppet for setup
include stdlib

exec { 'update':
  command => 'sudo apt-get update',
  path    => '/usr/bin',
} ->

package { 'nginx':
  ensure  => present,
  name    => 'nginx',
} ->

exec { 'create directory':
  command => 'mkdir -p /data/web_static/releases/test /data/web_static/shared',
  path    => '/usr/bin',
} ->

file { 'create fake html':
  ensure  => 'present',
  path    => '/data/web_static/releases/test/index.html',
  content => 'Deploy web static !',
} ->

file { 'create symbolic link':
  ensure  => 'link',
  path    => '/data/web_static/current',
  force   => true,
  target  => '/data/web_static/releases/test',
} ->

file_line { 'add alias':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'location /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-available/default',
} ->

service { 'nginx':
  ensure  => running,
} ->

exec { 'give ownerships':
  command => 'chown -R ubuntu:ubuntu /data',
  path    => '/usr/bin',
}
