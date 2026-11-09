FROM python:3.12-slim
WORKDIR /work
COPY . .
CMD ["bash", "infra/scripts/pages.sh"]
