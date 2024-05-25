# setup

### To start the django app run commands

docker compose build 
docker compose up

or if you have make install 
Run make r

# locate to 

POST http://localhost:8000/remove-bg/

### json-body
{"image_url": "your image url"}

this endpoint will download the image and remove the background from it and return the URL to access that image

first time it will take time becuase of downloading the requireded models