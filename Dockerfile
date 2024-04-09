FROM python:3.10

RUN apt-get update && apt-get install -y \
    libx11-6 \
    libx11-xcb1 \
    
    libgl1-mesa-glx \
    libegl1-mesa \
    libxrandr2 \
    libxss1 \
    libxcursor1 \
    libxcomposite1 \
    libasound2 \
    libxi6 \
    libxtst6 \
    libxkbcommon-x11-0 \


RUN pip install PyQt5 numpy vispy

# Copy your application code
COPY . /app
WORKDIR /app

ENV QT_DEBUG_PLUGINS=1
ENV QT_QPA_PLATFORM_PLUGIN_PATH=/usr/local/lib/python3.10/site-packages/PyQt5/Qt5/plugins/platforms

CMD ["python", "src/main.py"]
