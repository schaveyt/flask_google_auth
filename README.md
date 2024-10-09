# Flask Google Authentication

This is a example of how to perform google auth with a flask application

## Google Cloud Console

In the APIs & Services section of the Google Cloud Console of your project, create a new OAuth Client ID.

1. Go to the Credentials tab
1. Click Create Credentials and select OAuth client ID
1. Select Web application
1. Enter a name for your application
1. Add the following authorized redirect URIs:
    - http://127.0.0.1:5000/authorize
1. Click Create
1. Copy the client ID and client secret and save them in a secure location

## Environment Variables

Create a .env file in the root directory of the project and add the following:

```
GOOGLE_CLIENT_ID=YOUR_CLIENT_ID
GOOGLE_CLIENT_SECRET=YOUR_CLIENT_SECRET
```

## Running the Application

To run the application, first activate your virtual environment and then run the following command:

```python
python app.py
```

Then open your browser and navigate to http://127.0.0.1:5000/

## References

- [Flask-Dance](https://flask-dance.readthedocs.io/en/latest/)
- [Authlib](https://authlib.org/)
- [Flask-OAuthlib](https://flask-oauthlib.readthedocs.io/en/latest/)