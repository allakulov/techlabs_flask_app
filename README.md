# Cats vs Dogs Classifier

Takes in the input as a list of animal names and creates a model which is later used for identifying the name of animal given it's picture . Currently, the list of animals taken are cats , dogs .

This project uses fastai utils in combination with bing-search api to download the images which are later used to train the cnn-classifier . 

## Usage 

Start by Cloning the directory .

```bash
python prepare.py
```

## For Development 

### Cloning the repo :
```bash
git clone git@github.com:rama96/animals_prediction.git
```

### Creating virtualenv 
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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)