from django.test import TestCase, Client
from django.urls import reverse


class ButterTests(TestCase):
    def setUp(self):
        self.client =Client()
    def test_user_can_get_agreement(self):
        response =self.client.get('/butter/agreement/')
        self.assertEqual(response.status_code, 200)
    
    def test_user_can_sign_agreement(self):
        data = {"first_name": "first",
                "last_name": "last",
                "email": "first@gmail.com",
                "password": "1234567890vtytx",
                "street": "kampala",
                "post_code": "0000"}
        response =self.client.post('/butter/sign_agreement/', data=data)
        self.assertEqual(response.status_code, 201)
    
    def test_user_can_get_signed_agreement(self):
        data = {"first_name": "first1",
                "last_name": "last1",
                "email": "first1@gmail.com",
                "password": "1234567890vtytx",
                "street": "kampala",
                "post_code": "0000"}
        user_response =self.client.post('/butter/sign_agreement/', data=data)
        response =self.client.get('/butter/agreement/',HTTP_AUTHORIZATION=user_response.data["token"])
        self.assertEqual(response.status_code, 200)
