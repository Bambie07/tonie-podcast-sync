FROM python

# System deps:
RUN pip install "poetry"

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
RUN pip install -r requirements.txt

COPY tonie_api /app/tonie_api
RUN cd /app/tonie_api && python setup.py install

COPY toniepodcastsync.py podcast.py /app/
COPY tps.py /app/tps.py


ENTRYPOINT ["python", "/app/tps.py"]