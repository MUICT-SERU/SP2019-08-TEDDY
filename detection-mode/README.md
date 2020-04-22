## TEDDY DETECTION MODE USER INSTRUCTION (directly via Linux terminal)

**WARNING: THIS WORKS ONLY ON LINUX OS**

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
	- **Example: `$ ./AutoRunThorughComs https://github.com/pallets/flask.git /home/flask-results flask`**
4. Finally, a file named `myplot.html` will be created here. This is the final visualization of detection mode. Move it to wherever you like. Use a web browswer (Google Chrome is recommended) to view the file.
5. NOTE: Detection mode takes a considerable amount of time to complete depending on the repository's size and number of commits present.
