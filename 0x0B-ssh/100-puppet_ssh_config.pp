#create school file
file { '/etc/ssh_config':
  ensure  => 'present',
  mode    => '0744',
  owner   => 'root',
  group   => 'root',
  content => Host * \n 'IdentityFile ~/.ssh/school \n PasswordAuthentication no'
}
