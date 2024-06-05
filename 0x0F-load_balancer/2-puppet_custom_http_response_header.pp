# Using puppet, ensures nginx is installed and configurated
# so that http header response contains a custom header key/value pair
# with the name `X-Served-By` and the hostname as a value.

exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
  user    => 'root',
}

package { 'nginx':
  ensure => latest,
}

file_line { 'custom header':
  ensure => present,
  path   => '/etc/nginx/nginx.conf',
  match  => 'http {',
  line   => "http {\n\tadd_header X-Served-By ${facts['networking']['hostname']};",
  notify => Exec['restart_nginx'],  # Notify the restart if the line is added/changed
}

exec { 'restart nginx':
  command     => '/usr/bin/service nginx restart',
  user        => 'root',
  refreshonly => true,  # Only run when notified
}
