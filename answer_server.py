# Copyright Skullspace, 2014
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved. This file is offered as-is,
# without any warranty.
# http://www.gnu.org/prep/maintain/html_node/License-Notices-for-Other-Files.html
# @author Jay Smith <jayvsmith@gmail.com>

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT = 80

class AnswerRequestHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('content_type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        self.do_HEAD()
        self.wfile.write(self.server.current_answer)

    def log_message(self, format, *args):
        return

class AnswerServer(HTTPServer):
    def __init__(self):
        HTTPServer.__init__(self, ('',PORT), AnswerRequestHandler)
        self.current_answer = "None Yet"
