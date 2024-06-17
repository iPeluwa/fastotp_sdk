import unittest
from fastotp import FastOTPClient, FastOTPError

class TestFastOTPClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Set up the FastOTPClient and generate an OTP for testing.
        """
        cls.api_key = input("Enter your API key: ")
        cls.client = FastOTPClient(cls.api_key)
        cls.otp_id = None
        cls.identifier = input("Enter the identifier (email or phone): ")
        cls.otp = None

        otp_type = input("Enter OTP type (numeric, alpha, alpha_numeric): ")

        # Generate OTP
        payload = {
            "type": otp_type,
            "identifier": cls.identifier,
            "delivery": {"email": cls.identifier},
            "validity": 123,
            "token_length": 6,
        }
        response = cls.client.generate_otp(payload)
        if "otp" in response:
            cls.otp_id = response["otp"]["id"]
            print(f"Generated OTP ID: {cls.otp_id}")
        else:
            raise FastOTPError("Failed to generate OTP")

    def test_generate_otp(self):
        """
        Test that the OTP is generated successfully.
        """
        self.assertIsNotNone(self.otp_id, "OTP ID should not be None")

    def test_validate_otp(self):
        """
        Test that the OTP can be validated successfully.
        """
        otp = input("Enter the OTP received via email: ")
        payload = {
            "token": otp,
            "identifier": self.identifier
        }
        response = self.client.validate_otp(payload)
        self.assertIn("otp", response)
        self.assertEqual(response['otp']['status'], 'validated')

    def test_get_otp(self):
        """
        Test that the OTP details can be retrieved successfully.
        """
        response = self.client.get_otp(self.otp_id)
        self.assertIn("otp", response)
        print(f"Retrieved OTP: {response['otp']}")

    @classmethod
    def tearDownClass(cls):
        """
        Print a completion message after all tests have run.
        """
        print("Tests completed.")

if __name__ == "__main__":
    unittest.main()
