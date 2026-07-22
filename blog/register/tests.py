from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class LogoutPageTests(TestCase):
    def test_logout_renders_logout_page(self):
        user = User.objects.create_user(username='tester', password='secret123')
        self.client.force_login(user)

        response = self.client.post(reverse('logout'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logoutPage.html')
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_login_page_renders_even_for_authenticated_users(self):
        user = User.objects.create_user(username='tester2', password='secret123')
        self.client.force_login(user)

        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'loginPage.html')

    def test_home_page_renders_for_anonymous_users(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_root_url_opens_login_page(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'loginPage.html')

    def test_signup_creates_user_and_redirects_to_login(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'StrongPass123',
            'password2': 'StrongPass123',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        self.assertRedirects(response, reverse('login'))

    def test_record_page_provides_add_navigation(self):
        user = User.objects.create_user(username='recorduser', password='secret123')
        self.client.force_login(user)

        response = self.client.get(reverse('record'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse('home'))

    def test_add_lead_post_with_empty_form_does_not_crash(self):
        user = User.objects.create_user(username='adduser', password='secret123')
        self.client.force_login(user)

        response = self.client.post(reverse('add_lead'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_login_authenticates_existing_user(self):
        User.objects.create_user(username='existing', email='existing@example.com', password='StrongPass123')

        response = self.client.post(reverse('login'), {
            'username': 'existing',
            'password': 'StrongPass123',
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)
