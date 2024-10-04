FROM node:20-slim as client
WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=client /app/build /usr/share/nginx/html

EXPOSE $SERVER_PORT

CMD ["nginx", "-g", "daemon off;"]
