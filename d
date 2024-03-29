server {
    listen 80;
    server_name shartnoma.kspi.uz;

    listen 443 ssl;
    server_name shartnoma.kspi.uz;  # Sizning domeningiz nomi
    ssl_certificate /home/shartnoma/pdf2023/security_key/STAR.kspi.uz.crt;  # Sertifikat fayli yo'li
    ssl_certificate_key /home/shartnoma/pdf2023/security_key/STAR_kspi_uz.key;  # Maxfiy kalit fayli yo'li



    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/shartnoma/pdf2023;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
