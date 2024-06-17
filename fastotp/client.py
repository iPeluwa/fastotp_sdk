import httpx
from .exceptions import FastOTPError

class FastOTPClient:
    BASE_URL = "https://api.fastotp.co"

    def __init__(self, api_key: str):
        """
        Initializes the FastOTPClient with the provided API key.

        :param api_key: API key for authenticating requests to the FastOTP API.
        """
        self.api_key = api_key
        self.client = httpx.Client()

    def _headers(self):
        """
        Returns the headers required for authenticating requests.

        :return: Dictionary containing the headers.
        """
        return {"Content-Type": "application/json", "X-api-key": self.api_key}

    def generate_otp(self, payload: dict):
        """
        Generates an OTP based on the provided payload.

        :param payload: Dictionary containing the OTP generation parameters.
        :return: Response from the API as a dictionary.
        :raises FastOTPError: If the API request fails.
        """
        url = f"{self.BASE_URL}/generate"
        response = self.client.post(url, json=payload, headers=self._headers())
        if response.status_code != 200:
            raise FastOTPError(response.json().get("message"))
        return response.json()

    def validate_otp(self, payload: dict):
        """
        Validates an OTP based on the provided payload.

        :param payload: Dictionary containing the OTP validation parameters.
        :return: Response from the API as a dictionary.
        :raises FastOTPError: If the API request fails.
        """
        url = f"{self.BASE_URL}/validate"
        response = self.client.post(url, json=payload, headers=self._headers())
        if response.status_code != 200:
            raise FastOTPError(response.json().get("message"))
        return response.json()

    def get_otp(self, otp_id: str):
        """
        Retrieves the details of an OTP based on its ID.

        :param otp_id: ID of the OTP to retrieve.
        :return: Response from the API as a dictionary.
        :raises FastOTPError: If the API request fails.
        """
        url = f"{self.BASE_URL}/{otp_id}"
        response = self.client.get(url, headers=self._headers())
        if response.status_code != 200:
            raise FastOTPError(response.json().get("message"))
        return response.json()
