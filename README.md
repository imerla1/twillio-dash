# Implement an SMS Dashboard with Python and Twilio 

Full tutorial can be found here: 

This code sets up a Flask application that generates a table of data which
summarizes information about SMS messages received in a Twilio account.

This provides a starting point for building out a more fully-featured
dashboard.

## Getting Started

### Installing

```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

### Running locally

Create the `.env` for required config values:

```
(venv) $ cat .env 
TWILIO_ACCOUNT_SID=<account-sid>
TWILIO_AUTH_TOKEN=<auth-token>
```

Run the flask development server
```
(venv) $ flask run
```

Visit [localhost:5000/](localhost:5000/)

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [python-dotenv](https://github.com/theskumar/python-dotenv) - For config
* [Twilio Python](https://github.com/twilio/twilio-python) - For SMS 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

