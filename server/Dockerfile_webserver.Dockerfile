FROM node:slim 

# Create the base server
RUN mkdir -p /server/
WORKDIR /server/

COPY server/package.json package.json
RUN npm install 

ENV DOCKERIZED=1

# Copy the necessary files
COPY server/configurations configurations/
COPY server/source/ source/
COPY server/main.js main.js 


EXPOSE 3000

WORKDIR /server/
ENTRYPOINT [ "npm", "start" ]




