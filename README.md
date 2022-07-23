## Deployment of the image classification DL model for techlabs Berlin project titled
# "Beautify Berlin"

## Running the app locally
You can run the app locally running the following commands in the terminal 

### Clone the repo
```bash
git clone https://github.com/allakulov/techlabs_flask_app
```

### Set up a Python virtual environment (if it doesn't exist)
```bash
sudo apt install python3.8-venv
sudo apt-get update python3.8-venv
```

### Create a virtual environment
```bash
sudo python3 -m venv venv
source venv/bin/activate
```

### Install requirements

Please run the following commands to install the requirements/dependencies
```bash
pip install -r requirements.txt
```

### Launch application locally

```bash
python app.py
```

## Deploy the app on Heroku

### Create a Procfile in the main directory with the following line
```bash
web: gunicorn wsgi:app
```

### Create a wsgi.py file with the following line
```bash
from main import app

if __name__ == “__main__”: 
    app.run()
```
### Install Heroku CLI by following the instruction in this link
https://devcenter.heroku.com/articles/heroku-cli


### Initialize a git repository, add and commit files
```bash
git init 
git add .
git commit -m "Initial commit"
```
### Log in to Heroku CLI
```bash
heroku login
```

### Create an app on Heroku 
```bash
heroku create <choose-app-name>
```

### Push files to Heroku remote
```bash
git push heroku master
```

Once your files are successfully pushed to Heroku, it will take a few minutes for the app to be built and launched. 