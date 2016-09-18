#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

form = """
    <form action="/" method="post">
        <label>
            Username
            <input type="text" name = "user_name" value = "%(user_name)s"/>%(error_username)s

        </label>
        <br>
        <label>
            Password
            <input type="password" name="password" value = "%(password)s"/>%(error_password)s
        </label>
        <br>
        <label>
            Verify Password
            <input type="password" name="verify" value = "%(verify)s"/>%(error_verify)s

        </label>
        <br>
        <label>
            Email(Optional)
            <input type="text" name="email" value = "%(email)s"/>%(error_email)s
        </label>
        <br>
        <input type="submit">
    </form>
    """
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(user_name):
    return user_name and USER_RE.match(user_name)

PASSWORD_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASSWORD_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
    return email and EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def page_form(self, error_username="", user_name="", error_password="",
        password="", error_verify="", verify="", error_email="",  email=""):
        self.response.write(form %{'error_username': error_username,
                                    "user_name":user_name,
                                    "error_password":error_password,
                                    "error_verify": error_verify,
                                    "email": email,
                                    "password":password,
                                    "verify":verify,
                                    "error_email":error_email
                                    })

    def get(self):
        self.page_form()

    def post(self):
        have_error = False
        user_name = self.request.get("user_name")
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        error_username, error_password, error_verify, error_email = "", "", "", "",

        if not valid_username(user_name):
            error_username = "You've run into a little issue"
            have_error = True

        if not valid_password(password):
            error_password = "You've run into a little issue"
            have_error = True

        elif password != verify:
            error_verify = "You've run into a little issue"
            have_error = True

        if not valid_email(email):
            error_email = "You've run into a little issue"
            have_error = True

        self.page_form(error_username=error_username,error_password=error_password,error_verify=error_verify,error_email=error_email)

        if not have_error:
            self.redirect('/Welcome?user_name={}'.format(user_name))



class Welcome(webapp2.RequestHandler):
    def get(self):
        user_name = self.request.get("user_name")
        self.response.write("Welcome " + user_name + "! " + "You are the one.")




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Welcome', Welcome)
], debug=True)
