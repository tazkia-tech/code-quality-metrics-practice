import os
from flask import Flask

def create_app():
    root_dir = os.path.dirname(os.path.abspath(__file__))  
    project_dir = os.path.dirname(root_dir)  

    app = Flask(
        __name__,
        template_folder=os.path.join(project_dir, 'templates'),
        static_folder=os.path.join(project_dir, 'static')
    )

    from .routes import main
    app.register_blueprint(main)

    return app