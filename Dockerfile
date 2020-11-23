# We're using Ubuntu 20.10
FROM alfianandaa/alf:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/indraadp/telegram-userbot /home/telegram-userbot/
RUN mkdir /home/telegram-userbot/bin/
WORKDIR /home/telegram-userbot/

CMD ["python3","-m","userbot"]
