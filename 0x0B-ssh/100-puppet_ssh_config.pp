#!/usr/bin/env bash
#set up file so that you connect to a server without a password.
file {'/etc/ssh/ssh_config':
   ensure => 'present',
}

file_line {'Turn off passwd auth':
   path    => '/etc/ssh/ssh_config',
   line    => 'PasswordAuthentication no',
   match   => 'PasswordAuthetication yes',
   replace => 'true',
}

file_line {'Declare Identity file':
   path    => '/etc/ssh/ssh_config',
   line    => 'IdentityFile ~/.ssh/school',
   match   => '^IdentityFile',
   ensure => 'present',
}
