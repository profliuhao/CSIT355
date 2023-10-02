# READ ME

## Step 0: Download the Repository as a .zip File

Open your web browser and go to the GitHub repository URL: https://github.com/profliuhao/CSIT355/tree/main/flaskMysqlProjectTemplate.

Click on the green "Code" button near the top right of the page.

In the dropdown menu, select "Download ZIP."

Save the downloaded .zip file to a directory on your computer.

## Step 1: Extract the .zip File

Navigate to the directory where you saved the .zip file.

Right-click on the .zip file and select "Extract" or "Extract All." Choose a location to extract the files.

## Step 2: Change Directory to the Project

Open your terminal or command prompt.

Navigate into the extracted project directory:

```shell
cd path/to/CSIT355-main/flaskMysqlProjectTemplate
```
(Note: Replace path/to/ with the actual path to the extracted directory.)

## Step 3: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment to isolate dependencies for your project. Run:
```shell
python -m venv venv
```

> Activate the virtual environment:
On Windows:
```shell
venv\Scripts\activate
```

> On macOS and Linux:
```shell
source venv/bin/activate
```

## Step 4: Install Dependencies

Use pip to install the required packages:
```shell
pip install -r requirements.txt
```

## Step 5: Configure the Database

Open the MySQLConfig.py file and provide your MySQL database configuration details (username, password, host, database name).

## Step 6: Start the Flask Application

Start the Flask development server:
```shell
python app.py
```
or open app.py and click on the run button in Pycharm

Step 8: Access the Web Application

Open a web browser and navigate to http://localhost:5000.
If website not available, also try http://localhost:9999 (as the port number set in app.py).

Step 9: Interact with the Application

You can now interact with the Flask application. Explore its features and functionalities.



## For MacOS users
If installing mysql client failed with pk.config errors, 
please try the following 2 steps:
### First, Install Brew
Reference [Home Brew](https://brew.sh/).
Open your terminal and type in the following commands.
``` shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Then, Install mysql-client
```shell
brew install mysql-client pkg-config
export PKG_CONFIG_PATH="/opt/homebrew/opt/mysql-client/lib/pkgconfig"
pip install mysqlclient
```

