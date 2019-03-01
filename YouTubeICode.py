import pafy

url = raw_input("Enter your URL : ")

# Creating an instance
video = pafy.new(url)

# Users Choice
print "Do You Want To Download It , or Want To Extract Information ?"
choice = raw_input("Input d To Download or ei To Extract Information : ")

# Actions on Choices
if choice == 'd':
    # Get the best video url
    best = video.getbest()
    # Print relevant information, when downloading the file
    best.download(quiet=False)

elif choice == 'ei':
    print "Title : " + video.title
    print "Rating : " + str(video.rating)
    print "View Count : " + str(video.viewcount) + " Author : " + video.author + " Length : " + str(video.length)
    print "Duration : " + str(video.duration) + " Likes : " + str(video.likes) + " Dislikes : " + str(video.dislikes)
    print "Description : " + video.description
    print "Published on Date : " + str(video.published)

else:
    print "OOps Wrong Choice!"
