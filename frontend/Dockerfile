FROM node:18-alpine

WORKDIR /usr/src/frontend

# install dependencies
RUN apk update
RUN apk add xdg-utils

COPY ./package.json .
COPY ./tsconfig.json .
COPY ./index.html .
COPY ./vite.config.ts .
COPY ./vite-env.d.ts .

RUN yarn install



COPY ./src src

COPY ./public public

EXPOSE 3000

CMD yarn start