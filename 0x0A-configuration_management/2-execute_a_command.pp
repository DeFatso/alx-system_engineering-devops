#manifest that kills a process named killmenow
exec { 'killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  refreshonly => true,
  logoutput   => true,
  onlyif      => '/usr/bin/pgrep -f killmenow',
  loglevel    => 'debug',
}
