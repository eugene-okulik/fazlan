FROM jenkins/jenkins:lts-jdk17

USER root

# Установка Python, pip, venv и других зависимостей
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv wget

# Установка Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Копирование файлов
COPY requirements.txt .
COPY test_demo.py .

# Создание виртуального окружения и установка зависимостей
RUN python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

# Используем пользователя Jenkins
USER jenkins
