FROM node:8

# set up angular cli
RUN npm -g add @angular/cli@10.2.0

WORKDIR /app
COPY package.json /app
COPY yarn.lock /app
RUN yarn install --pure-lockfile

# now everything on the host frontend/ will be inside app/
# as far as the container is concerned
# ../docker-compose.yml specifies a volume for this,
# to enable live file changes in the container.
COPY . /app

# create watch files
CMD ng serve --host 0.0.0.0 --disable-host-check --proxy-config proxy.conf.dev.json
EXPOSE 4200
