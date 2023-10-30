<h1>Multi Vendor Ecommerce API</h1>
This project has used Django and Django rest-framewok to implement the features of a E-commerce API.
The project is dockerized so installion will be easy.

just open a terminal in the project folder and paste the command below.

```
sudo docker-compose build
sudo docker-compose up
```
<hr>

<h1>How it was made</h1>
The project is seperated into apps which are named after the features written inside them.
By using the Django's default preffered app structure, this code has been scaleable, and readable.
Inside User app there is managers.py file, authentication.py file and a custom user in the models. This helps new-comers in django understand the basic of authentication in django.

<h1>APIs User</h1>
|Name          | endpoint       | fields                    | methods |
|--------------|----------------|---------------------------|---------|
|User register | /api/register/ | username, email, password | POST    |
|User login    | /api/login/    | username, password        | POST    |
|forgot pass   | /api/forgot-password/| email | POST  |
| Auth test    | /api/isauth/         | None  | GET   |

for Auth test you need to use the JWT returned after login.
put it in a Header AUTH : JWT YOUROWNJWTKEY

