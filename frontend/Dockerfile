FROM node:alpine as build-stage

WORKDIR /app
COPY . /app

RUN yarn global add @quasar/cli && yarn install && quasar build -m spa


FROM nginx:alpine as production-stage

LABEL maintainer="Anton Grabovsky <skiton25@gmail.com>"

COPY --from=build-stage /app/dist/spa /usr/share/nginx/html

EXPOSE 80

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
