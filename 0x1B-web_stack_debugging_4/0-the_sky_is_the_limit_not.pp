#sed nginx to handle more requests
exec { 'limit increase':
  command  => 'sed -i "s/-n 15/-n 2000/g"\
  /etc/default/nginx; sudo service nginx restart',
  provider => 'shell'
}
