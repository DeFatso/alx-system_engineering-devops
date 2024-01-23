# File: nginx_config.pp

# Update package list
package { 'nginx':
  ensure => installed,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure => file,
  content => "server {
    listen 80;
    server_name localhost;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}",
  notify => Service['nginx'],
}

# Create a simple HTML file with Hello World!
file { '/usr/share/nginx/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  notify  => Service['nginx'],
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
}
