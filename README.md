# flask-redirect
1) https://certbot.eff.org/instructions?ws=other&os=ubuntufocal
2) apt install python3-pip
3) pip install flask
4) copy project
5) set up config.py
6) mv flask-redirect.service /usr/lib/systemd/system && sudo systemctl daemon-reload && sudo systemctl enable flask-redirect.service && sudo systemctl restart flask-redirect && sudo systemctl status flask-redirect
