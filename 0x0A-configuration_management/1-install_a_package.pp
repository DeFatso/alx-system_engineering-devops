# Install flask

exec  { 'puppet-lint':
  command => '/usr/bin/pip3 install flask -v 2.1.0',
}
