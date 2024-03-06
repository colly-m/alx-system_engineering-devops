# Puppet script to replace a line in a file on a server

$file_to_edit = '/var/www/html/wp-settings.php'

#Fixing line containing "phpp" with "php"

exec { 'fix_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => '/usr/local/bin/:/bin/'
}
