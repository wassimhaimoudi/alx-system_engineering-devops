# Increase the number of worker processes in the nginx config file
exec { 'upper-treshold':
  command => 'sed -i "s/15/4096/g" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin', '/usr/bin'],  # More consistent paths
}

exec { 'restart-nginx':
  command     => 'service nginx restart',
  path        => ['/usr/local/bin', '/bin', '/usr/bin'],
  require     => Exec['upper-treshold'],  # Ensures this runs after 'upper-treshold'
  refreshonly => true,  # Ensures it only runs if something triggers it
}
