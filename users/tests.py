from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class UserAuthTests(TestCase):
    def setUp(self):
        # Configuración previa a las pruebas, se ejecuta antes de cada prueba.
        self.client = Client()
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_view_get(self):
        # Verifica que la vista de login responde correctamente a una solicitud GET.
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_view_post_success(self):
        # Verifica que un usuario puede iniciar sesión con credenciales válidas.
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)  # Redirecciona a la página de inicio.
        self.assertRedirects(response, reverse('home'))
        self.assertIn('_auth_user_id', self.client.session)  # Verifica que el usuario está autenticado.

    def test_login_view_post_failure(self):
        # Verifica que un usuario no puede iniciar sesión con credenciales inválidas.
        response = self.client.post(reverse('login'), {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # Debe renderizar la misma página.
        self.assertContains(response, "Usuario o contraseña incorrectos")

    def test_register_view_get(self):
        # Verifica que la vista de registro responde correctamente a una solicitud GET.
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_view_post_success(self):
        # Verifica que un usuario puede registrarse correctamente.
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertEqual(response.status_code, 302)  # Redirecciona a la página de inicio.
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(User.objects.filter(username='newuser').exists())  # Verifica que el usuario ha sido creado.

    def test_register_view_post_failure(self):
        # Verifica que no se puede registrar un usuario con contraseñas que no coinciden.
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'password1', 'password2': 'password2'})
        self.assertEqual(response.status_code, 200)  # Debe renderizar la misma página.
        self.assertContains(response, "This field is required")  # Verifica que muestra un error de formulario.
