FROM node:lts-alpine AS builder
WORKDIR /app
RUN yarn cache clean && yarn --update-checksums
COPY . ./
RUN yarn && yarn run build

FROM node:lts-alpine
RUN apk add --no-cache git
WORKDIR /app
COPY --from=builder /app/dist ./dist
RUN yarn add spassr@1.0.2
EXPOSE 5000 5005
ENTRYPOINT ["npx", "spassr", "--serve-spa", "--serve-ssr"]
