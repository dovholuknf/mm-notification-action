# mm-notification-action

Debug with:
```text
docker build -t python-action .
example=$(cat example.json)
docker run --rm python-action --example_input1="<input1>" --example_input2="$example"
```
