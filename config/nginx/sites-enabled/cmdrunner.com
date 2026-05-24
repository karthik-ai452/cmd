server {
    listen 80;
    server_name cmdrunner.com www.cmdrunner.com;

    location = /favicon.ico {
        alias /opt/cmdrunner-website/static/favicon/favicon.ico;
    }

    location /static/ {
        alias /opt/cmdrunner-website/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location / {
        proxy_pass http://unix:/opt/cmdrunner-website/cmdrunner.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}