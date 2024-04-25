# This script creates a file in /tmp
file {'/tmp/school':
  ensure  => file, present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
