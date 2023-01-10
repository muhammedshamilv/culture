import uuid
from models import db
from sqlalchemy.dialects.postgresql import UUID,ENUM
from sqlalchemy_utils import URLType
from enum import Enum, unique

@unique
class input_typeEnum(Enum):
    text = 'text'
    number = 'number'
    date = 'date' 

class Experience(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    name = db.Column(db.String(80), unique=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    url = db.Column(URLType)
    description = db.Column(db.Text)
    Can_be_kicked_off = db.Column(db.Boolean)
    target = db.Column(db.Boolean)
    button_text = db.Column(db.String(80))
    
    kick_off_information = db.relationship('Kick_off_information', backref='experience')
    kick_off = db.relationship('Kick_off', backref='experience')
    task = db.relationship('Task', backref='experience')
    dependencies = db.relationship('Dependencies', backref='experience')
    
    def __repr__(self):
        return '<Experience %r>' % self.name


class Kick_off_information(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    experience_id=  db.Column(UUID(as_uuid=True), db.ForeignKey('experience.id'))
    label = db.Column(db.String(80))
    input_type = db.Column(ENUM(input_typeEnum),nullable=False)
    values = db.Column(db.String(120))
    order = db.Column(db.Integer)
    use_for_epic_name = db.Column(db.Boolean)

    experience_run_values = db.relationship('Experience_run_values', backref='kick_off_information')

    def __repr__(self):
        return '<Kick of information %r>' % self.id


class Kick_off(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    experience_id= db.Column(UUID(as_uuid=True), db.ForeignKey('experience.id'))
    target = db.Column(db.Integer)
    epic_name = db.Column(db.String(120), unique=True)
    created_at = db.Column(db.String(120), unique=True)
    jira_epic_id = db.Column(db.Integer)
    is_completed=db.Column(db.Boolean)

    experience_run_values = db.relationship('Experience_run_values', backref='kick_off')
    kick_off_story = db.relationship('Kick_off_story', backref='kick_off')


    def __repr__(self):
        return '<Kick off %r>' % self.id


class Experience_run_values(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    Kick_off_id = db.Column(UUID(as_uuid=True), db.ForeignKey('kick_off.id'))
    field_id= db.Column(UUID(as_uuid=True), db.ForeignKey('kick_off_information.id'))
    value = db.Column(db.String(120))

    def __repr__(self):
        return '<Experience run values %r>' % self.id


class Kick_off_story(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    Kick_off_id = db.Column(UUID(as_uuid=True), db.ForeignKey('kick_off.id'))
    task_id= db.Column(UUID(as_uuid=True), db.ForeignKey('task.id'))
    jira_task_id = db.Column(db.Integer, unique=True)
    is_completed=db.Column(db.Boolean)

    item_run = db.relationship('Item_run', backref='kick_off_story')

    def __repr__(self):
        return '<Kick of story %r>' % self.id


class Task(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    experience_id= db.Column(UUID(as_uuid=True), db.ForeignKey('experience.id'))
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)
    url = db.Column(URLType)
    creates_jira_user=db.Column(db.Boolean)
    jira_assignee_id= db.Column(db.Integer, unique=True)

    kick_off_story = db.relationship('Kick_off_story', backref='task')
    item = db.relationship('Item', backref='task')
    

    def __repr__(self):
        return '<Task %r>' % self.id


class Item(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    task_id = db.Column(UUID(as_uuid=True), db.ForeignKey('task.id'))
    text = db.Column(db.Text)

    Item_run = db.relationship('Item_run', backref='item')

    def __repr__(self):
        return '<Item %r>' % self.id


class Item_run(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    item_id = db.Column(UUID(as_uuid=True), db.ForeignKey('item.id'))
    Kick_off_story_id = db.Column(UUID(as_uuid=True), db.ForeignKey('kick_off_story.id'))
    is_completed = db.Column(db.Boolean)

    def __repr__(self):
        return '<Item run %r>' % self.id

    def get_item(self):
        return self.item_id.text

# objects = Item_run.all()
# for obj in objets: 
#   print(obj.get_item())

class Sub_experience(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    experience_id = db.Column(UUID(as_uuid=True), db.ForeignKey('experience.id'))
    sub_experience_id = db.Column(UUID(as_uuid=True), db.ForeignKey('experience.id'))

    experience = db.relationship('Experience',backref='sub_experience',foreign_keys=[experience_id])
    sub_experience = db.relationship('Experience',foreign_keys=[sub_experience_id])

    def __repr__(self):
        return '<Sub experience %r>' % self.id


class Dependencies(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    experience_id = db.Column(UUID(as_uuid=True), db.ForeignKey('experience.id'))
    source_task = db.Column(UUID(as_uuid=True), db.ForeignKey('task.id'))
    source_sub_exp = db.Column(UUID(as_uuid=True), db.ForeignKey('sub_experience.id'))
    blocking_task = db.Column(UUID(as_uuid=True), db.ForeignKey('task.id'))
    blocking_sub_exp = db.Column(UUID(as_uuid=True), db.ForeignKey('sub_experience.id'))

    task = db.relationship('Task',backref='Dependencies',foreign_keys=[source_task])
    block_task = db.relationship('Task',foreign_keys=[blocking_task])

    sub_experience = db.relationship('Sub_experience',backref='Dependencies',foreign_keys=[source_sub_exp])
    block_sub_exp = db.relationship('Sub_experience',foreign_keys=[blocking_sub_exp])

    def __repr__(self):
        return '<DEpendencies %r>' % self.id
