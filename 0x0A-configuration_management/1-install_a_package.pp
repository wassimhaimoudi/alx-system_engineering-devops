# This script installs flask 2.1.0 from pip3
package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.0.1',
  path    => '/usr/local/bin:/usr/bin:/bin',
  require => Package['python3-pip'],
}

