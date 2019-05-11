FROM python:2

ADD MovieRetrievalViaOmdbapi.py /

ENTRYPOINT ["python", "MovieRetrievalViaOmdbapi.py"]
