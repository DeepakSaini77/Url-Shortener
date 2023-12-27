import unittest
from main import app

class TestURLShortener(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'URL Shortener Service is running.')

    def test_generate_hashed_url(self):
        response = self.app.post('/generate', json={'long_url': 'https://www.google.com'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('hashed_url', data)

    def test_click_tracking(self):
        response_generate = self.app.post('/generate', json={'long_url': 'https://www.google.com'})
        data_generate = response_generate.get_json()

        response_click = self.app.get(f'/{data_generate["hashed_url"].split("/")[-1]}')
        self.assertEqual(response_click.status_code, 302) 

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
