#!/bin/sh
# This shell must receive the path of where the GitHub is cloned and stored in $cloneRepoPath
#
# Command-line arguments
# $1 - path to the cloned repository
# $2 - path to the idiom/non-idiom snippets
# $3 - path for the output files to be saved
# $4 - name for the cloned repository Elasticsearch index
# $5 - commitID
# $6 - version tracking num (start from 1) of the cloned repo

idiomPath = "D:\senior-project\python3-idiom"

# Reading of $indexName variable is optional if Don's script can get ES index's name from the user already
echo "Enter index name for your repository"
read indexName


# Indexing the cloned repo
java -jar siamese.jar -cf ./config.properties -c index -i $1 -n $4

# Searching in the newly created ES index using the idiom/non-idiom Python snippets
# '-n' is a new command-line overriding parameter of .jar for index in config.properties
java -jar siamese.jar -cf ./config.properties -c search -i $2 -o $3 -n $4

echo "Search completed"

