#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate

pip install -r /home/ubuntu/gym_website/requirements.txt
pip install gunicorn
sudo chmod 777 /home/ubuntu/gym_website
sudo chmod 777 /home/ubuntu/gym_website/db.sqlite3
