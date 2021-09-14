from flask_migrate import Migrate
from applications import create_app
from applications.extensions.init_sqlalchemy import db

app = create_app(config_name="development")
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
