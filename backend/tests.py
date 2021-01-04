import unittest
from login import create_app
import secrets
from login import models


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            models.db.create_all()

            self.user_data = {
                'username': 'test',
                'password': '123456',
                'email': 'test@email.com',
            }

            user = models.User(**self.user_data)
            user.save()
            self.user = user

    def test_register(self):
        data = {
            'username': secrets.token_urlsafe(8),
            'email': f'{secrets.token_urlsafe(8)}@gmail.com',
            'password': secrets.token_urlsafe(8)
        }

        res = self.client.post('/user', json=data)
        self.assertEqual(201, res.status_code, res.get_data())

    def test_login(self):
        res = self.client.post(
            '/session',
            json={'username': self.user_data['username'],
                  'password': self.user_data['password']})
        self.assertEqual(201, res.status_code)

    def test_logout(self):
        res = self.client.post(
            'session',
            json={'username': self.user_data['username'],
                  'password': self.user_data['password']}
        )
        access_token = res.json['access_token']

        res = self.client.delete(
            '/session',
            headers={'Authorization': f'Bearer {access_token}'},
        )
        self.assertEqual(201, res.status_code)

    def test_set_password(self):
        res = self.client.post(
            'session',
            json={'username': self.user_data['username'],
                  'password': self.user_data['password']}
        )
        access_token = res.json['access_token']
        res = self.client.put(
            '/user',
            json={'current_password': self.user_data['password'],
                  'new_password': '123456'},
            headers={'Authorization': f'Bearer {access_token}'},
        )
        self.assertEqual(201, res.status_code)

    def test_get_user(self):
        res = self.client.post(
            '/session',
            json={'username': self.user_data['username'],
                  'password': self.user_data['password']}
        )
        access_token = res.json['access_token']
        res = self.client.get('/user', headers={'Authorization': f'Bearer {access_token}'})
        self.assertEqual(201, res.status_code)


if __name__ == '__main__':
    unittest.main()
