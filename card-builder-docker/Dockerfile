FROM node:alpine
WORKDIR /work
COPY package.json /work
COPY gulpfile.js /work
RUN npm install
CMD ["npm", "run", "gulp"]
