
# REST API Challenge

1. Automation of REST APIs using **Python 3.12**, **pytest**, and **requests** libraries.
2. Login API will provide authentication token for other APIs access. 
3. Automated postive flow of REST APIs. 
4. Used own REST API: **https://aanurupdas.pythonanywhere.com**   





## API Reference
EMAIL: admin@admin.com, PASSWORD: admin

#### Login user

```http
  POST /api/login
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Required**. Email |
| `password` | `string` | **Required**. Password |

#### Get all users

```http
  GET /api/list
```
#### Get user details

```http
  GET /api/get/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of user to fetch |

#### Update user details

```http
   PUT /api/update/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of user to fetch & update |

## Installation

Install requirements with pip

```bash
  pip install -r requirements.txt
```
    
## Running Tests

To run tests, run the following command

```bash
  python run_tests.py
```