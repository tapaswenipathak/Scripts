import subprocess
from subprocess import call


# Exracting the links
find_links = subprocess.Popen(
    ["lynx -dump -listonly bookmarks_7_24_14.html > BookMarks1.txt"], stdin=subprocess.PIPE, shell=True)
find_links.communicate("Make The File\n")
find_links.wait()

find_links = subprocess.Popen(
    ["lynx -dump -listonly bookmarks_7_25_14.html > BookMarks2.txt"], stdin=subprocess.PIPE, shell=True)
find_links.communicate("Make The File\n")
find_links.wait()


# Finding the difference and saving it in a file
find_diff = subprocess.Popen(
    ["diff BookMarks1.txt BookMarks2.txt > NewBookMarks.txt"], stdin=subprocess.PIPE, shell=True)
find_diff.communicate("Find Difference\n")
find_diff.wait()


# Merge the file having the difference and previous bookmarks file into a
# new single bigger file
Update_file = subprocess.Popen(
    ["sort -n BookMarks1.txt NewBookMarks.txt > UpdatedBookMarks.txt"], stdin=subprocess.PIPE, shell=True)
Update_file.communicate("Your Output Created\n")
Update_file.wait()


# Delete the files created in the process of finding the updated one
call(["rm", "BookMarks1.txt"])
call(["rm", "BookMarks2.txt"])
call(["rm", "NewBookMarks.txt"])
call(["rm", "bookmarks_7_24_14.html"])
call(["rm", "bookmarks_7_25_14.html"])
