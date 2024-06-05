# Using puppet, ensures nginx is installed and configurated so that http header response contains a custom header key/value pair with the name `X-Served-By` and the hostname as a value.

exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
  user    => 'root',
}

packege { 'nginx'
  ensure => ensure, latest,
}

file_line {'custom_header'
  ensure => present,
  path => '/etc/nginx/nginx.conf',
  match => 'http {',
  line => "http {\n\tadd_header X-Served-By ${hostname};"
}

exec {
  command => '/usr/bin/service nginx restart',
  user => 'root',
}
