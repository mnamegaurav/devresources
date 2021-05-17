# DevResources

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/hamhaingaurav/devresources)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/hamhaingaurav/devresources/django)

### One destination for all the developer's learning resources.<br> Find all of your learning resources under one roof and add your own.

### Live :sparkles:

You can find the project live [here](https://devresources.guru/) :point_left:

### Screenshot :camera:

![cap](https://user-images.githubusercontent.com/31548778/110208967-fc2b3a00-7eaf-11eb-8c53-61447999f4e5.PNG)

### Features :information_source:

:heavy_check_mark: Responsive UI <br>

:heavy_check_mark: Authentication System <br>

:heavy_check_mark: Add / Update / Delete / View new resources of your own under specific categories <br>

:heavy_check_mark: Searching/Browsing the existing resources <br>

:heavy_check_mark: Top 3 watched resources
<br><br>

### Add your own learning resource :fire:

:one: Login to your account (if not create one) <br>

:two: Once logged in , click on the add icon which navigates to the add resources page <br>

:three: Enter **Title** , **Resource URL** , **Categories (more than one if applicable)** and hit **save** <br>

:four: Check whether your resource added is present in the **Resources Added by You** icon present at the top of the page or you may find it using the searchbox functionality
<br><br>

### Set this project locally :computer:

1. Go to the [project repo](https://github.com/hamhaingaurav/devresources) and fork it by clicking "Fork" ( or Download the Zip file directly and start from the step 3 )<br>

2. Open terminal / command prompt and Clone the project using `git clone https://github.com/YOUR_USERNAME/devresources.git`

3. Add Upstream or the remote of the original project to your local repository

```bash
# check remotes
git remote -v
git remote add upstream https://github.com/hamhaingaurav/devresources

```

4. Make sure you update the local repository

```bash
# Get updates
git fetch upstream
# switch to master branch
git checkout main
# Merge updates to local repository
git merge upstream/main
# Push to github repository
git push origin main

```

5.  Create a python3 virtual environment:

    ```bash
    $ python3 -m venv venv
    ```

    Or, use [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html):

    ```bash
    $ virtualenv venv
    ```

6.  Activate the virtual environment:

    On Linux or Mac or any Unix based system-

    ```bash
    $ source venv/bin/activate
    ```

    On Windows-

    ```
    > venv\Scripts\activate
    ```

7.  Now Install the dependecies:

    ```bash
    $ pip install -r requirements.txt
    ```

8.  Creating local settings:
    Create a `local_settings.py` file in the same directory where your `settings.py` resides.

        Copy this code in your `local_settings.py` file -
        ```
        DEBUG = True
        ```

9.  Creating `.env` file:
    Create a `.env` file in the same directory where your `manage.py` resides.

        Copy this text in your `.env` file -
        ```
        SECRET_KEY = 'secretkey'
        ```

10. Run the `migrate` command:

    ```bash
    $ python manage.py migrate
    ```

11. Now you are ready to go:

    #### Run the application

    ```bash
    $ python manage.py runserver
    ```

12. Optionally you can also add some dump data into your local database using this command:

    #### Add redacted dump data

    **_Note_**: Please run these commands in the same order it has been written here, either it will cause integrity error in your database.

    ```bash
    $ python manage.py loaddata fixtures/ResourceCategory.json

    $ python manage.py loaddata fixtures/Resource.json
    ```

# Thanks
