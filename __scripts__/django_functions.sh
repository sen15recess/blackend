syncfork() {
	git fetch upstream;
	git checkout master;
	git merge upstream/master;
}

pullcommits() {
# If you don't have push (write) access to an upstream repository, 
# then you can pull commits from that repository into your own fork.

# Change later
	git checkout master;
	git pull https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git BRANCH_NAME;
}

update_requirements() {
	pip freeze > requirements.txt
	echo "Updated Requirements\n"
	cat requirements.txt
}
