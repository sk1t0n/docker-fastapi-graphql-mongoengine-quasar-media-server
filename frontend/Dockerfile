FROM node:alpine as build-stage

WORKDIR /app
COPY . /app

RUN yarn global add @quasar/cli && yarn install && quasar build -m spa


FROM nginx:alpine as production-stage

LABEL maintainer="Anton Grabovsky <skiton25@gmail.com>"

COPY --from=build-stage /app/dist/spa /app
COPY --from=build-stage /app/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
