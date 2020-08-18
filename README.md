# Rivulet

This project is a small streaming service, intending to be a smooth and simple experience of streaming videos.

## UX

#### User stories
- As Adil, I want to watch some movies to relax in the evening
- As Hibo, I want to check out a streaming service recommended to me, and see the price and content easily.
- As Catrin, I want to update my email address in my profile, so I can easily recover my account now that my old one is lost
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

The wireframes for this project are quite simple as it took a lot of inspiration from other streaming sites (mainly Netflix), and this was a method to try to avoid looking _exactly_ like those sites. The responsiveness is planned out to be a stacking of thumbnails on the top of each other when the smaller the screen gets.

## Features

### Existing Features
- User authorization - allows users to create an account that stores user information and lets logged-in users see the content on the site. This includes sign up, login, and logout pages.
- Admin page - allows a superuser to log in to the admin panel and use CRUD functionality on all users, videos, categories, etc. This is currently the built-in Django admin page as it fulfilled all the functionality needed for the admin user at the moment. This will be built out to a more fitting admin page and functionality on the site itself in the future.
- Landing page - this view redirects logged in users to the library directly but stops unauthorized users and shows them buttons that are linked to the sign-up and login pages. All views redirect to this page is the user isn't authorized.
- Library - the main page of the site, it shows the user thumbnails of the following videos:
- The most 5 viewed videos and
- The most 5 viewed videos of the 3 most clicked categories.
- Videos - at the moment this stores a video object which includes a title, a description, a foreign key to a category, a PG integer, and a youtube ID. This project uses a youtube iframe API to display videos as the database is currently too small to store entire videos on it.
- Categories - an object that stores a slug and a name, the slug is for filtering and the name is for displaying on the page.
- Filtering - uses the slug from the category object and a dropdown bar to filter the videos and only show the ones with a matching category. It also uses the name to display a title to show what category you are currently on.
- Search - a form on the navbar which submits a query variable, the variable is then used to filter through the videos and display any video what a title or description that has matching keywords. It displays how many results you have on the top of the page if the search bar is empty is simply returns you to the main library page.
- Player - A view that displays a specific video and starts playing it directly.
- User page - a view that currently displays a greeting including the user's username and three buttons: change password, donate, and back to library.
- Donations - allows users to submit small single payments via stripe to support the site. This is currently quite crude and only processes either succeeded payments or failed payments and redirecting them to a specific page based on this.
- Most viewed videos - increments an integer in the video object whenever someone accesses the video in the player. This is then used to display the 5 most viewed videos on the main library page.
- Most clicked categories - increments an integer in the category object whenever someone filters by that category. This is then used to display the 3 most clicked categories on the main library page.
- This also uses the most viewed videos feature, as it displays the 5 most viewed videos in each top category.

### Features Left to Implement
- Emails - sends verification emails and password reset links to users. This is currently printed out in the console instead of emailed out, the reason for this is that an email would need to be connected to this and I do not want to make my email publicly accessible.
- Actors - a model that would relate the actors to various videos that would allow users to filter and search by actors' names.
- Subcategories - a model which would have a many to one relationship with categories and allow users to dive deeper into filtering videos.
- Storing more categories - allowing videos to have several categories for videos that are genre-crossing.
- Extended user page - storing a user history which would be used to recommend videos and display a "latest watched" on the user page. This would make it possible to store a user's age and filter videos based on the PG integer in the video objects.
- Subscription system - developing the donation system to have recurring payments and handling more webhooks. This would also be used for the user authorization and extended user page to store information regarding payments, missed payments, etc.
- Video ratings - would allow users to submit a rating that would be used for a list of good and bad ratings to create an average score of a video.
- Recommendations - will use a user's click and view history to create recommendations for the user.

### Features in contrast to the user stories
- As Adil, I want to watch some movies to relax in the evening
For this user-story, Adil can easily log in to the site (or sign up) and start streaming a video right away.

- As Hibo, I want to check out a streaming service recommended to me, and see the price and content easily.
Hibo can quite easily create an account and start watching quickly and without too much of a hassle.

- As Eivind, I want the site to recommend new videos to me based on my history
While this isn't implemented yet, the most clicked categories and most viewed videos features give some recommendations based on what all the users on the site click and view.

- As Catrin, I want to update my email address in my profile, so I can easily recover my account now that my old one is lost
This has not been implemented as it made more sense to have a password recovery functionality instead in the minimal viable product.

- As Oliver, I want to cancel my subscription since I no longer have time to use the service that much
- As Jasin, I want to update my payment info so my subscription can be renewed automatically
The two of these have not been implemented as the site currently uses a donations feature. These would be the focus of future versions of the project as the next step would be implementing the subscription feature.

