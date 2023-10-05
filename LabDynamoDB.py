import boto3
from dotenv import load_dotenv
import requests
import pprint as pp
import random


def main():
    dynamodb = boto3.resource(
        'dynamodb',
        region_name="us-west-2"
    )

    table = dynamodb.create_table(
        TableName='Pokemons',
        KeySchema=[
            {
                'AttributeName': 'name',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'id',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }

    )
    # Wait until the table exists.
    table.wait_until_exists()
    print(table)
    print(list(dynamodb.tables.all()))
    return table


def get_pokemons(api_url):
    response = requests.get(api_url)
    res = response.json()
    return res


def insert_pokemon(table, pokemon):
    table.put_item(
        Item={
            'name': pokemon['name'],
            'id': pokemon['id'],
            'abilities': pokemon['abilities'],
            'height': pokemon['height'],
        }
    )


def pokemon_exist(table, pokemon):
    response = table.get_item(
        Key={
            'name': pokemon['name'],
            'id': pokemon['id'],
        }
    )
    if 'Item' in response:
        return True
    else:
        return False

def retrive_pokemon(table, pokemon):
    response = table.get_item(
        Key={
            'name': pokemon['name'],
            'id': pokemon['id'],
        }
    )

    item=response["Item"]
    name=item["name"]
    id=item["id"]
    abilities=item["abilities"]
    height=item["height"]
    pp.pprint(f"name: {name} , id: {id} , abilities: {abilities} , height: {height} ")

if __name__ == '__main__':
    load_dotenv()
    pokemon_table = main()
    api_url = "https://pokeapi.co/api/v2/pokemon"
    result = get_pokemons(api_url)
    pokemon_list = result["results"]
    draw ="yes"
    while draw == "yes":
        draw=input("Would you like to draw a Pokemon? yes/no: ")
        if draw == "yes" :
            pokemon = random.choice(pokemon_list)
            pokemon_name = pokemon["name"]
            pokemon_url = pokemon["url"]
            api_url = pokemon_url
            pokemon = get_pokemons(api_url)
            pokemon_id = pokemon["id"]

            if pokemon_exist(pokemon_table, pokemon) == False:
                insert_pokemon(pokemon_table, pokemon)

                retrive_pokemon(pokemon_table, pokemon)
        if draw != 'yes':
             print("Goodbye, have a nice day!")



#pokemons_table.delete()