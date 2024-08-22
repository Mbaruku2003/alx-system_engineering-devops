#!/usr/bin/env bash
# increase the amount of traffic a server can handle
# increase the unlimit of the default file
exec { 'fix--for--nginx':
   #specify the unlimit value
   command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
   #specify the path for the sed command
   path    => '/usr/local/bin/:/bin/',
}
# restart nginx
exec { 'nginx-restart':
   command => '/etc/init.d/nginx restart',
   #specify the path for init.d server
   path    => '/etc/init.d/',
}
