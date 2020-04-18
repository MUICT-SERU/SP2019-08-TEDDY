## USER INSTRUCTION (directly through linux terminal)
**WARNING: THIS WORKS ONLY ON LINUX OS**
1. Turn on elasticsearch server at `.\elasticsearch-2.2.0-windows\bin\elasticsearch`
2. Make sure there is no any folder located in this directory
3. At this directory, execute `AutoRunThorughComs.sh` with following order of arguments:
	- git URL
	- output results location, NOT WITHIN THE REPO (absolute path recommended)
	- name for the Elasticsearch index of the repo (no whitespace allowed)
	- Example: `.\AutoRunThorughComs https://github.com/pallets/flask.git \home\flask-results flask`
4. NOTE: Detection mode takes a considerable amount of time to complete depending on the repository's size and number of commits present.
