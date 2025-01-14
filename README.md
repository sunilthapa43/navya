# navya

Project Set-up

1. Clone the repository: `git clone git@github.com:sunilthapa43/navya.git`
2. Change directory to the project root: `cd navya`
3. Create a virtual environment: `python -m venv .venv`
4. Activate the virtual environment:
    - On Windows: `.\.venv\Scripts\activate`
    - On macOS and Linux: `source .venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Create a `.env` file in the project root and add the following environment variables:
    ```
    DEBUG=True
    SECRET_KEY=your_secret_key
   ```
7. Run the migrations: `python manage.py migrate`
8. Create a superuser: `python manage.py createsuperuser`
9. Run the development server: `python manage.py runserver your_port`
10. Access the Swagger API documentation at `http://localhost:your_port`

Guidelines
JWT Authentication is used for the API authentication. On the Swagger UI, fill in the access token you get from the token obtain API in the "Authorize" button on the top right corner.
Example:
```
POST /api/token/
{
  "username": "uname",
  "password": "pass"
}
```
This will return an access token. Copy the token and paste it in the "Value" field in the "Bearer" field in the "Authorize" button on the top right corner of the Swagger UI.
Example:
```Bearer <access_token_from_token_endpoint_response>```