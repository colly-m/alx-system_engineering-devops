# Kills process named killmenow
exec { 'killmenow':
  command  => 'pkill killmenow',
  return   => [0, 1],
}
