#create school file
file { '/etc/ssh_config':
  mode    => '0744',
  owner   => 'root',
  group   => 'root',
  content => 'IdentityFile ~/.ssh/school \n PasswordAuthentication no'
}
