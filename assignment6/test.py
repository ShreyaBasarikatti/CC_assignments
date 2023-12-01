import webapp2
import json
from google.appengine.ext import ndb
import requests

class MainPage(webapp2.RequestHandler):
    def get(self):
        with open('index.html', 'r') as file:
            html_content = file.read()
        self.response.out.write(html_content)

    def post(self):
        data_json = json.loads(self.request.body)
        action = data_json.get('action')

        if action == 'create_account':
            signup_email = data_json.get('signupEmail')
            signup_password = data_json.get('signupPassword')

            user = User(email=signup_email, data={})
            user.put()

            firebase_url = 'https://www.gstatic.com/firebasejs/10.7.0/firebase-auth.js'
            firebase_data = {'email': signup_email, 'user_data': {}}
            requests.post(firebase_url, json=firebase_data)

            self.response.write('Account created successfully')

        elif action == 'login':
            email = data_json.get('email')
            password = data_json.get('password')
            self.response.write('Login successful')    
app= webapp2.WSGIApplication([('/',MainPage)],debug=True)

