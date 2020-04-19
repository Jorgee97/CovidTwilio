<a  href="https://www.twilio.com">
<img  src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg"  alt="Twilio"  width="250"  />
</a>
 
# Covid-19 Colombia Twilio

## About

Hey everyone, my partner [Andrea](https://github.com/AndreaMelendez) and I build a WhatsApp bot which brings useful information about the people that is infected by Covid-19 in our country Colombia.  

[Dev.to Post](https://dev.to/andreamelende12/bot-whatsapp-covid19-colombia-42ic) that shows up the bot
### How it works

The application uses the Twilio's WhatsApp API for sending information to the user based on a menu that we designed.

## Features

- Flask Web server
- MongoDB Database
- Web Scrapping

## How to use it

The usage is shown in the [Dev.to post](https://dev.to/andreamelende12/bot-whatsapp-covid19-colombia-42ic)

## Set up

### Requirements

- [Docker](https://www.docker.com/) or [Flask](https://flask.palletsprojects.com/en/1.1.x/) for local dev
- A Twilio account - [sign up](https://www.twilio.com/try-twilio)
- A Twilio WhatsApp SandBox
- A [MongoDB](https://www.mongodb.com/) Free Tier at Atlas or Local
- [Ngrok](https://ngrok.com/) for local testing

### Local development

After the above requirements have been met:

1. Clone this repository and `cd` into it

```bash
git clone git@github.com:Jorgee97/CovidTwilio.git
cd CovidTwilio
```

2. Create a virtualenv and activate

```bash
python3 -m venv .env
source .env/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Set environmental variables
```bash
export FLASK_APP=app
export FLASK_DEBUG=1
```

5. Run the application

```bash
flask run
```

6. Run ngrok to expose your api
```bash
./ngrok http 5000
```

7. Add the ngrok Forwarding URL to your WhatsApp sandbox

That's it!

### Cloud deployment

There is a Dockerfile attached to this repository that you can build and deploy wherever it fits best for your purposes.
You can build your image using the Dockerfile like:
```bash
docker build -t covidtwilio:tag .
```

## Resources

- [Api Open Data Colombia](https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr/data)
- [Movies and Series (Data Scrapping)](http://finde.latercera.com)

## Contributing

This project is Open Source and we are open for contributions :smile:

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.

