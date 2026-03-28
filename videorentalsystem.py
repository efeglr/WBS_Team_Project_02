class Video:
    def __init__(self, title, genre, video_id, available):
        self.title = title
        self.genre = genre
        self.video_id = video_id
        self.available = available
        self.ratings = []
        self.average_rating = 0
    def __str__(self):
        return f"{self.title},{self.genre},{self.video_id},{self.available}"

class Customer:
    def __init__(self,name, customer_id, rented_videos):
        self.name = name
        self.customer_id = customer_id
        self.rented_videos = rented_videos
        self.video_ratings = {}

    def give_rating(self,video,rating):
        try:
            if video.title in self.video_ratings.keys():    # check if customer rated a movie already, if so return
                print("Movie has already been reviewed")
                return
            if rating >= 1 and rating <= 5:                 # only allow ratings between 1 and 5
                video.ratings.append(rating)
                self.video_ratings[video.title] = rating
                total_rating = 0
                for rating in video.ratings:
                    total_rating += rating
                video.average_rating = total_rating/len(video.ratings)
                print(f"The movie: {video.title} got a review from you with {rating} star(s)")
        except: 
            print("Please enter a number between 1 and 5")

    

class VideoStore:
    def __init__(self,name):
        self.name = name
        self.videos = {}
        self.customers = {}
        self.customer_rents = {}

    def add_video(self,video):
        self.videos[video.video_id] = video

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer
    
    def rent_video(self, customer_id, video_id):
        if self.videos[video_id].available == True:
            self.customer_rents[customer_id] = video_id #adding the customer and the rented book as a pair into customer_rents
            self.videos[video_id].available = False #setting the availability of the Movie to False
            self.customers[customer_id].rented_videos.append(video_id)
        else:
            print("Move is not available for rent.")
    
    def return_video(self, customer_id, video_id):
        if self.videos[video_id].available == False:
            self.videos[video_id].available = True # Setting the availability of the video to True
            self.customer_rents.pop(customer_id) # Delete that the customer rented something

    def list_available_videos(self):
        for video in self.videos.values():
            if video.available == True:
                print(video.title)

    def list_customer_videos(self,customer_id): #show what a customer has rented.
        print(f"Customer has rented {self.customers[customer_id].rented_videos}")
    
    def search_title(self, title):
        for item in self.videos.values():
            if title in item.title:
                print("Your movie is in the video store!")
                if item.available == True:
                    print("Our Video Store has the movie!")
                else:
                    print("The movie is rented, come back when it's available")
                return
        print("Movie was not found") #if movie title wasn't found

    def search_genre(self, genre):
        for item in self.videos.values():
            if genre in item.genre:
                print("Your genre is in the video store!")
                return
        print("Movie genre was not found") #if movie genre wasnt found
    
def main():
    video_1 = Video("Harry Potter", "Fantasy", 1, True)
    video_2 = Video("Scarface", "Mafia", 2, True)
    customer_1 = Customer("Bubu",1, [])
    customer_2 = Customer("Dudu",2, [])
    video_store_by_efe = VideoStore("By efe")
    video_store_by_efe.add_customer(customer_1)
    video_store_by_efe.add_video(video_1)
    video_store_by_efe.add_video(video_2)
    video_store_by_efe.rent_video(1,1)
    video_store_by_efe.list_available_videos()
    video_store_by_efe.list_customer_videos(1)
    video_store_by_efe.search_title("Scarface")
    video_store_by_efe.search_title("Harry Potter")
    customer_1.give_rating(video_1,5)
    customer_2.give_rating(video_1,4)
    print(video_1.average_rating)
main()

#🎬 Video Rental System
# 🎯 Goal
# Students will build a console-based system for renting movies, returning them, and managing members.

# 🔑 Learning Focus
# Classes: Video, Customer, VideoStore
# Functions: rent, return, search, list
# Collections: use of dict and list for efficient management

# 🎯 Learning Objectives
# By the end of this project, students will be able to:
# Apply Object-Oriented Programming (OOP) principles by creating and using classes (Video, Customer, VideoStore).
# Encapsulate functionality inside methods (e.g., rent, return, search, list).
# Use Python collections (list, dict) to store and retrieve structured data efficiently.
# Implement control flow with conditions and loops to manage system operations.
# Design modular code by splitting responsibilities across classes and functions.
# Collaborate in groups, practice version control (if used), and present solutions.

# 🗓️ Weekly Breakdown
# Day 1: Define Classes
# Video: attributes → title, genre, video_id, available (bool).
# Customer: attributes → name, customer_id, rented_videos (list).
# VideoStore: manages collections of videos and customers.

# Day 1–3: Implement Core Functions
# In the VideoStore class:
# add_video(video) – add a new movie.
# add_customer(customer) – register a new customer.
# rent_video(customer_id, video_id) – customer rents if available.
# return_video(customer_id, video_id) – customer returns a video.
# list_available_videos() – show available movies.
# list_customer_videos(customer_id) – show what a customer has rented.

# Day 3–6: Extensions (Group Work)
# Encourage groups to add one or two enhancements:
# Search feature: by title or genre.
# Late fee system: calculate fee if not returned on time.
# Ratings system: customers rate videos.
# Collections: Use a dict for quick lookups (e.g. video_id -> Video).

# Day 7: Presentation & Review
# Groups demo renting/returning videos.
# Discuss use of OOP + collections.
# Compare different extensions.