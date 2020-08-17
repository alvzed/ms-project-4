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


## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

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
