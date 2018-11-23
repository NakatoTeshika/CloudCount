# Instructions copied from - https://hub.docker.com/_/python/
FROM python:3-onbuild

# tell the port number the container should expose
EXPOSE 80/tcp

# run the command
CMD ["python", "./api.py"]
