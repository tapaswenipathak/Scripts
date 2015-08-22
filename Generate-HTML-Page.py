# Create HTML File For Writing
f = open('Fun.html', 'w')


# Writing Starting Tags & Code for V1 Google Search in HTML file
message = """<html>
  <head>
	  <title> Preparation </title>
	</head>
	<body>
    <div>  
      <script>
        (function() {
        var cx = '008056931742069760033:arfzvopx6zc';
        var gcse = document.createElement('script');
        gcse.type = 'text/javascript';
        gcse.async = true;
        gcse.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') +
        '//www.google.com/cse/cse.js?cx=' + cx;
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(gcse, s);
        })();
     </script>
     <gcse:search></gcse:search>
  </div>
	  <center> 
		<p> <font size = "6" color = "Red"> Read Articles </font> </p>
	  """
f.write(message)


# Ask For User's Choice
choice = raw_input("Do you have any links to add?(y/n) : ")

if choice == "y":
    while True:

        # Enter Link & Title of The Link
        link = raw_input("Enter link : ")
        title = raw_input("Enter title of the link : ")

        # Intialize Message & Write It In The File
        message = "<a href = \"" + link + "\" target=\"_blank\" >" + title + "</a> </br>"
        f.write(message)
        choice = raw_input("Do you have any links to add?(y/n) : ")
        if choice == "n":
            break
        elif choice != "n" and choice != "y":
            choice = raw_input("Do you have any links to add?(y/n) : ")

elif choice == "n":
    print "Sure."
    print "Thanks!"
else:
    print "OOps Wrong Choice!"


# Writing Tags For Words & Meanings
message = """
		<p> <font size = "6" color = "Red"> Words & Meanings </font> </p>
		"""
f.write(message)


# Input User's Choice
choice = raw_input("Do you have any words & meanings to add?(y/n) : ")
if choice == "y":
    while True:

        # Ask For Word & It's Meaning
        word = raw_input("Enter  word: ")
        meaning_link = raw_input("Enter meaning link : ")

        # Write The Generated Code In The HTML File
        message = "<a href = \"" + meaning_link + \
            "\" target=\"_blank\">" + word + "</a> </br>"
        f.write(message)
        choice = raw_input("Do you have any words & meanings to add?(y/n) : ")
        if choice == "n":
            print "Sure."
            print "Thanks!"
            break
        elif choice != "n" and choice != "y":
            choice = raw_input(
                "Do you have any words & meanings to add?(y/n) : ")
elif choice == "n":
    print "Sure."
    print "Thanks!"
else:
    print "OOps Wrong Choice!"


# Write Code For A Motivation GIF At The End of The Page
message = """    </br>	</br>
		</br> </br>
    </br> </br>
		</br> </br>
		<marquee behavior="scroll" direction="left"> <img src="http://www.allgifs.com/wp-content/uploads/2013/08/tumblr_mrmi90oEHD1srth6oo1_400.gif" width="300" height="300" alt="<3">
		</marquee>"""
f.write(message)


# Write The Ending Tags/Code In The HTML File
message = """
    </center>  
  </body>
</html>"""
f.write(message)


# Close It
f.close()
