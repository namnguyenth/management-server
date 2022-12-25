Requirements
  ```Python 3.8```
  ```MySql```

Setting up environment
  ```
  Create .env file in the main folder.
  Copy the content from .env.example file to .env file.
  Edit postgres info as needed
  ```
 
Migrate DB
  Run these commands:

  ```flask db init```

  ```flask db migrate -m "Initial migration."```

  ```flask db upgrade```
  
Run Server
  ```flask run```