## Technologies Used
- [Python](https://www.python.org/)
- Used as the back end language
- [Django](https://www.djangoproject.com/)
- Used to make the back end views, URLs, templates, and more. It was chosen because it makes the process easier and faster.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/overview.html)
- Used to make the authorization processes and views faster to implement.
- [JQuery](https://jquery.com)
- The project uses **JQuery** to simplify DOM manipulation together with Bootstrap.
- [Bootstrap 4.5.1](https://getbootstrap.com/)
- **Bootstrap** was mainly used to simplify the design process, especially the responsiveness.

## Testing
1. User authorization
- This testing process is here to make sure that users can only access the content of the site if they are logged in.
- Make sure you are logged out.
- Go to the site's landing page '/', see if you are redirected or stay on the landing page.
- Add 'library/' to the end of the URL, see if you can access the library or if you are redirected to the landing page.
- Change 'library/' to 'profile/', see if you can access the user page or if you are redirected to the landing page.
- Repeat the process for every URL on the site. The only ones you should be able to access are the ones related to user authorization (login, etc), and the admin page as superusers need to be able to log in there.
- Note any bugs that have appeared and resolve any issues.
2. User sign up, login, and logout
1. Sign up
- Go to the landing page of the site.
- Click the sign-up button and enter any information needed.
- At this point, you should be logged in automatically, note if there are any issues with this.
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
- Click the user dropdown on the navbar, click the logout option. You should be redirected to a page asking you if you are sure you want to log out.
- Click log out.
- Try to access the library, note if you can.
- Log in again.
- Go to the user page.
- Click the log out button. You should be redirected to a page asking you if you are sure you want to log out.
- Click the log out button.
- Note any issues with redirects and links on the page.
3. Search
- Go to the library page.
- Enter a keyword in the search bar, make sure it is gibberish and doesn't match any video (example 'dfhgdfh').
- See if any videos appear, check if you have a message at the top of the screen telling you there are no matches.
- Enter a new keyword in the search bar, make sure it matches a title on the library front page. See how many videos appear and see if they match the number of results the message on the top of the page is telling you there are.
- Enter a new keyword that matches something in the description of a video, see how many results you get and if the amount matches the results' message again.
4. Category filter
- Go to the library page.
- Click the category dropdown box on the navbar and select a category.
- Check if the heading on the page displays the selected category.
- Check if all videos in the selected category appear (you may need to double-check the admin page for this).
5. Admin page
- Go to the admin page and log in with a superuser.
- Check if all models appear on the screen.
- Check each of them to see if all related fields appear.
- Create a new object.
- Click in on this new object and see if everything displays correctly.
- Update something in the object.
- Delete the object.
6. Donations
1. Payment succeeded
- Go to the donations page.
- Enter information in all fields, the email should be prepopulated with your account's email. Make sure to fill in the card field with 4242424242424242, and the date to any future date, the last field can be any number.
- Press submit.
- Check that you are redirected properly and that the donation amount is visible on the success page.
2. Payment failed
- Go to the donations page.
- Enter information in all fields, the email should be prepopulated with your account's email. Make sure to fill in the card field with 4000000000000002, and the date to any future date, the last field can be any number.
- Press submit.
- Check that you are redirected properly to the failure page.

7. Incrementing clicks/views
- The click and view counters are currently quite crude and use the same type of functionality. The reason they have different names despite their similarities is for future versions.
1. Incrementing views
- Go to the admin page.
- Check the number of views of a specific video, note it down.
- Go to the library page, click the video you have chosen.
- Go back to the admin page, and to the specific video object.
- Compare the integer to the number you have previously noted down.
2. Incrementing clicks
- Go to the admin page.
- Check the number of views of a specific category, note it down.
- Go to the library page, filter by the category you have chosen.
- Go back to the admin page, and to the specific category object.
- Compare the integer to the number you have previously noted down.

##### Bugs discovered
The main tests didn't yield any bugs as they rely on Django which is quite a mature and stable framework.
What was discovered is when incrementing clicks and views. Whenever you visit the URL of one of the categories or videos it increments the clicks/views, which means that it will happen if someone simply refreshes the page as well. This is something to resolve in future versions.

#### Current UI

This is how the site currently looks on a desktop and iPhone X.

![Landing page](/wireframes/rivulet_landing_current.png)
![Landing page mobile](/wireframes/rivulet_landing_current_mobile.png)
![Library page](/wireframes/rivulet_library_current.png)
![Library page mobile](/wireframes/rivulet_library_current_mobile.png)

## Deployment
Below is a brief summary of how to deploy a site on H, I do not give as good of an explanation as you can find [on their site](https://devcenter.H.com/articles/getting-started-with-python). Please go to this site for a much better explanation.

This project is hosted on H, specifically with the H CLI for python.
First make sure that you've installed H on your device, if not then install it.

Login to H through the terminal by typing H login and pressing enter.
Push the project to H with your preferred method.
Set up all the config vars you need in the settings of your project.

Make sure to have a Procfile and requirements.txt so the webapp sets up properly.

Then launch the site with the command H ps:scale web=1.
A complete guide to the deployment process can be found [here](https://devcenter.H.com/articles/getting-started-with-python).

**The main difference** between the deployed app and the development app is in a few if statements found on settings.py in the rivulet folder. Two if-statements based on an environment variable called USE_AWS decide if the site is in debug mode or not and if they use the static files locally from an AWS bucket. The development version also uses an SQLite database while the deployed version uses Heroku's Postgres database.

## Credits
- A huge thank you to Emma Öberg for giving valuable feedback during the UI process, and for testing the site over and over again.

### Content
- The videos on this site are mainly trailers from this [youtube channel](https://www.youtube.com/c/movieclipsTRAILERS). The synopsis for each video is also taken from there.

### Media
- The photos used in this site were obtained from [unsplash](https://unsplash.com/)

### Acknowledgments

- I received inspiration for this project mainly from Netflix, but also Crunchyroll, HBO Nordic, and Youtube.