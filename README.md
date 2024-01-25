PockemonDB
PockemonDB is a Python script designed to collect Pokémon data from the PokeAPI website and store it in an AWS DynamoDB database. This README provides an overview of the project, setup instructions, usage guidelines, and other important details.

Table of Contents
Overview
Prerequisites
Setup
Usage
Functionality
Contributing
License
Acknowledgements
Support
Overview
PockemonDB is a Python script that leverages the PokeAPI website to collect Pokémon data and stores it in an AWS DynamoDB database. The script provides functionality to randomly select Pokémon, retrieve their details from the PokeAPI, and store them in the DynamoDB database if not already present. It also allows users to retrieve Pokémon details from the database.

Prerequisites
Before using PockemonDB, ensure you have the following prerequisites installed:

Python 3.x
AWS account with DynamoDB access
Required Python libraries (boto3, dotenv, requests)
Setup
Clone the repository:

bash

git clone https://github.com/yourusername/PockemonDB.git
Navigate into the project directory:

bash

cd PockemonDB
Install the required dependencies:

pip install -r requirements.txt
Set up your AWS credentials and region in a .env file:

makefile
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_REGION=your_aws_regio
Usage
To use PockemonDB, follow these steps:

Run the script:

css
python main.py
When prompted, enter whether you would like to draw a Pokémon (yes/no).

If you choose to draw a Pokémon, a random Pokémon will be selected, and its details will be retrieved from the PokeAPI. If the Pokémon is not already in the DynamoDB database, its details will be stored in the database.

If the Pokémon is already in the database, its details will be retrieved from the database and presented to the user.

If you choose not to draw a Pokémon, a farewell message will be displayed, and the program will exit.

Functionality
Insert Pokémon: Adds a Pokémon to the DynamoDB database if it doesn't already exist.
Retrieve Pokémon: Retrieves information about a Pokémon from the DynamoDB database.
Random Pokémon Selection: Randomly selects a Pokémon from the PokeAPI.
Exit: Exits the program.
Contributing
Contributions to PockemonDB are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Data sourced from PokeAPI
Support
For any questions or issues regarding PockemonDB, feel free to open an issue on GitHub or contact [ingulator@gmail.com].
