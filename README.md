# pyflix-movie-rental-database

# <h2> Introduction

This Python code takes the user to a portal for the rent and purchase of movies. The
program navigates through the various stages of the purchase, including login, selection
of movies, discount(if applicable), and payment. We have incorporated various modules
and functions into the program in order to make the program as user-friendly as possible.
The program has a pre-created database of movies, which can be accessed using the text
file in which it is stored.

The Python module “Turtle” is also used in the program, to draw the logo of our project.
The program starts with the choice for the user to either login or create a new account. By
creating a new account, the user’s details such as username, password, and number, are
stored in a user database (csv file). After logging in, the user is asked to use filters to find movies
that are favourable for them. A list of movies is then displayed, and the user is asked to
enter the movie of his choice and is given the option to rent or buy the movie. Renting a
movie will allow a user to temporarily own the movie for 7 days; buying the movie
allows permanent ownership. If more than 5 movies are purchased, the user is offered a
discount, which is applied to the total purchase cost. The final amount to be paid is added
to the user’s bill in the user database. The user is then given an option to provide
suggestions for movies to be added to our database.

We used sql connectivity for the purpose of collecting reviews from customers. We are giving the
user an option to rate their experience while using the program and they are given an opportunity
to enter feedback, which will be updated in the SQL database. This is used to enhance user
experience.
  
# <h2> User-Defined Functions
1. discount():
The purpose of this feature is to offer a discount of 25 percent to customers that purchase
or rent more than five movies at a time
2. userinput():
 Users are provided with this function so they can give their own movie recommendations.
 You can specify the genre, name, rating, and actors of the movie you'd like to
 recommend.
  
# <h2> Sample Output 
# <h4> Output 1: New User
  Logo (using Python Turtle) <br>
<img src= "https://user-images.githubusercontent.com/86789453/211568242-5313affc-e3d3-4730-a5c3-12653650ac1f.JPG" width="400" /> <br> <br>
<img src = "https://user-images.githubusercontent.com/86789453/211570046-f03db106-e4b5-494b-a984-4cfdd02c0f1e.JPG" width="700" /> <br> 
<img src = "https://user-images.githubusercontent.com/86789453/211570066-d9a0d794-b080-41f2-892c-7d53213fc439.JPG" width="700" /> <br> 
  
 The updated user database with new users <br>
 <img src = "https://user-images.githubusercontent.com/86789453/211573302-29c09e1c-6484-40ca-a782-c53e6f34dae0.JPG" width="400" /> <br> 
  
 The updated movies list with user’s recommended movies <br>
 <img src = "https://user-images.githubusercontent.com/86789453/211573298-2f3c5194-3ab7-41af-aa35-d817a9f56923.JPG" width="400" /> <br> 
  
  # <h4> Output 2: Exisitng User and Discount Application
  <img src = "https://user-images.githubusercontent.com/86789453/211573297-d09a2207-3d15-408b-99b5-894bbb80c60e.JPG" width="700" /> <br> 
  <img src = "https://user-images.githubusercontent.com/86789453/211573294-835fcac1-f797-423c-85a6-532d3ef2a2f9.JPG" width="700" /> <br>
  The updated SQL Databse<br>
  <img src = "https://user-images.githubusercontent.com/86789453/211573292-ee30f99b-297c-49a4-a81a-3244f629b2d5.JPG" width="700" /> 
  
  # <h2> Synopsis
Though the program serves a straightforward purpose, we believe that there is scope for
improvement. The database of the movies currently is limited, enabling the user to rent or
purchase only from a small collection. Enabling the user to add more movies will help
with this problem, but there is a risk of unwanted and corrupted files entering the
database.
We have also noticed that the movie database would work faster and be more efficient if
it existed in MYSQL instead of a CSV file as it is currently in. Upon learning to connect
Python with MYSQL, we would be able to implement this idea in our project.
