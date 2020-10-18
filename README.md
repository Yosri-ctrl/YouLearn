# Running
To run the server use the following commands:
 - open venv :
 ```
 source venv/bin/activate
 ```
 - run server :
 ```
 ./youlearn.py
 ```

# API Documentation
# Register a new user:
The body must contain a JSON object that defines email, password, name, lastname, telephone fields.
On success a status code 201 is returned. The body of the response contains a JSON object with the newly added user id. A Location header contains the URI of the new user.
On failure status code 400 (bad request) is returned.
- example :
```
$ curl -i -X POST -H "Content-Type:application/json" -d '{"email":"youlearn@email.com","password":"youlearn", "name":"you","lastname":"learn","telephone":"69696969"}' http://127.0.0.1:5000/api/users
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 14
Location: http://127.0.0.1:5000/api/users/2
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Sun, 18 Oct 2020 14:08:10 GMT
{
  "id": 2
}
```
# Return a user:
On success a status code 200 is returned. The body of the response contains a JSON object with the requested user.
On failure status code 400 (bad request) is returned.
- example :
```
curl -i -X GET http://127.0.0.1:5000/api/users/2
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 104
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Sun, 18 Oct 2020 14:24:16 GMT

{
  "email": "youlearn@email.com", 
  "lastname": "learn", 
  "name": "you", 
  "telephone": 69696969
}
```
# Return an authentication token:
This request must be authenticated using a HTTP Basic Authentication header.
On success a JSON object is returned with a field token set to the authentication token for the user and a field duration set to the (approximate) number of seconds the token is valid.
On failure status code 401 (unauthorized) is returned.
- example :
```
curl -u youlearn@email.com:youlearn -i -X GET http://127.0.0.1:5000/api/token
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 183
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Sun, 18 Oct 2020 14:27:54 GMT

{
  "token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMzAzMTI3NCwiZXhwIjoxNjAzMDMxODc0fQ.eyJpZCI6Mn0.erm1Oc6FuZrscAYk61WIIP4IxaD7BYWswmePc9RdP3yyK_wn5fh151T0pHVqfus0xUub8NALB0Bp2SvhIKeK2w"
}
```
# Return a protected resource: (ex: courses, profile...)
This request must be authenticated using a HTTP Basic Authentication header. Instead of email and password, the client can provide a valid authentication token in the email field. If using an authentication token the password field is not used and can be set to any value.
On success a JSON object with data for the authenticated user is returned.
On failure status code 401 (unauthorized) is returned.
- example:
```
curl -u youlearn@email.com:youlearn -i -X GET http://127.0.0.1:5000/api/resource
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 28
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Sun, 18 Oct 2020 14:29:42 GMT

{
  "data": "Hello, you!"
}
```
- with token :
```
curl -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMzAzMTI3NCwiZXhwIjoxNjAzMDMxODc0fQ.eyJpZCI6Mn0.erm1Oc6FuZrscAYk61WIIP4IxaD7BYWswmePc9RdP3yyK_wn5fh151T0pHVqfus0xUub8NALB0Bp2SvhIKeK2w: -i -X GET http://127.0.0.1:5000/api/resource
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 28
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Sun, 18 Oct 2020 14:30:50 GMT

{
  "data": "Hello, you!"
}
```