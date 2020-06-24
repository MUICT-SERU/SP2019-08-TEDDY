# Teddy: Automatic Recommendation of Pythonic Idiom Usage For Pull-Based Software Projects
A repo for the Teddy tool. 

## Required Components
- Elasticsearch **2.2.0**
- Apache Maven 3.6.3 or higher

## Setting up Elasticsearch 2.2.0
1. In `.\config\elasticsearch.yml` file of Elasticsearch folder, add `index.query.bool.max_clause_count: 20480` and `action.auto_create_index: .marvel-*` to the file. Save and close the file.

1. Using `cmd` or PowerShell Go to `.\bin` directory of your local Elasticsearch folder.
2. Execute `.\elasticsearch` command to run an Elasticsearch instance.

## Setting up Teddy
1. Use `git clone` to make a local copy of this branch on your machine, or download this branch as a `.zip` package and extract it.

2. From `.\config\elasticsearch.yml` file in the Elasticsearch folder, check the value of the parameter `cluster.name`, then set the value of the property `cluster` inside `.\webapp\config.properties` in SP2019-TEDDY folder to be the same name.

3. In `config.properties` file, be sure to set the value of property `index` to be the name of an existing index in your local Elasticsearch. (To see the list of index in your Elasticsearch, go to `localhost:9200/_cat/indices?v=pretty` on a web browser).

4. Using another `cmd` or PowerShell instance, go to `.\webbapp` directory of SP2019-TEDDY folder

5. Use the command `mvn spring-boot:run` to launch Spring-boot framework and run TEDDY

6. On any web browser, go to `localhost:8080/search` to start using TEDDY (Google Chrome is recommended).

## PREVENTION MODE USER INSTALLATION

** DON - Please work on this part **

## DETECTION MODE USER INSTRUCTION (directly via Linux terminal)

**WARNING: These steps have only been tested on Linux **

**DO NOT REMOVE ANY OF THE FILES IN THIS FOLDER**

0. Needed dependencies and library before start using:
	- Java JDK 1.8 or above
	- Python 3.X.X
	- `pandas` library for Python
	- `bokeh` library for Python
	- `git` bash for Linux
1. Open a terminal and turn on Elasticsearch server (`./elasticsearch`) at `~/elasticsearch-2.2.0-linux/bin`
2. Make sure there is no any folder located in the directory `~/detection-mode/`
3. Open another terminal and execute `AutoRun.sh` at `~/detection-mode/` with the following order of arguments:
	- `.git` URL of a GitHub repository
	- directory for the result CSV files from Siamese to be saved, NOT within THE REPO (absolute path recommended)
	- name for the Elasticsearch index of the repo (no whitespace allowed)
	- **Example: `$ ./AutoRun https://github.com/pallets/flask.git /home/flask-results flask`**
4. Finally, a file named `myplot.html` will be created here. This is the final visualization of detection mode. Move it to wherever you like. Use a web browswer (Google Chrome is recommended) to view the file.
5. NOTE: Detection mode takes a considerable amount of time to complete depending on the repository's size and number of commits present.

