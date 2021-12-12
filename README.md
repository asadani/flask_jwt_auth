# Flask JWT Authorization: Beginner

Nowadays many of the services (microservices) do not deal with user management rather there is single user management or gateway service that handles the authentication. However, the authorization is the responsibility of individual services.

> Authentication is the process of verifying who someone is.
> Authorization is the process of verifying what specific applications, files, and data a user has access to.

## Steps

Create a virtual environment for the project
```
> python -m venv .env
> source .env/bin/activate
> pip install -r requirements.txt
```

## Run and Test

**Start the flask application:** 

`flask run` or `python app.py`

**Testing the routes using curl**
```
/home/anuj/work [anuj@devmachine]
> export ADMINTOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiQ29tbWFuZG8gRGhydXZhIiwiZW1haWwiOiJjb21tYW5kby5kaHJ1dmFAc3VwZXJoZXJvcy5jb20iLCJkaXNwbGF5TmFtZSI6IkRocnV2YSIsInJvbGVzIjpbImFkbWluIiwidmlld2VyIl0sInVzZXJJZCI6MjEwMH0.JbNrJkDdAKrtTFMl8gwLbEisWiniwMng6u_9J1dN2GY
 
/home/anuj/work [anuj@devmachine]
> export VIEWERTOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiUmFqIFNoYWgiLCJlbWFpbCI6Im5hZ3JhakBzdXBlcmhlcm9zLmNvbSIsImRpc3BsYXlOYW1lIjoiTmFncmFqIiwicm9sZXMiOlsidmlld2VyIl0sInVzZXJJZCI6MjEwMn0.ulVozC-QMaOrEjz6bGG-YRKiZXoyigambT6khXYoUSk

/home/anuj/work [anuj@devmachine]
> curl -XGET "http://127.0.0.1:5000/employee"                                    
{
  "message": "Welcome to employee portal"
}
/home/anuj/work [anuj@devmachine]
> curl -H "x-access-token:$ADMINTOKEN" -XGET "http://127.0.0.1:5000/employee/info" 
{
  "data": [
    {
      "department": "R&D", 
      "emp_id": 5870, 
      "name": "Doga"
    }, 
    {
      "department": "Engineering", 
      "emp_id": 5871, 
      "name": "Shakti"
    }
  ]
}

/home/anuj/work [anuj@devmachine]
> curl -H "x-access-token:$ADMINTOKEN" -XGET "http://127.0.0.1:5000/employee/salary"
{
  "data": [
    {
      "emp_id": 5870, 
      "salary": 55000
    }, 
    {
      "emp_id": 5871, 
      "salary": 55000
    }
  ]
}
 
/home/anuj/work [anuj@devmachine]
> curl -H "x-access-token:$VIEWERTOKEN" -XGET "http://127.0.0.1:5000/employee/info"
{
  "data": [
    {
      "department": "R&D", 
      "emp_id": 5870, 
      "name": "Doga"
    }, 
    {
      "department": "Engineering", 
      "emp_id": 5871, 
      "name": "Shakti"
    }
  ]
}

/home/anuj/work [anuj@devmachine]
> curl -H "x-access-token:$VIEWERTOKEN" -XGET "http://127.0.0.1:5000/employee/salary"
{
  "message": "Not authorized to access the API"
}
```
