# DevResources
## One destination for all the developer's learning resources.

### [Live Link](https://devresources-guru.herokuapp.com/)

## Contributing:

### To run this project locally-

1. Create a python3 virtual environment:

    ```
    $ python3 -m venv venv
    ```

    Or, use [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html):

    ```
    $ virtualenv venv
    ```

2. Activate the virtual environment:

    On Linux or Mac or any Unix based system-
    
    ```
    $ source venv/bin/activate
    ```
    
    On Windows-
    ```
    > venv\Scripts\activate
    ```

3. Now Install the dependecies:

    ```
    $ pip install -r requirements.txt
    ```

4. Creating local settings:
Create a `local_settings.py` file in the same directory where your `settings.py` resides.

    Copy this code in your `local_settings.py` file -
    ```
    DEBUG = True
    ```
    
5. Creating `.env` file:
Create a `.env` file in the same directory where your `manage.py` resides.

    Copy this text in your `.env` file -
    ```
    SECRET_KEY = 'secretkey'
    ```

6. Run the `migrate` command:
    ```
    $ python manage.py migrate
    ```

7. Now you are ready to go:

    #### Run the application

    ```
    $ python manage.py runserver
    ```


## Thanks
