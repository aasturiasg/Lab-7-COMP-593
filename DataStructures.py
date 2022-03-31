""" 
COMP 593 - Lab 7

Description: 
  Prints four grammatically correct sentences with data extracted from a complex data
  structure with fixed values.

Usage:
  python DataStructures.py

Parameters:
  None.

History:
  Date        Author      Description
  2022-03-31  A.Asturias  Initial creation
"""

def main():

    #initialize the data structure with default values
    pizza_and_movies = {
        'name': 'Andre Asturias',
        'student_id': 10265772,
        'pizza_toppings': ['gummy bears', 'watermelon', 'glue'],
        'movies': [
            {'title': '22 Jump Street', 'genre': 'comedy'},
            {'title': 'Iron Man', 'genre': 'action'}
            ]
    }

    #create a new dictionary for a movie, and append it
    new_movie = {'title': 'When We First Met', 'genre': 'romance'}
    pizza_and_movies['movies'].append(new_movie)

    #add more toppings to the pizza toppings list by calling a function
    new_toppings = ('chocolate', 'chicken balls', 'gasoline', 'salmon')
    add_pizza_toppings(pizza_and_movies, new_toppings)

    #call a funtion to print the desired sentences with the information in the data structure
    print_sentences(pizza_and_movies)

#function to add new toppings to the list of pizza toppings
def add_pizza_toppings(data_structure, new_toppings):

    #add every element in the tuple to the pizza toppings list
    for topping in new_toppings:
        data_structure['pizza_toppings'].append(topping)

    #sort all the elements in the pizza toppings list
    data_structure['pizza_toppings'].sort()

#function to print the 4 expected sentences
def print_sentences(data_structure):

    #print the sentence involving name and student ID
    print('Hi Joe, my name is', data_structure['name'] + ', and my student ID is', str(data_structure['student_id']) + '.')

    #build the desired string containing all the pizza toppings
    string_for_toppings = 'My ideal pizza has '
    #iterate through all the elements in the toppings list
    for index, topping in enumerate(data_structure['pizza_toppings']):
        #for the last element in the list
        if (index == len(data_structure['pizza_toppings']) - 1):
            string_for_toppings += 'and ' + topping + '.'
        #for any other element
        else:
            string_for_toppings += topping + ', '
    #print the string created
    print(string_for_toppings)

    #build the desired strings for the movie genres and titles
    string_for_movie_genres = 'I like to watch '
    string_for_movie_titles =  'Some of my favorites are '
    #iterate through the list containing the dictionaries for the movies
    for index, movie in enumerate(data_structure['movies']):
        #for the last element in the list
        if (index == len(data_structure['movies']) - 1):
            string_for_movie_genres += 'and ' + movie['genre'] + ' movies.'
            string_for_movie_titles += 'and ' + movie['title'] + '!'
        #for any other element
        else:
            string_for_movie_genres += movie['genre'] + ', '
            string_for_movie_titles += movie['title'] + ', '
    #print the two strings created
    print(string_for_movie_genres)
    print(string_for_movie_titles)

main()