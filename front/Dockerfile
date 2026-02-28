# Étape 1: build
FROM node:20-alpine AS builder

WORKDIR /app

# Installer les dépendances
COPY front/package*.json ./
RUN npm ci

# Copier le code front et builder
COPY front/ ./
RUN npm run build

# Étape 2: serveur web
FROM nginx:1.27-alpine

# Copier le build statique dans nginx
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]