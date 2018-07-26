# install puppet-lint
exec { 'killme' :
    command  => 'pkill killmenow'
    provider => 'shell'
}
