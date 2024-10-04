FROM node:20-slim as client
WORKDIR /client
COPY . /client
RUN npm install && npm run build

FROM node:20-slim as server
WORKDIR /server
COPY package*.json /server/
RUN npm install

FROM node:20-slim
WORKDIR /app
COPY ./server/ /app/server/
COPY --from=server /server/node_modules /app/server/node_modules/
COPY --from=client /client/build/ /app/build

EXPOSE $SERVER_PORT

CMD ["node", "server/index.js"]
