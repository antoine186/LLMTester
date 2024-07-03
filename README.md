# LLM Testing Challenge

## Running backend using docker:
- docker build --tag python-docker .
- docker run -d -p 5000:5000 python-docker
- docker ps
- docker exec -it mycontainerid bash
- ollama run llama3 (And wait for installation to complete)

## If docker approach doesn't work, use vscode debug:
* Install VSCode and open project using VSCode.
* In VSCode, do CTRL+SHIFT+D. Press on the play button that appears on the left (not the one on the right).

* Wait until "Running on http://127.0.0.1:5000"

* Install ollama using the .exe installer from the official site: https://ollama.com/download.
* In command line, run "ollama pull llama3".
* "ollama run llama3".

# Ping the backend using Postman
* Install the Postman API client
* In Postman, click the "New" button in the top left. A new request template should popup.
* Switch the template from GET to POST. Paste http://127.0.0.1:5000/api/simulate-user-test-case-1-blueprint in your url box.
* Below the url box is a nav bar with "body". Click that and then select "raw". Paste the below in:

{
    "data": {
        "chatbot_to_test": 1
    }
}

* Press the "SEND" button and wait for Postman to display the result.
