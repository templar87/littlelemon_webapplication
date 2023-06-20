API endpoints to test with insomina

Testing: Get

http://127.0.0.1:8000/admin/

Username: admin
password: LittleLemon123!

http://127.0.0.1:8000/restaurant/

http://127.0.0.1:8000/restaurant/menu

http://127.0.0.1:8000/restaurant/menu/1

Testing: Post

http://127.0.0.1:8000/restaurant/menu/


Testing: Put

http://127.0.0.1:8000/restaurant/menu/7

Testing: Delete

http://127.0.0.1:8000/restaurant/menu/7

To confirm Delete

Get with http://127.0.0.1:8000/restaurant/menu

Testing: TokenAuthentication 

http://127.0.0.1:8000/restaurant/api-token-auth/

select Post, Multipart

In the body: 
username: admin
password: LittleLemon123!

