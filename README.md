## Change Data Capture (CDC) example

## Steps:
1. cp .env.example .env
2. ./tools.sh pg up -d --build
3. Open your browser: 
 - http://127.0.0.1:8080 > Create connector
4. Setup venv and install libraries 
 - python3 -m venv venv
 - source venv/bin/active (linux/macos)
 - pip install -r requirements.txt
 - python consumer.py

5. Access to postgres tools (pgAdmin)
 - schema: inventory
 - Do something with your data

## Clean:
1. Stop python consumer.py
2. ./tools.sh pg down -v
