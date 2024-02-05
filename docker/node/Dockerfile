FROM node:18-bookworm
WORKDIR /app
COPY ./package.json /app/
RUN mkdir -p /app/node_modules
RUN apt-get update && apt upgrade -y && apt-get install python3 -y
RUN npm install

COPY . /app
