# This puppet manifest fixes a server error that was caused by a typo

exec {'replate_line':
  command  => "sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'",
  path    => ['/bin', '/usr/bin']
}
