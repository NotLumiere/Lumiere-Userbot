#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Lumiere-Userbot https://github.com/NotLumiere/Lumiere-Userbot /home/Lumiereuserbot/ \
    && chmod 777 /home/Lumiereuserbot \
    && mkdir /home/Lumiereuserbot/bin/

COPY ./sample_config.env ./config.env* /home/Lumiereuserbot/

WORKDIR /home/Lumiereuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
