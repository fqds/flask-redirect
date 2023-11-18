# flask-redirect
1) https://certbot.eff.org/instructions?ws=other&os=ubuntufocal
2) apt install python3-pip
3) pip install flask
4) copy project
5) set up config.py
6) move flask-redirect.service to /usr/lib/systemd/system
7) sudo systemctl daemon-reload
8) sudo systemctl enable flask-redirect.service
9) sudo systemctl restart flask-redirect
10) sudo systemctl status flask-redirect
