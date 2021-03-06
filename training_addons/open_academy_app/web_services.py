import functools
import xmlrpc.client

HOST = 'localhost'
PORT = 8069
DB = '2023t'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# 1. Login
uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print("Logged in as %s (uid:%d)" % (USER, uid))

call = functools.partial(
    xmlrpc.client.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# 2. Read the sessions
sessions = call('session', 'search_read', [], ['name', 'seats'])
for session in sessions:
    print("Session %s (%s seats)" % (session['name'], session['seats']))
# 3.create a new session
session_id = call('session', 'create', {
    'name': 'My session',
    'course_id': 2,
})
# 3.create a new session for the "Functional" course
course_id = call('course', 'search', [('name', 'ilike', 'Functional')])[0]
session_id = call('session', 'create', {
    'name': 'My session',
    'course_id': course_id,
})
