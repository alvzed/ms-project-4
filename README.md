# Rivulet

This project is a small streaming service, with the goal of being a smooth and simple experience of streaming videos.
 
## UX
 
#### User stories
 - As Adil, I want to watch some movies to relax in the evening
 - As Hibo, I want to check out a streaming service recommended to me, and see the price and content easily.
 - As Catrin, I want to update my email address in my profile so I can easily recover my account now that my old one is lost
 - As Oliver, I want to cancel my subscription since I no longer have time to use the service that much
 - As Jasin, I want to update my payment info so my subscription can be renewed automatically
 - As Eivind, I want the site to recommend new videos to me based on my history

#### Wireframes

![Landing page](/wireframes/landing_page.png)
![Landing page mobile](/wireframes/landing_page_mobile.png)
![registration page](/wireframes/register.png)
![registration page mobile](/wireframes/register_mobile.png)
![video page](/wireframes/video_page.png)
![video page mobile](/wireframes/video_page_mobile.png)
![video player](/wireframes/video_player.png)
![video player mobile](/wireframes/video_player_mobile.png)
![search page](/wireframes/search_page.png)
![search page mobile](/wireframes/search_page_mobile.png)

The wireframes for this project are quite simple as it took a lot of inspiration from other streaming sites (mainly netflix), and this was a method to try to avoid looking _exactly_ like those sites. The responsiveness is planned out to be a stacking of thumbnails on top of each other when the smaller the screen gets. 

## Features
 
### Existing Features
- User authorization - allows users to create an account that stores user information and lets logged in user's see the content on the site. This includes sign up, login and logout pages.
- Admin page - allows a superuser to log in to the admin panel and use CRUD functionality on all users, videos, categories, etc. This is currently the built in Django admin page as it fulfilled all the functionality needed for the admin user at the moment. This will be built out to a more fitting admin page and functionality on the site istelf in the future. 
- Landing page - this view redirects logged in users to the library directly but stops unauthorized users and shows them buttons that are linked to the sign up and login pages. All views redirect to this page is the user isn't authorized.
- Library - the main page of the site, it shows the user thumbnails of the following videos: 
    - The most 5 viewed videos and 
    - The most 5 viewed videos of the 3 most clicked categories. 
- Videos - at the moment this stores a video object which inludes a title, a description, a foreign key to a category, a PG integer, and a youtube ID. This project uses a youtube iframe api to display videos as the database is currently too small to store entire videos on it. 
- Categories - an object that stores a slug and a name, the slug is for filtering and the name is for displaying on the page. 
- Filtering - uses the slug from the category object and a dropdown bar to filter the videos and only show the ones with a matching category. It also uses the name to display a title to show what category you are currently on. 
- Search - a form on the navbar which submits a query variable, the variable is then used to filter through the videos and display any video what a title or description that has matching keywords. It displays how many results you have on the top of the page if the search bar is empty is simply returns you to the main library page. 
- Player - A view that displays a specific video and starts playing it directly. 
- User page - a view that currently displays a greeting including the user's username and three buttons: change password, donate and back to library. 
- Donations - allows users to submit small single payments via stripe to support the site. This is currently quite crude and only processes either succeeded payments or failed payments and redirecting them to a specific page based on this. 

### Features Left to Implement
- Actors - a model which would relate the actors to various videos that would allow users to filter and search by actors names.
- Subcategories - a model which would have a many to one relationship with categories and allow users to dive deeper into filtering videos.
- Storing more categories - allowing videos to have several categories for videos that match several categories definitions. 
- Extended userpage - storing a user history which would be used to recommend videos and display a "latest watched" on the userpage.
- Subscription system - developing the donation system to have recurring payments and handling more webhooks. This would also be used for the user authorization and extended userpage to store information regarding payments, missed payments, etc. 
- Video ratings - would allow users to submit a rating that would be used for a list of good and bad ratings to create an average score of a video. 
- Recommedations - will use a users click and view history to create recommendations for the user.

### Features in contrast to the user stories
Go through user stories one by one and see if they were fulfilled

## Technologies Used
- [Python](https://www.python.org/)
    - Used as the back end language
- [Django](https://www.djangoproject.com/)
    - Used to make the back end views, urls, templates, and more. It was chosen because it makes the process easier and faster.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/overview.html)
    - Used to make the authorization processes and views faster to implement.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation together with Bootstrap.
- [Bootstrap 4.5.1](https://getbootstrap.com/)
    - **Bootstrap** was mainly used for simplify design process, especially the responsiveness.


## Testing
1. User authorization
    - This testing process is here to make sure that users can only access the content of the site if they are logged in.
    - Make sure you are logged out.
    - Go to the site's landing page '/', see if you are redirected or stay on the landing page.
    - Add 'library/' to the end of the url, see if you can access the library or if you are redirected to the landing page.
    - Change 'library/' to 'profile/', see if you can access the userpage or if you are redirected to the landing page.
    - Repeat the process for every url on the site. The only ones you should be able to access are the ones related to user authorization (login, etc), and the admin page as superusers need to be able to log in there.
    - Note any bugs that have appeared and resolve any issues. 
2. User sign up, login, and logout
    1. Sign up
        - Go to the landing page of the site.
        - Click the sign up button and enter any information needed. 
        - At this point you should be logged in automatically, note if there are any issues with this. 
    2. Login
        - Make sure you are logged out.
        - Go to the landing page and click the login button.
        - Enter your credentials.
            - Try once with the password field empty.
            - Try once with the wrong password.
            - Try once with the correct information.
            - Note any issues.
        - See if you are redirected to the library.
    3. Logout
        - Make sure you are logged out.
        - Go to the site, you should be redirected to the library. 
        - Click the user dropdown on the navbar, click the log out option. You should be redirected to a page asking you if you are sure you want to log out.
        - Click log out.
        - Try to access the library, note if you can.
        - Log in again. 
        - Go to the userpage. 
        - Click the log out button. You should be redirected to a page asking you if you are sure you want to log out.
        - Click the log out button. 
        - Note any issues with redirects and links on the page.
3. Search
    - Go to the library page.
    - Enter a key word in the search bar, make sure it is gibberish and doesn't match any video (example 'dfhgdfh').
    - See if any videos appear, check if you have a message on the top of the screen telling you there are no matches.
    - Enter a new key word in the search bar, make sure it matches a title on the library front page. See how many videos appear and see if they match the number of results the message on the top of the page are telling you there are.
    - Enter a new key word that matches something in the description of a video, see how many results you get and if the amount matches the results message again. 
4. Category filter
5. Admin page
6. Donations
    1. Payment succeeded
    2. Payment failed
7. User page
8. Password reset

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
