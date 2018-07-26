#create file in /tmp/
file { 'holberton' :
    ensure     => file,
    path       => '/tmp/holberton',
    owner      => 'www-data',
    group      => 'www-data',
    permission => '0744',
    content    => 'I love Puppet'
}
