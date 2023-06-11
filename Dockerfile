ARG value=1
FROM python:3.12.0a6-alpine

ENV test_env=2

COPY . .

ENTRYPOINT ["python3"]
CMD ["operations_binary.py"]