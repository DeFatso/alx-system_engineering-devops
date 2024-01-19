# Install Python
include python3
class { 'python3':
  version  => 'system',
}

# Install Flask using pip3
python::pip { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Class['python3'],
}
