from flask import Flask, request, jsonify
from frontend.render_routes import render

app = Flask(
    __name__,
    template_folder='frontend/templates',
    static_folder='frontend/static'
)

render(app)

if __name__ == '__main__':
    app.run(debug=True)