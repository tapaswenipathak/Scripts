#!/bin/bash


read -p "Enter File Name : " file_name;
git add $file_name
echo $file_name "added"
read -p "Enter Commit Message : " message;
git commit -m $message
echo "Git Commit Successful!"
git push origin master
echo "Git Push Done."

