
# FastOTP SDK Documentation

## Overview

The FastOTP SDK is a Python library for interacting with the FastOTP API. It supports various frameworks including Django, FastAPI, and Flask. This SDK allows you to generate, validate, and retrieve OTPs (One-Time Passwords) easily.

## Installation

To install the FastOTP SDK, use pip:

```bash
pip install fastotp_sdk
```

## Configuration

You need an API key to authenticate your requests. You can find your API key in the FastOTP Dashboard.

## Usage

### Importing the SDK

To use the SDK, import the `FastOTPClient` class from the `fastotp` module and instantiate it with your API key.

```python
from fastotp import FastOTPClient

api_key = "your_api_key"
client = FastOTPClient(api_key)
```

### Generating an OTP

To generate an OTP, use the `generate_otp` method. Provide a dictionary with the necessary payload.

```python
payload = {
    "type": "numeric",
    "identifier": "user@example.com",
    "delivery": {"email": "user@example.com"},
    "validity": 123,
    "token_length": 6,
}
response = client.generate_otp(payload)
print(response)
```

### Validating an OTP

To validate an OTP, use the `validate_otp` method. Provide a dictionary with the token and identifier.

```python
payload = {
    "token": "123456",
    "identifier": "user@example.com"
}
response = client.validate_otp(payload)
print(response)
```

### Retrieving an OTP

To retrieve an OTP by its ID, use the `get_otp` method.

```python
otp_id = "some-otp-id"
response = client.get_otp(otp_id)
print(response)
```

## Framework-Specific Examples

### Django Example

Create a view to generate an OTP in your Django project.

```python
from django.http import JsonResponse
from fastotp import FastOTPClient

api_key = "your_api_key"
client = FastOTPClient(api_key)

def generate_otp(request):
    payload = {
        "type": "numeric",
        "identifier": "user@example.com",
        "delivery": {"email": "user@example.com"},
        "validity": 123,
        "token_length": 6,
    }
    response = client.generate_otp(payload)
    return JsonResponse(response)
```

### FastAPI Example

Create an endpoint to generate an OTP in your FastAPI project.

```python
from fastapi import FastAPI
from fastotp import FastOTPClient

app = FastAPI()
api_key = "your_api_key"
client = FastOTPClient(api_key)

@app.post("/generate-otp/")
async def generate_otp(payload: dict):
    return client.generate_otp(payload)
```

### Flask Example

Create a route to generate an OTP in your Flask project.

```python
from flask import Flask, request, jsonify
from fastotp import FastOTPClient

app = Flask(__name__)
api_key = "your_api_key"
client = FastOTPClient(api_key)

@app.route("/generate-otp", methods=["POST"])
def generate_otp():
    payload = request.json
    return jsonify(client.generate_otp(payload))

if __name__ == "__main__":
    app.run()
```

## Error Handling

The SDK raises a `FastOTPError` exception for any errors returned by the FastOTP API.

```python
try:
    response = client.generate_otp(payload)
except FastOTPError as e:
    print(f"Error: {e}")
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any issues or questions, please contact [your_email@example.com](mailto:your_email@example.com).
