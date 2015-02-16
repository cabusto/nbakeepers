from flask.ext.script import Server, Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from project import app, db

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(port=4000, host='0.0.0.0'))
		
if __name__ == "__main__":
    manager.run()