from models.experience_template import *
from models import db,app
with app.app_context():
    exp1=Experience(name='exp1', description='first exp', button='apply')
    exp2=Experience(name='exp2', description='second exp', button='not apply')
    exp3=Experience(name='exp3', description='third exp', button='submit')
    task1=Task(experience=exp1,title='task1',description='1st task',jira_assignee_id=1)
    task2=Task(experience=exp1,title='task2',description='2d task',jira_assignee_id=2)
    task3=Task(experience=exp1,title='task3',description='3rd task',jira_assignee_id=3)
    task4=Task(experience=exp2,title='task4',description='4th task',jira_assignee_id=4)
    task5=Task(experience=exp2,title='task5',description='5th task',jira_assignee_id=5)
    task6=Task(experience=exp3,title='task6',description='6th task',jira_assignee_id=6)
    task7=Task(experience=exp3,title='task7',description='7th task',jira_assignee_id=7)
    task8=Task(experience=exp3,title='task8',description='8th task',jira_assignee_id=8)
    task9=Task(experience=exp3,title='task9',description='9th task',jira_assignee_id=9)
    item1=Item(task=task1,text='1st item')
    item2=Item(task=task2,text='2d item')
    item3=Item(task=task3,text='3rd item')
    item4=Item(task=task4,text='4th item')
    item5=Item(task=task5,text='5th item')
    item6=Item(task=task6,text='6th item')
    item7=Item(task=task7,text='7th item')
    item8=Item(task=task8,text='8th item')
    item9=Item(task=task9,text='9th item')
    item10=Item(task=task9,text='10th item')
    kickoffinfo1=Kick_off_information(experience=exp1,label='first name',input_type='text',values=1,order=1)
    kickoffinfo2=Kick_off_information(experience=exp1,label='last name',input_type='text',values=1,order=2)
    kickoffinfo3=Kick_off_information(experience=exp1,label='age',input_type='number',values=1,order=3)
    kickoffinfo4=Kick_off_information(experience=exp3,label='customer',input_type='text',values=2,order=1)
    kickoff1=Kick_off(experience=exp1,target=1,epic_name='ajay poly kickoff',jira_epic_id=1)
    kickoff2=Kick_off(experience=exp3,target=2,epic_name='jassim k kickoff',jira_epic_id=2)
    exprunvalue1=Experience_run_values(kick_off=kickoff1,kick_off_information=kickoffinfo1,value='ajay')
    exprunvalue2=Experience_run_values(kick_off=kickoff1,kick_off_information=kickoffinfo2,value='poly')
    exprunvalue3=Experience_run_values(kick_off=kickoff1,kick_off_information=kickoffinfo3,value='21')
    exprunvalue4=Experience_run_values(kick_off=kickoff2,kick_off_information=kickoffinfo1,value='jassim')
    exprunvalue5=Experience_run_values(kick_off=kickoff2,kick_off_information=kickoffinfo2,value='k')
    exprunvalue6=Experience_run_values(kick_off=kickoff2,kick_off_information=kickoffinfo3,value='22')
    kickoffstory1=Kick_off_story(kick_off=kickoff1,task=task1,jira_task_id=1)
    kickoffstory2=Kick_off_story(kick_off=kickoff1,task=task2,jira_task_id=2)
    kickoffstory3=Kick_off_story(kick_off=kickoff1,task=task3,jira_task_id=3)
    kickoffstory4=Kick_off_story(kick_off=kickoff1,task=task4,jira_task_id=4)
    kickoffstory5=Kick_off_story(kick_off=kickoff1,task=task5,jira_task_id=5)
    kickoffstory6=Kick_off_story(kick_off=kickoff2,task=task6,jira_task_id=7)
    kickoffstory7=Kick_off_story(kick_off=kickoff2,task=task7,jira_task_id=8)
    kickoffstory8=Kick_off_story(kick_off=kickoff2,task=task8,jira_task_id=9)
    kickoffstory9=Kick_off_story(kick_off=kickoff2,task=task9,jira_task_id=10)
    itemrun1=Item_run(item=item1,kick_off_story=kickoffstory1,is_completed=False)
    itemrun2=Item_run(item=item2,kick_off_story=kickoffstory2,is_completed=False)
    itemrun3=Item_run(item=item3,kick_off_story=kickoffstory3,is_completed=False)
    itemrun4=Item_run(item=item4,kick_off_story=kickoffstory4,is_completed=False)
    itemrun5=Item_run(item=item5,kick_off_story=kickoffstory5,is_completed=False)
    itemrun6=Item_run(item=item6,kick_off_story=kickoffstory6,is_completed=False)
    itemrun7=Item_run(item=item7,kick_off_story=kickoffstory7,is_completed=False)
    itemrun8=Item_run(item=item8,kick_off_story=kickoffstory8,is_completed=False)
    itemrun9=Item_run(item=item9,kick_off_story=kickoffstory9,is_completed=False)
    itemrun10=Item_run(item=item10,kick_off_story=kickoffstory9,is_completed=False)
    sub_exp1=Sub_experience(experience=exp1,sub_experience=exp2)
    dp1=Dependencies(experience=exp1,task=task3,block_task=task2)
    dp2=Dependencies(experience=exp1,task=task2,block_task=task1)
    dp3=Dependencies(experience=exp1,sub_experience=sub_exp1,block_task=task1)
    dp4=Dependencies(experience=exp3,task=task9,block_task=task7)
    dp5=Dependencies(experience=exp3,task=task9,block_task=task8)
    dp6=Dependencies(experience=exp3,task=task7,block_task=task6)
    dp7=Dependencies(experience=exp3,task=task8,block_task=task6)
    db.session.add_all([exp1,exp2,exp3,task1,task2,task3,task4,task5,task6,task7,task8,task9,item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,kickoffinfo1,kickoffinfo2,kickoffinfo3,kickoffinfo4,kickoff1,kickoff2,exprunvalue1,exprunvalue2,exprunvalue3,exprunvalue4,exprunvalue5,exprunvalue6,kickoffstory1,kickoffstory2,kickoffstory3,kickoffstory4,kickoffstory5,kickoffstory6,kickoffstory7,kickoffstory8,kickoffstory9,itemrun1,itemrun2,itemrun3,item4,item5,item6,item7,item8,item9,item10,sub_exp1,dp1,dp2,dp3,dp4,dp5,dp6,dp7])
    db.session.commit()


