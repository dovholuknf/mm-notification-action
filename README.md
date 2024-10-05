# mm-notification-action

Debug with:
```text
docker build -t python-action .
exampleIdentityFile=$(cat example.id.json)
exampleGithubEvent=$(cat example.github.event.json)
docker run --rm python-action --identityFile="${exampleIdentityFile}" --githubEvent="${exampleGithubEvent}}"
```
