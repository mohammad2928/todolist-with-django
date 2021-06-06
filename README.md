# todolist-with-django

You can manage your TODO tasks with this app.


# Installation (python 3)
```
pip install -r requierments.txt
```
# Running

```
cd todolist
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
```

If you have any question or suggest, please make an issue. 

# Apis

## getting all tasks
```
curl http://127.0.0.1:8000/api/
```

## post a new task
```
url = "http://127.0.0.1:8000/api/"
payload = {
"name":"task title",
"priority": 2,
"description": "no description"
}

response = requests.post(url, data=payload)
print(response.json())
```

## get by task id

```
curl -X "GET" http://127.0.0.1:8000/api/8/
```

## update by task id 

```
curl -X "PUT" http://127.0.0.1:8000/api/8/  -H "Content-Type: application/json" -d '{ "name":"NEW NAME"}'
``` 

## remove by a tag id 

```
curl -X "DELETE" http://127.0.0.1:8000/api/8/
```