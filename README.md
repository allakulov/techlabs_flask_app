# Cats vs Dogs Classifier

Takes in the input as a list of animal names and creates a model which is later used for identifying the name of animal given it's picture . Currently, the list of animals taken are cats and dogs .

This project uses fastai utils in combination with bing-search api to download the images which are later used to train the cnn-classifier . 

### Cloning the repo :
```bash
git clone git@github.com:rama96/animals_prediction.git
```

### Creating virtual environment
```bash
virtualenv -p python3.8 env
source env/bin/activate
```

### Adding env variables
Create a .env file and add your python path and Microsoft azure_key to the same . Run the below commands to add get your .env added to your environment

```bash
printf "\n# Adding this command to read local .env file" >> env/bin/activate 
printf "\nexport $(grep -v '^#' .env | xargs)" >> env/bin/activate
```

### Installing Requirements

Please run the following commands to install the requirements/dependencies
```bash
source env/bin/activate
pip install -r requirements.txt
```

## Application Usage

<p><b>app.py</b>  is the web application developed using flask to make use of the trained model (<b>animals_prediction.pkl</b>) to predict the label of the uploaded image .  <p>

To fire up the application , run the below command
```bash
python app.py
```

<p> Once the application is fired up , it will be hosted in the following link  http://127.0.0.1:5000/ <p>


## Development 

### Data Creation 

<p><b>prepare.py</b> creates the data by crawling through the bing search engine to geneate/download the data required for training purposes. </p> 

```bash
python prepare.py
```

### Processesing and Training the model

<p><b>process.py</b> trains the images and outputs the model in the root of dir as <b>animals_prediction.pkl</b> <p>

```bash
python process.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)