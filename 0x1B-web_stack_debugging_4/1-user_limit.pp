# Script to enable smooth logins of a holberton user

# Increasing hard limit file of the hbton user.
exec { 'fix_limit_hbton_user':
  command => 'sed -i "/holberton hard/s/5/10000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increasing soft file limit of the holberton user.
exec { 'increase_soft_file':
  command => 'sed -i "/holberton soft/s/4/20000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
