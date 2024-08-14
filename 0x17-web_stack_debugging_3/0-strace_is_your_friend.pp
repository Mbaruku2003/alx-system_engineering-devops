#!/usr/bin/env bash
#fixes bad phpp extension to php
exec{'fix-wordpress':
<<<<<<< HEAD
   command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
   path    => 'usr/local/bin/:/bin/'
=======
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => 'usr/local/bin/:/bin/'
>>>>>>> 41467160e0f7749f5eedafb6452cbd1ca4d58f1d
}
