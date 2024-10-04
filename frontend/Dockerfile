FROM node:20-slim as client
WORKDIR /client
COPY . /client
RUN npm install && npm run build

FROM node:20-slim as server
WORKDIR /server
COPY package*.json /server/
RUN npm install

FROM nginx:alpine
WORKDIR /app
COPY ./ /app/server/
COPY --from=client /client/build /usr/share/nginx/html

EXPOSE $SERVER_PORT

CMD ["nginx", "-g", "daemon off;"]
