from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

	# Ensure that flask was setup correctly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/test')
		self.assertEqual(response.status_code, 200)

	# Ennsure that the login page loads correctly
	def test_login_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertTrue(b'Please login' in response.data)

	# Ensure that user logs in with correct account
	def test_correct_login(self):
		tester = app.test_client(self)
		response = tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects = True)
		self.assertIn(b'You were logged in', response.data)

	# Ensure incorrect login
	def test_incorrect_login(self):
		tester = app.test_client(self)
		response = tester.post('/login', data=dict(username="adminoin", password="adalj"), follow_redirects = True)
		self.assertIn(b'Invalid credentials. Please try again', response.data)

	# Ensure that user logs out
	def test_correct_logout(self):
		tester = app.test_client(self)
		tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects = True)
		response = tester.get('/logout', follow_redirects = True)
		self.assertIn(b'You were logged out', response.data)	
		
	# Ensure main paige returns login page
	def test_main_page_returns_login(self):
		tester = app.test_client(self)
		response = tester.get('/', follow_redirects = True)
		self.assertTrue(b'You need to login first' in response.data)

	# Ensure posts is on the page after login
	def test_posts_shows_up(self):
		tester = app.test_client(self)
		response = tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects = True)
		self.assertIn(b'Bonjour from French', response.data)

if __name__ == '__main__':
	unittest.main()