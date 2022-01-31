FROM python:3.9-slim-buster

RUN apt-get -qq update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app
WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3 -m pip install --upgrade \
    pip \
    wheel

RUN pip install -r requirements.txt

CMD [ "python3", "-m", "app" ]
