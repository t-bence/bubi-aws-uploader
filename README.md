# bubi-aws-uploader

A minimal AWS Lambda function to download a file from a URL and upload it to an S3 bucket. Includes local testing and development setup with `uv`, `pytest`, and pre-commit hooks.

## Features

- Downloads a file from a configurable URL
- Uploads the file to a specified S3 bucket
- Uses environment variables for configuration
- Includes tests and linting

## Setup

1. **Clone the repo:**

   ```sh
   git clone <repo-url>
   cd bubi-aws-uploader
   ```

2. **Install dependencies:**

   ```sh
   uv venv
   uv pip install -r requirements.txt
   uv pip install -e .
   uv add pytest pre-commit ruff python-dotenv boto3
   pre-commit install
   ```

3. **Run tests:**

   ```sh
   uv run pytest
   ```

## Deployment

Package and deploy using AWS CLI:

```sh
zip function.zip lambda_function.py lib.py
aws lambda update-function-code \
  --function-name <your-lambda-name> \
  --zip-file fileb://function.zip
```

## Configure environment

Add the following env vars to the Lambda

   ```env
   TARGET_URL=https://example.com/file.txt
   S3_BUCKET=your-bucket-name
   ```

## Schedule

Set the following schedule: `cron(0 12 * * ? *)`

## Project Structure

```
├── lambda_function.py   # Lambda handler
├── lib.py               # Shared logic
├── tests/               # Pytest tests
├── .env                 # Environment config
├── .pre-commit-config.yaml
├── pyproject.toml
├── pytest.ini
├── .gitignore
```

## License

MIT
