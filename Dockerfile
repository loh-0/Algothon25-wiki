# Build stage
FROM python:3.11-slim AS builder
WORKDIR /app
COPY . /app
RUN pip install mkdocs mkdocs-material \
    && mkdocs build --clean

# Serve stage
FROM nginx:alpine
COPY --from=builder /app/site /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
