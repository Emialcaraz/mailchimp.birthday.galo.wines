# Mailchimp Birthday sender for Galo Wines restaurant
This project it is created to schedule mails in Mailchimp for birthdays with the free version.
The objective is to send two mails, one ten days before the birthday for example to offer discounts and the other mail it is to say happy birthday.

The project it is customized for an specific usage of Galo Wines restaurant.

## Environments variables:
Create an .env file and .env.dev for development mode in the docker folder, with the following settings:

```bash
ENV_TYPE=development
API_TOKEN= The api token for mailchimp
USERNAME= The username in mailchimp
CAMPAIGN_ID= The ID of the campaign for the celebrate mail
CAMPAIGN_ID_BIRTHDAY= The ID of the campaing of the Birthday Mail
 ```

## Development
Note: to run the service in development mode, you need to enter to the docker container.
The development script mounts the source code in the docker image.
```bash
./scripts/start_develop.sh build
```

To run the image:
```bash
./scripts/start_develop.sh
```

Then you can search the container id and simple run:

```bash
docker exec -it CONTAINERID bash
```

```bash
python main.py
```

Probably you need first to install pre-commit hooks in your computer, simply run

`sudo apt install pre-commit` or look on https://pre-commit.com/ how to install on your OS.


You can install a set of pre-commit-hooks to prevent you screw it up. To do that just run:

```bash
./start.sh
```
