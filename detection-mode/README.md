## USER INSTRUCTION (directly through linux terminal)
**WARNING: THIS WORKS ONLY ON LINUX OS**
1. On a terminal, turn on Elasticsearch server (`./elasticsearch`) at `~/elasticsearch-2.2.0-linux/bin`
2. Make sure there is no any folder located in this directory (`~/detection-mode/`)
3. Open another terminal, execute `AutoRunThorughComs.sh` at `~/detection-mode/` with the following order of arguments:
	- `.git` URL of a GitHub repository
	- directory for the result files, NOT within THE REPO (absolute path recommended)
	- name for the Elasticsearch index of the repo (no whitespace allowed)
	- Example: `$ .\AutoRunThorughComs https://github.com/pallets/flask.git \home\flask-results flask`
4. NOTE: Detection mode takes a considerable amount of time to complete depending on the repository's size and number of commits present.
