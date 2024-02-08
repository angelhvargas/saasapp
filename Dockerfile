# for forcing NPM build.
# this should not be used for development.
# is helpful to spot problems with NPM compatibility.

FROM node:20-bookworm-slim

RUN apt update -y && apt clean && apt install -y python3 \
gcc make build-essential git


COPY . .

RUN npm install
RUN npm run babel
RUN npm run dev
#RUN NODE_ENV=development npm run babel -- ./node_modules/.bin/webpack-dev-server --progress --hot --host 0.0.0.0