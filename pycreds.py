#! /usr/bin/python3
# Made by SpawnZii for BZHunt 07/05/2024
import requests
import json
import click
from termcolor import colored


@click.command()
@click.option('--type','-t',default="email",help='Query type (default email): id, email, ip_address, username, password, hashed_password, hash_type, name, vin, address, phone, database_name')
@click.option('--query','-q',help='Query input, exemple : test@gmail.com')
@click.option('--page','-p',default="1",help='Page to display (default 1). /!\ This options cost 1 api key credit by page display')
@click.option('--size','-s',default="100",help='Number of results by page (default 100).')
@click.option('--filter','-f',default=False,help='Output filter, only display email,username,password')
@click.option('--username','-u',help='Email of your Dehashed account.')
@click.option('--apikey','-a',help='Api key of your Dehashed account.')
@click.option('--output','-o',default="creds.json",help='Save result in json format.')


def main(type,query,page,size,username,apikey,output,filter):
	get_leak(type,query,page,size,username,apikey,output,filter)
 
results = 0

def parse_response(response,page,filter):
    balance = response.get('balance')
    entries = response.get('entries')
    global results
    if entries is not None and filter != True:
        print(f'\nPage {str(page)}')
        print(f'Balance: {balance}')
        print('Entries:' + str(len(entries)))

        for entry in entries:
            print(f'Email: {entry.get("email")}')
            print(f'IP Address: {entry.get("ip_address")}')
            print(f'Username: {entry.get("username")}')
            password = entry.get("password")
            if password:
                print(f'Password: {colored(password, "red")}')
            else:
                print(f'Password: {password}')
            print(f'Hashed Password: {entry.get("hashed_password")}')
            print(f'Name: {entry.get("name")}')
            print(f'Phone: {entry.get("phone")}')
            print(f'Database Name: {entry.get("database_name")}')
            print('-' * 50)

    elif entries is not None and filter == True:
        for entry in entries:
            print(f'Email: {entry.get("email")}')
            print(f'Username: {entry.get("username")}')
            print(f'Hashed Password: {entry.get("hashed_password")}')
            password = entry.get("password")
            if password:
                print(f'Password: {colored(password, "red")}')
            else:
                print(f'Password: {password}')
            print('-' * 50)

    else:
        print('Failed to parse response')

def get_leak(type,query,num_pages,size,email,api_key,output,filter):
    for page in range(1, int(num_pages)+1):
        url = f'https://api.dehashed.com/search?query={type}:{query}&size={size}&page={page}'
        headers = {'Accept': 'application/json'}
        auth = (email, api_key)

        response = requests.get(url, headers=headers, auth=auth)

        if response.status_code == 200:
            parse_response(response.json(),num_pages,filter)
            page_results = response.json().get('entries')
            if page_results is not None:
                with open(output, 'a') as f:
                    json.dump(page_results, f)
                    f.write('\n')
        else:
            print(f'Request failed with status code {response.status_code}, Check your sub.')



if __name__=="__main__":
    main()