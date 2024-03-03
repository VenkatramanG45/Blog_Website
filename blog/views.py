from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"Maxmillian",
        "date":date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": " There's nothing like a views you get when Hiking Mountain,Its Really Enjoyable and Give Soul Peace to Mental and Physical Health to Heal from weird Memory.",
        "content":"""
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Soluta architecto est itaque fugiat tempore eum aperiam saepe harum, 
        blanditiis molestias sint debitis eaque quae exercitationem? Enim aliquid a quae natus.     
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Soluta architecto est itaque fugiat tempore eum aperiam saepe harum, 
        blanditiis molestias sint debitis eaque quae exercitationem? Enim aliquid a quae natus.
            
            
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Soluta architecto est itaque fugiat tempore eum aperiam saepe harum, 
        blanditiis molestias sint debitis eaque quae exercitationem? Enim aliquid a quae natus.
        """
    },
    
    {
        "slug": "into-the-woods",
        "image":"woods.jpg",
        "author":"Maxmillian",
        "date":date(2021, 7, 21),
        "title": "Nature at Best",
        "excerpt": " There's nothing like a views you get when Hiking Mountain,Its Really Enjoyable and Give Soul Peace to Mental and Physical Health to Heal from weird Memory.",
        "content":"""
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Soluta architecto est itaque fugiat tempore eum aperiam saepe harum, 
        blanditiis molestias sint debitis eaque quae exercitationem? Enim aliquid a quae natus.     
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Soluta architecto est itaque fugiat tempore eum aperiam saepe harum, 
        blanditiis molestias sint debitis eaque quae exercitationem? Enim aliquid a quae natus.
            
            
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Soluta architecto est itaque fugiat tempore eum aperiam saepe harum, 
        blanditiis molestias sint debitis eaque quae exercitationem? Enim aliquid a quae natus.
        """
    },
    
    {
        "slug": "programming-is-fun",
        "image":"coding.jpg",
        "author":"Maxmillian",
        "date":date(2021, 7, 21),
        "title": "Coding is Best",
        "excerpt": " There's nothing like a views you get when Hiking Mountain,Its Really Enjoyable and Give Soul Peace to Mental and Physical Health to Heal from weird Memory.",
        "content":"""
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Soluta architecto est itaque fugiat tempore eum aperiam saepe harum, 
        blanditiis molestias sint debitis eaque quae exercitationem? Enim aliquid a quae natus.     
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Soluta architecto est itaque fugiat tempore eum aperiam saepe harum, 
        blanditiis molestias sint debitis eaque quae exercitationem? Enim aliquid a quae natus.
            
            
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Soluta architecto est itaque fugiat tempore eum aperiam saepe harum, 
        blanditiis molestias sint debitis eaque quae exercitationem? Enim aliquid a quae natus.
        """
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    
    return render(request, "blog/index.html",{
        "posts": latest_posts       
    })

def posts(requests):
    return render(requests, "blog/all-posts.html",{
        "all_posts": all_posts
    })


def post_details(requests,slug):
    identified_posts =next(post for post in all_posts if post["slug"] == slug)
    return render(requests, "blog/post-detail.html", {
        "post": identified_posts
    })
# Create your views here.
