# Login project
---

### Backend

Login project when training at Teko

### Run in development

```bash
$ python manager.py runserver --host 127.0.0.1 --port 5000
```

### Run in production (recommend use __gunicorn__ and __nginx__)

```bash
$ gunicorn -c login.config.py login.wsgi:application
```

### Frontend

```sh
$ npm run build
```
