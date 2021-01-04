from flask_migrate import Migrate
from login import create_app
from login import models


app = create_app('testing')
migrate = Migrate(app, models.db)
