# Simple chat app

## How to install

### Server

1. Change directory: `cd server`
2. Create new database
3. Import dump from `dump.sql`
4. Create `config.py` using provided example in `config.py.example`
5. Install all requirements: `pip3 install -r requirements.txt`
6. Run app server: `flask run`

### Client

1. Change directory: `cd client`
2. Create configuration file `.env` using provided example in `.env.example`
3. Install libraries: `yarn install`
4. Compile and hot-reload for development: `yarn run serve`
5. ..or build minified version for production: `yarn run build`
