# pypy-eventlet-bug

## Reproduction

1. Start a server:

  ```sh
  twistd --pidfile= -l - -o -n web --path=. -p 8000
  ```

2. Run `make_requests.py`:

  ```sh
  pip freeze -l | grep eventlet && python --version && TARGET_HOST=http://127.0.0.1:8000 python make_requests.py
  ```
