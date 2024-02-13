Deployment Steps :
* Heroku CLI: Make sure you have the Heroku CLI installed on your local machine. If not, download and install it from the Heroku website.
* Login to Heroku: Open a terminal and run heroku login to log in to your Heroku account.
* Initialize a Git Repository (if not already done):
    * Navigate to your project directory.
    * Initialize a Git repository with git init.
    * Add all files to the repository with git add .
    * Commit the files with git commit -m "Initial commit".
* Create a Heroku App:
    * In the terminal, run heroku create keizntree
* 		Add a Procfile: Ensure you have a Procfile in your project root (I noticed there is one in your directory). It should contain: makefile  Copy code web: gunicorn keizntree-project.wsgi   
* Set up Database: If your project uses a database, set up a Heroku Postgres database (or other databases supported by Heroku).
* Configure settings.py:
    * Update the DATABASES setting to use dj_database_url for the database URL.
    * Add django_heroku.settings(locals()) at the end of the settings.py file.
* Add requirements.txt:
    * Ensure all required packages are listed in requirements.txt.
    * Include gunicorn and django-heroku.
* Deploy to Heroku:
    * Add the Heroku remote with heroku git:remote -a keizntree.
    * Deploy your app with git push heroku master.
* Run Migrations:
    * Run heroku run python manage.py migrate to apply database migrations.
* Create a Superuser (optional):
    * Create a superuser with heroku run python manage.py createsuperuser if needed.
Running the App
* The app should now be running on Heroku. You can open it in a web browser with heroku open or by visiting https://keizntree-e0a76fd0954f.herokuapp.com
