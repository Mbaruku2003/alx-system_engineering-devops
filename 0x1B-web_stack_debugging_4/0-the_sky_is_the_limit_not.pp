# increase the amount of traffic a server can handle
# increase the unlimit of the default file
exec { 'modify limit to 4096':
   command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
   path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
