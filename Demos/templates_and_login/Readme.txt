- The server can be run via the command "flask --app server run". This will serve the webpage on localhost:5000. You can navigate to this address in your browser to see the displayed webpage with some sample data. 

- If you navigate to localhost:5000/login page you will be greeted with a login prompt. By default our server has one account that can login, the username is "foo@bar.tld" and the password is "secret". 

- Logging in under this account will take you to the page localhost:5000/protected where you can add/delete data from the list of players. 

- When a browser requests the main page, localhost:5000/, our server builds that page from a template called welcome.html in ./templates. The server fills in data into the template using the players array in server.py then serves the final html file to the users browser.

- For the login and admin control page we just serve simple static pages. In fact the login page is specified as a single string within server.py.

- The admin account can be logged out from by navigating to the localhost:5000/logout page. Once the user is logged out, or if the user has never logged in to begin with the localhost:5000/protected page is not accessible.

- The main page localhost:5000/ is always accessible whether or not the user is logged in.
