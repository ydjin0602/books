# books

#General information
Service that implements a library for demonstrating CRUD requests

#Environment variables
 | Name | Default | Description| 
 | --- | --- | --- |
 | APP_PORT | "" | Application port |
 | PG_HOST | "postgres" | PostgreSQL host |
 | PG_PORT | "5432" | PostgreSQL port |
 | PG_DATABASE | "books" | PostgreSQL database |
 | PG_USERNAME | "dev" | PostgreSQL username |
 | PG_PASSWORD | "dev" | Postgres password |

# [Dependencies](requirements.txt)

# Run service
1. Clone repository.
2. Set environment variables in `.env` file.
3. Run command `docker-compose up -d --build`

#Viewing logs
 - `docker logs <container_id>`


# Default CRUD requests
 - Get a book:
```
GET localhost:port/?id=<id>
```
Request body:
```
{
    "author": str,
    "id": int,
    "pages_num": int,
    "title": str
}
```

 - Get all books:
```
GET localhost:port/?id=all_books
```
Response body:
```
{
    "result": [
        {
            "author": str,
            "id": int,
            "pages_num": int,
            "title": str
        }
    ]
}
```

- Create a book:
```
POST localhost:port/
```
Request body:
```
{
    "title": str,
    "author": str,
    "pages_num": int
}
```
Response body:
```
{
    "author": str,
    "id": int,
    "pages_num": int,
    "title": str
}
```

- Update a book:
```
PUT localhost:port/
```
Request body:
```
{
    "author": str,
    "id": int,
    "pages_num": int,
    "title": str
}
```
Response body:
```
{
    "author": str,
    "id": int,
    "pages_num": int,
    "title": str
}
```

- Delete a book:
```
DELETE localhost:port/
```
Request body:
```
{
    "id": int
}
```
Response body:
```
{
    "id": int,
    "result": "Book successfully deleted."
}
```

#Error responses
 - Invalid request body
```
{
    "error": "request body is invalid."
}
```

- Some errors with SQLAlchemy
```
{
    "error": "transaction error."
}
```

- Book not found (GET and DELETE requests)
```
{
    "error": "Book not found."
}
```