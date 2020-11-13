FROM node
LABEL author="andrei.iosif@tum.de"

# set up angular cli
RUN npm i -g --supress-warnings @angular/cli@latest typescript 

WORKDIR /app
COPY package.json /app

# Cool docker hack:
# Copy first (guaranteed) and only copy
# the others if they exist. (saves lines)

# This one: only use package-json if there's no lockfile available
COPY package-lock.json package.json* /app/

RUN [ -f package-lock.json ] && echo ">> using lockfile <<" && npm ci || echo ">> using package.json <<" && npm install --supress-warnings

# now everything on the host frontend/ will be inside app/
# as far as the container is concerned
# ../docker-compose.yml specifies a volume for this,
# to enable live file changes in the container.
COPY . /app

# Angular material is just
# being nasty about it.
# (dependency hell is a real place)
RUN ng add @angular/material

# create watch files
CMD ng serve --host 0.0.0.0 --disable-host-check --proxy-config proxy.conf.dev.json
EXPOSE 4200
