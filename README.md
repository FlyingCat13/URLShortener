# URL Shortener

URL Shortener is a simple project that allows users to create short URLs that redirect to longer specified URLs.

## Requirement

The project requires Python 3, and Python 3 should be run when using `python` in  the command line.

## Installation

To install the necessary packages, as well as migrate the database, run 

```bash
start.sh
```
from a Bash command line.

A superuser with the `username`/`password` of `admin`/`admin` should be created.

## Run
Run the server using the Bash script

```bash
run_server.sh
```

Then, go to `localhost:8000` to access the website.

## Usage

First, log in using the first user credentials. You can create new Users via the admin portal at `localhost:8000/admin`

After you're logged in, you will be greeted with a page containing
- a navigation bar which highlights which page you are on.
- a "Log out" button in the up-right-corner, alongside which user you are logged in as.
- the main portion, which contains the original URL you want to create a short URL for and the button to create it.

Enter your URL into the field. Note that the field requires the scheme to be included as well.

Click the `Shorten URL` button. The page will return a short URL that will redirect to the original URL you entered.

You can also manage the URLs you created by clicking on `View created short URLs` on the navigation bar.

Here, you will see a list of URLs you created, alongside how many times it was accessed.

You can also delete a short URL redirect by clicking `Delete` on the row of the URL you wish to delete.

To log out, simply click `Log out`, and then you can log in as another user after navigating back to the login page.