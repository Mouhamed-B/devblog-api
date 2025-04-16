from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Post  # Import your Post model

class PostAPITestCase(APITestCase):
    def setUp(self):
        # Create a user and generate tokens
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

        # Add Authorization header with Bearer token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        # Create a sample post
        self.post = Post.objects.create(title="Sample Post", content="This is a sample post.", author=self.user)
        self.post_url = f'/api/posts/{self.post.id}/'  # Update URL based on your API endpoint

    def test_create_post(self):
        data = {
            "title": "New Post",
            "content": "This is a new post.",
        }
        response = self.client.post('/api/posts/', data)  # Update the URL based on your API endpoint
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    def test_get_post_list(self):
        response = self.client.get('/api/posts/')  # Update the URL based on your API endpoint
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_get_post_detail(self):
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)

    def test_update_post(self):
        data = {
            "title": "Updated Title",
            "content": "Updated content.",
        }
        response = self.client.put(self.post_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])

    def test_delete_post(self):
        response = self.client.delete(self.post_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthorized_access(self):
        # Remove credentials to simulate unauthorized access
        self.client.credentials()
        data = {
            "title": "Updated Title 2",
            "content": "Updated content 2.",
        }
        response = self.client.put(self.post_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)