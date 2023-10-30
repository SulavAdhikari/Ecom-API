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
The uploaded files are stored in media folder, with well managed file structure being

/media/uploads/product/product:slug/image.jpg

while using this we can now add a new folder for User profile, without storing all files in oone folder 

A thing to Note is that this will run properly only on debug mode,
We can either use a workaround
 https://github.com/SulavAdhikari/DjangoMediaDisplayFixConcept
 or a cloud storage server



## API Endpoints

| Name           | Endpoint               | Fields                    | Methods |
|----------------|------------------------|---------------------------|---------|
| User register  | `/api/register/`       | username, email, password | POST    |
| User login     | `/api/login/`          | username, password        | POST    |
| Forgot pass    | `/api/forgot-password/`| email                     | POST    |
| Auth test      | `/api/isauth/`         | None                      | GET     |


for Auth test you need to use the JWT returned after login.
put it in a Header AUTH : JWT YOUROWNJWTKEY


## Seller Dashboard API Endpoints

| Name           | Endpoint                                  | Methods |
|----------------|-------------------------------------------|---------|
| Product Upload | `/seller_dashboard/upload/`               | POST    |
| Product Edit   | `/seller_dashboard/edit/<slug:slug>/`     | PUT, PATCH   |
| Product Delete | `/seller_dashboard/delete/<slug:slug>/`   | DELETE  |
| Make Unavailable | `/seller_dashboard/make-unavailable/<slug:slug>/` | POST |
| Make Available | `/seller_dashboard/make-available/<slug:slug>/` | POST   |
| Product List   | `/seller_dashboard/list/`                 | GET     |
| Seller Create  | `/seller_dashboard/create/`               | POST    |
| Seller Update  | `/seller_dashboard/<int:id>/`             | PUT   |
| Seller Delete  | `/seller_dashboard/<int:id>/delete/`      | DELETE  |

All of the above endpoint requires Authentication

## Products API Endpoints

| Name                          | Endpoint                                   | Methods |
|-------------------------------|--------------------------------------------|---------|
| Available Products            | `/products/available/`                     | GET     |
| User's Available Products     | `/products/user/<str:username>/`           | GET     |
| Products in Price Range       | `/products/price-range/`                   | GET     |
| Search Products               | `/products/search/`                        | GET     |
| Product by Slug               | `/products/<slug:slug>/`                   | GET     |
| Products in Date Range        | `/products/date-range/`                    | GET     |


## Shopping and Payment API Endpoints

| Name               | Endpoint               | Methods |
|--------------------|------------------------|---------|
| Add to Cart        | `/cart/add/`           | POST    |
| Checkout           | `/checkout/`           | POST |
| Payment            | `/payment/`            | POST    |

## Reviews API Endpoints

| Name                       | Endpoint                             | Methods |
|----------------------------|--------------------------------------|---------|
| Create Review              | `/create/`                           | POST    |
| Product Reviews            | `/product/<int:product_id>/reviews/` | GET     |
