import unittest
import os

from fastapi.testclient import TestClient
from backend.evercrow.main import app


class TestEndpoint(unittest.TestCase):

    def setUp(self) -> None:
        self.client = TestClient(app)
        self.test_file = os.path.join(os.path.dirname(__file__), 'test.pdf')
        self.test_invalid_file = os.path.join(os.path.dirname(__file__), 'test.txt')

    def test_root(self):
        """
        Testing the root url
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'Hello': 'World'})

    
    def test_pdf_upload(self):
        """
        Testing PDF upload
        """
        with open(self.test_file, 'rb') as pdf_file:
            response = self.client.post('/upload', files={'file': pdf_file})
            self.assertEqual(response.status_code, 200)
            birds = ['crow: 2', 'sparrow: 2', 'eagle: 2', 'robin: 2', 'hawk: 2', 'penguin: 2', 'flamingo: 2', 'owl: 2', 'hummingbird: 2']
            self.assertEqual(response.json(), birds)
    
    def test_invalid_pdf_upload(self):
        """
        Failing PDF upload
        """
        with open(self.test_invalid_file, 'rb') as test_file:
            response = self.client.post('/upload', files={'file': test_file})
            self.assertEqual(response.status_code, 400)

