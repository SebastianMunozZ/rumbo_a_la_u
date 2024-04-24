FROM node:18.16.0

WORKDIR /app

COPY . .

RUN cd development-pkg && npm install && npm install -g gulp-cli

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]

EXPOSE 3111

#CMD ["cd development-pkg", "gulp"]