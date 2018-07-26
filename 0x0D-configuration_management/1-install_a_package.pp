# install puppet-lint
exec { 'package install' :
    command  => 'gem install puppet-lint -v 2.1.1'
    provider => 'shell'
}
