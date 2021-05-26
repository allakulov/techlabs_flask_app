# animals_prediction
Takes in the input as a list of animal names and creates a model which is later used for identifying the name of animal given it's picture .

# creating virtualenv 
virtualenv -p python3.8 env
source env/bin/activate

# adding env variables
printf "\n# Adding this command to read local .env file" >> env/bin/activate 
printf "\nexport $(grep -v '^#' .env | xargs)" >> env/bin/activate

