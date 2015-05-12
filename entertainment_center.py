import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Going on a trip with toys.",
                        "http://img2.wikia.nocookie.net/__cb20140317213412/disney/images/1/14/Toy-Story-3-Movie-Poster.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "Marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)

#avatar.show_trailer()

divergent = media.Movie("Divergent",
                        "Divergent from the factions",
                        "http://www.impawards.com/2014/posters/divergent_ver11_xxlg.jpg",
                        "https://www.youtube.com/watch?v=sutgWjz10sM")
#print(divergent.storyline)

#divergent.show_trailer()

movies = [toy_story, avatar, divergent]
fresh_tomatoes.open_movies_page(movies)
