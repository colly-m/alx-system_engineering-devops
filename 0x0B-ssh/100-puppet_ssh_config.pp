#!/usr/bin/env bash
# SSH client configuration file to enable connection with no password
# Using Puppet

file_line { 'SSH Private Key':
  path     => '/etc/ssh/ssh_config',
  line     => 'IdentityFile ~/.ssh/school',
  match    => '^IdentityFile',
}

# Reglex explanation
#
# ^      beginning of a line
file_line { 'Turn off Password':
  path     => '/etc/ssh/ssh_config',
  line     => 'PasswordAuthentication no',
  match    => '^PasswordAuthentification',
}
