# Pycreds
Dehashed cli 
## Install
- `git clone https://github.com/SpawnZii-bzhunt/pycreds.git ; cd pycreds ; pip3 install -r requirements.txt`

## Usage
```bash
$ python3 pycreds.py --help
Usage: pycreds.py [OPTIONS]

Options:
  -t, --type TEXT       Query type (default email): id, email, ip_address,
                        username, password, hashed_password, hash_type, name,
                        vin, address, phone, database_name
  -q, --query TEXT      Query input, exemple : test@gmail.com
  -p, --page TEXT       Page to display (default 1). /!\ This options cost 1
                        api key credit by page display
  -s, --size TEXT       Number of results by page (default 100).
  -f, --filter BOOLEAN  Output filter, only display email,username,password
  -u, --username TEXT   Email of your Dehashed account.
  -a, --apikey TEXT     Api key of your Dehashed account.
  -o, --output TEXT     Save result in json format.
  --help   
```
```bash
$ python3 pycreds.py -t email -q test@gmail.com -s 1 -p 1 -u "*****@gmail.com" -a "****************************" -o creds.json -f true
Email: test@gmail.com
Username: 
Hashed Password: 
Password: rui
--------------------------------------------------
```
