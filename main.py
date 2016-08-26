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
class MainHandler(webapp2.RequestHandler):
    form = """
        <form action="/" method="post">
            <label>
                Username
                <input type="text"/>
                <input name="Username" value = %(username)s>
                <div style="color: red">%(error)s</div>
            </label>
            <br>
            <label>
                Password
                <input type="password"/>
            </label>
            <br>
            <label>
                Verify Password
                <input type="password">
            </label>
            <br>
            <label>
                Email(Optional)
                <input type="text">
            </label>
            <br>
            <input type="submit">
        </form>
        """
    #def write_form(self, error="")
        #self.response.write(form % {"error": error})

    def get(self):
        self.response.write(self.form)
        #self.write_form()

    def post(self):
        self.response.write("Thank you")
        self.write_form("Error Boy!")




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
