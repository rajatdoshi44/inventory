# Users service

Run from the `be` directory with `make users` (port 8003). Initialize the database
first with `make create-tables`.

Endpoints:

- `POST /users` — create a user
- `GET /users?offset=0&limit=50` — list users
- `GET /users/{user_id}` — get a user
- `PATCH /users/{user_id}` — update user fields
- `DELETE /users/{user_id}` — delete a user

Passwords are stored as scrypt hashes and are never included in API responses.
These routes currently have no authentication or authorization; do not expose
them publicly until access controls are added.