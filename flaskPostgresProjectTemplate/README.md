# Run with Docker Compose
We can use docker to set up our app and Mysql database using Docker compose with internet connection.
## Step 0
Before you can actually run it you need to build them using
```bash
docker-compose build --no-cache
```
## Step 1
If you are running for the first time you don't need --no-cache. Now, let us run it

```bash
docker-compose up -d
```
That should run the containers successfully, here -d is used to "detach" which basically lets you exit the logs after successfully deploying the containers.

At this point, you should be able to access your API successfully on http://localhost:9999. You can test it out. 

## Step 2
Now to stop the containers you can use
```bash
docker-compose down
```
Read the official docs to see what else you can do with docker-compose. 

## Step 3
To develop and implement more functionality of this application (updating app.py), run 
```bash
docker-compose up -d --build app
```
