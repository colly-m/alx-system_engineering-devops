# Script to install nginx using puppet

package { 'nginx':
  ensure        => 'present',
  listen_ports  =>  ['80'],
}

service { 'nginx':
  ensure        => 'running',
  enable        => true,
  subscribe     => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure        => 'file',
  content       => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure        => 'file',
  content       => template('path/to/your/nginx_config.erb'),
  notify        => Exec['nginx-restart'],
}

exec { 'nginx-restart':
  command       => 'service nginx restart',
  refreshonly   => true,
}
