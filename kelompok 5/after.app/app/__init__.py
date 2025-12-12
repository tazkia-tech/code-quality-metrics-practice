import os
from flask import Flask

def create_app():
    # path ke folder after_app (project dir)
    root_dir = os.path.dirname(os.path.abspath(__file__))        # .../after_app/app
    project_dir = os.path.dirname(root_dir)                      # .../after_app

    app = Flask(
        __name__,
        template_folder=os.path.join(project_dir, 'templates'),
        static_folder=os.path.join(project_dir, 'static')
    )

    from app.routes import main
    app.register_blueprint(main)

    return app