# list all tasks under an experience
# select * from task t where experience_id ='92457700-af22-4bf4-b18f-693e9a089b07'

# list all subexperience under an Experience
# select * from sub_experience se where experience_id ='92457700-af22-4bf4-b18f-693e9a089b07'

# list all checklist items under an experience
# select * from item i where task_id in (select id from task t where experience_id='92457700-af22-4bf4-b18f-693e9a089b07')

# list all items under a task
# select * from item i where task_id ='cd7d5068-d3b4-4792-b2b8-b4bcdc0ba00e'

#list all kickoff under an experience
# select * from kick_off ko where ko.experience_id ='92457700-af22-4bf4-b18f-693e9a089b07'

# select kick off form of an experience
# select * from kick_off_information koi where koi.experience_id  ='92457700-af22-4bf4-b18f-693e9a089b07'

# list all kick off form values under an experience
# select * from experience_run_values erv where erv."Kick_off_id" in (select ko.id from kick_off ko where ko.experience_id='92457700-af22-4bf4-b18f-693e9a089b07')

# list all item run under an experience
# select * from item_run ir where ir."Kick_off_story_id" in (select id from kick_off_story kos  where kos.task_id in (select id from task t where t.experience_id='92457700-af22-4bf4-b18f-693e9a089b07'))

#list all item run under a task
# select * from item_run ir where ir."Kick_off_story_id" in (select id from kick_off_story kos  where kos.jira_task_id=1)

# list dependencies of an experience
# select * from dependencies d where d.experience_id ='a4f2a8e4-24ee-4547-a59f-ce19e0478a40'


#tasks unblocking steps

# list all tasks and subexp that is blocked by currently completed task
# select d.source_task ,d.source_sub_exp  from dependencies d where d.blocking_task ='34d1ca6c-fa1e-481a-b382-3008659401e3'
# add those results into separate lists
#list all blocking task and subexp for the resulting ids in the list
# select d.blocking_task,d.blocking_sub_exp from dependencies d where d.source_task  ='35b36e9c-a141-4785-b3c9-ef7525206ab2'
# select d.blocking_task,d.blocking_sub_exp from dependencies d where d.source_sub_exp  ='35b36e9c-a141-4785-b3c9-ef7525206ab2'
#if it results blocking_sub_exp we will have to query sub_experience_id from sub_experience table and check all its tasks are completed or not
#check the status of the resulting blocking_task if all are completed then unblock the source_task/source_sub_exp


# 1.kicking off
#     select all tasks and tasks under the subexp  of main exp 

# lst=[]
# data=select subexpid from subexp where id=123
# lst.append(data)
# while loopid==none:
#     loopid=select subexpid from subexp where expid=x for x in lst:
#     for i in lst:
#         if loopid.id==i:
#             loopid=none
#         else:
#             lst.append(loopid.id)

# select task from task where expid in(lst)

#     check workflow and find the first task/subexp if first task is a subexp find its first task and set it unblocked all other tasks should be blocked
#     then kickoff these tasks to jira under an epic name which will return success result then add these results to kick off table and to the kick off story table 
#     create item run table data from the kick off story (set is completed false)by default

# 2.workflow
#     if the task is completed
#     list all tasks and subexp that is blocked by currently completed task
#     if its null
#     find its parent exp using kick off story table (jira task id=task id,kick of id) from task table returs(subexpid)
#     find main exp id using kick off story (kick of id) from kick of table returns(main experience id)
#     find id from sub experience table using main experience id and subexpid
#     find which tasks are blocked by the above id
#     if its null the experience is completed 
#     select d.source_task ,d.source_sub_exp  from dependencies d where d.blocking_task =id
#     add those results into separate lists
#     list all blocking task and subexp for the resulting ids in the list
#     select d.blocking_task,d.blocking_sub_exp from dependencies d where d.source_task  ='35b36e9c-a141-4785-b3c9-ef7525206ab2'
#     select d.blocking_task,d.blocking_sub_exp from dependencies d where d.source_sub_exp  ='35b36e9c-a141-4785-b3c9-ef7525206ab2'
#     if it only blocked by any task use the kick of story id and check its status if its completed unblock the current task
#     if it blocking_sub_exp we will have to query sub_experience_id from sub_experience table and select all tasks under the subexperience
#     check the status of these tasks from the kick of story table using the same kick off id if all are completed task unblock the next task 




