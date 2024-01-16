FROM node:16-alpine

WORKDIR /usr/src/frontend

COPY ./package.json .
COPY ./tsconfig.json .

RUN yarn install

COPY ./src src

COPY ./public public

EXPOSE 3000

CMD yarn start