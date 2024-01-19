#Using Puppet, create a file

file  { 'school':
  ensure  => file,
  path    => '/tmp/shcool',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'Ilove Puppet',
}
