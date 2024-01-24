# Define a Puppet class for installing and configuring Nginx
class nginx_installation {

  # Ensure Nginx package is installed
  package { 'nginx':
    ensure => 'present',
  }

  # Manage the Nginx default configuration file
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    source  => 'puppet:///modules/nginx_installation/default',
    notify  => Exec['nginx_restart'],
  }

  # Manage the HTML file
  file { '/var/www/html/index.html':
    ensure  => file,
    content => "Hello World!\n",
  }

  # Manage Nginx service
  service { 'nginx':
    ensure    => 'running',
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }

  # Restart Nginx when the configuration changes
  exec { 'nginx_restart':
    command     => 'sudo service nginx restart',
    refreshonly => true,
  }

}

# Include the class to apply it
include nginx_installation

server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm;

    server_name _;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4/;
    }

    location / {
        try_files $uri $uri/ =404;
    }
}
