#!/bin/bash
# Выполните эту команду на сервере от root или через sudo
echo "alekseeva ALL=(ALL) NOPASSWD: /bin/systemctl restart alekseeva-api" | sudo tee /etc/sudoers.d/alekseeva
sudo chmod 0440 /etc/sudoers.d/alekseeva
