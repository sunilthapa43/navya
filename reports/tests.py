from rest_framework.test import APITestCase

from mutual_funds.models import MutualFund


class ReportsAPITest(APITestCase):
    def setUp(self):
        self.register_url = 'http://localhost:8000/api/auth/register/'
        self.token_url = 'http://localhost:8000/api/auth/token/'

        self.user_data = {
            'email': 'test_api@gmail.com',
            'username': 'test_api',
            'password': 'Test@12345'
        }

        self.client.post(self.register_url, self.user_data)
        response = self.client.post(self.token_url, {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        self.access_token = response.data['data']['access']

        # create a mutual fund
        MutualFund.objects.create(
            name='Mutual Fund 1',
            fund_type='Equity',
            symbol='MF1',
            nav=2532551.22
        )

    # now hit investment endpoint post
    def test_investment_endpoint(self):
        investment_url = 'http://localhost:8000/api/investments/'
        response = self.client.post(investment_url, {
            "mutual_fund": 1,
            "units": 100
        }, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data['success'])
        self.assertIn('data', response.data)
        self.assertIn('mutual_fund', response.data['data'])

    def test_reports_endpoint(self):
        reports_url = 'http://localhost:8000/api/reports/'
        response = self.client.get(reports_url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['success'])
        self.assertIn('data', response.data)

    def test_mutual_fund_creation_by_non_admin(self):
        mutual_fund_url = 'http://localhost:8000/api/mutual-fund/'
        response = self.client.post(mutual_fund_url, {
            "name": "Mutual Fund 2",
            "fund_type": "Debt",
            "symbol": "MF2",
            "nav": 123.45
        }, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        print(response)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(response.data['success'])
        self.assertIn('error', response.data)
        self.assertIn('You are not authorized to perform this action', response.data['error'])

