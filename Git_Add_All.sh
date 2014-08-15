#!/bin/bash

echo "To commit follow the process."
read -p "Enter commit message : " message;
git add -A
echo "All files added"
git commit -m $message
echo "Commit Successful!"
git push origin master
echo "Push Done"
