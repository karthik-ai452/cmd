# CmdRunner Website

AI-powered automation and software testing platform landing page. Operated by **BotifyQA Solutions Private Limited**.

## Project Structure

```
cmdrunner-website/
├── server.py                          # Main Python server (Flask + Gunicorn)
├── requirements.txt                   # Python dependencies
├── .env-example                       # Environment variables template
├── .gitignore                         # Git ignore rules
│
├── config/                            # Deployment configuration
│   ├── cmdrunner_website.service      # Systemd service file
│   └── nginx/sites-enabled/
│       └── cmdrunner.com              # Nginx reverse proxy config
│
├── static/
│   ├── assets/
│   │   ├── css/
│   │   │   └── main.css               # Main stylesheet
│   │   └── js/
│   │       ├── main.js                # Main JavaScript
│   │       └── util.js                # Utility functions
│   ├── favicon/                       # Favicon assets
│   └── images/                        # Product images and logos
│
└── templates/
    ├── index.html                     # Landing page
    └── terms.html                     # Legal framework (ToS, Privacy, Refund, etc.)
```

## Quick Start

### Local Development

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python server.py
```

The site runs at `http://localhost:5000`.

### Production Deploy (AWS / Nginx + Gunicorn)

```bash
# Clone to /opt/cmdrunner-website
sudo cp config/cmdrunner_website.service /etc/systemd/system/
sudo systemctl enable cmdrunner_website
sudo systemctl start cmdrunner_website

# Nginx config
sudo cp config/nginx/sites-enabled/cmdrunner.com /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

## Routes

| Route      | Description                                       |
|------------|---------------------------------------------------|
| `/`        | Landing page                                      |
| `/terms`   | Complete legal framework (9 sections)             |
| `/privacy` | Redirects to `/terms#privacy-policy`              |
| `/refund`  | Redirects to `/terms#refund`                      |
| `/register`| POST — Beta registration (JSON API)               |

## Stack

- **Backend:** Python, Flask, Gunicorn
- **Frontend:** Tailwind CSS (CDN), vanilla JavaScript
- **Server:** Nginx reverse proxy → Gunicorn

## License

© 2026 BotifyQA Solutions Private Limited. All rights reserved.