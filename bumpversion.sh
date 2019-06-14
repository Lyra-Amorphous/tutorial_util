#git reset --hard

# Installing required libraries for new version update of the package
echo "$ pip install -r requirements.txt"
#pip install -r requirements.txt

# Updating version - default patch
echo "$ bumpversion patch"
bumpversion patch


# Pushing new changes to the repo
git add .
git commit -m "updated patch version"
git push

