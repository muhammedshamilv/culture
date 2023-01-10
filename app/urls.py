from flask import Blueprint
from views.experience import task,template

tasks = Blueprint('task', __name__, url_prefix='')

tasks.add_url_rule('/all/experiences/', view_func=template.get_experiences,methods=['GET'])

tasks.add_url_rule('/home', view_func=task.home,methods=['GET'])
