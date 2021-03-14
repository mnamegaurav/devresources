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

:four: Check whether your resource added is present in the **Resources Added by You** icon present at the top of the page or you may find it using the searchbox  functionality
<br><br>

### Set this project locally :computer:

1. Go to the [project repo](https://github.com/hamhaingaurav/devresources) and fork it by clicking "Fork" ( or Download the Zip file directly and start from the step 3 )<br>

2. Open terminal / command prompt and Clone the project using `git clone https://github.com/YOUR_USERNAME/devresources.git`
  
3. Create a python3 virtual environment:

    ```
    $ python3 -m venv venv
    ```

    Or, use [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html):

    ```
    $ virtualenv venv
    ```

4. Activate the virtual environment:

    On Linux or Mac or any Unix based system-
    
    ```
    $ source venv/bin/activate
    ```
    
    On Windows-
    ```
    > venv\Scripts\activate
    ```

5. Now Install the dependecies:

    ```
    $ pip install -r requirements.txt
    ```

6. Creating local settings:
Create a `local_settings.py` file in the same directory where your `settings.py` resides.

    Copy this code in your `local_settings.py` file -
    ```
    DEBUG = True
    ```
    
7. Creating `.env` file:
Create a `.env` file in the same directory where your `manage.py` resides.

    Copy this text in your `.env` file -
    ```
    SECRET_KEY = 'secretkey'
    ```

8. Run the `migrate` command:
    ```
    $ python manage.py migrate
    ```

9. Now you are ready to go:

    #### Run the application

    ```
    $ python manage.py runserver
    ```
 
## Developer ✨

<table>
  <tr>
    <td align="center"><a href="https://github.com/hamhaingaurav"><img src="https://avatars.githubusercontent.com/u/34805677?s=400&u=a0f45325750d037434da90119a237286785bf16a&v=4" width="200px;" alt=""/><br /><sub><b>Gaurav Sharma</b></sub></a><br />
    <!-- <a href="https://github.com/hamhaingaurav" title="Code">💻</a> -->
    </td>
  </tr>
</table>
 
### Contributors :zap:
Thanks goes to these wonderful people 
<table>
  <tr>
    <td align="center"><a href="https://github.com/yash2189"><img src="https://avatars.githubusercontent.com/u/31548778?s=460&v=4" width="200px;" alt=""/><br /><sub><b>Yash Ajgaonkar</b></sub></a><br />
    <!-- <a href="https://github.com/yash2189" title="Code">💻</a> -->
    </td>
  </tr>
</table>
<table>
  <tr>
    <td align="center"><a href="https://github.com/chrisjsimpson"><img src="https://avatars.githubusercontent.com/u/1718624?s=460&u=c1240dc4f544632926454196eaabefd47957cc93&v=4" width="200px;" alt=""/><br /><sub><b>Chris J Simpson</b></sub></a><br />
    <!-- <a href="https://github.com/chrisjsimpson" title="Code">💻</a> -->
    </td>
  </tr>
</table>

