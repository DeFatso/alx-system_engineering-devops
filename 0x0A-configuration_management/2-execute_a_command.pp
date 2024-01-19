exec { 'killmenow':
  command     => 'pkill -f killmenow',
  refreshonly => true,
}
