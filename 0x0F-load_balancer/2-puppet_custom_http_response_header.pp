# Custom HTTP header response in a nginx server
# Configures a new ubuntu machine

# update ubuntu server
exec { 'update server':
  command     => 'apt-get update',
  user        => 'root',
  provider    => 'shell',
}
->
# installs nginx web server on server
package { 'nginx':
  ensure      => installed,
  provider    => 'apt'
}
->
# customizes Nginx response header (X-Served-By: hostname)
file_line { 'add HTTP header':
  ensure      => 'present',
  path        => '/etc/nginx/sites-enabled/default',
  after       => 'listen 80 default_server;',
  line        => 'add_header X-Served-By $hostname;'
}
->
# start service
service { 'nginx':
  ensure      => 'running',
  enable      => true,
  hasrestart  => true,
  require     => Package['nginx']
}
