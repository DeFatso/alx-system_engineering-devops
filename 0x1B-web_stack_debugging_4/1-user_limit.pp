# user_limit.pp

# Define a Puppet class for configuring file descriptor limits
#class user_file_limits {

  # Set the file descriptor limits for the holberton user
#  user { 'holberton':
    # Set soft and hard limits for the number of open files
    # Adjust these values as needed
    # 65535 is often used as a high limit
    # These values will be applied to both soft and hard limits
#    ulimit => {
#      'nofile' => {
#        'soft' => 65535,
#        'hard' => 65535,
#      },
#    },
#  }

#}

# Apply the configuration by including the class
#include user_file_limits

# fixes increase limit
exec { 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/" /etc/security/limits.conf':
  path => '/usr/bin:/usr/sbin:/bin',
}
exec { 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4000/" /etc/security/limits.conf':
  path => '/usr/bin:/usr/sbin:/bin',
}
-> exec {'refresh conf':
  command => '/sbin/sysctl -p',
}
