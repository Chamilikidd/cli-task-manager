#IMPORTS
import uuid
import datetime #for date and time of task created
import os #so python can search through my directory
import json #so I can save tasks

#setting variables

priorities = ['High', 'Medium', 'Low']
user = input ("What's your name?")
user = user.capitalize().strip()
#pulling JSON Saves into program
if os.path.exists('tasks.json') and os.path.getsize('tasks.json') > 0:
	with open("tasks.json", "r") as f:
		tasks = json.load(f)
else:
	tasks = []
#add a task
def addtask():
	addnumber = int(input('How Many Tasks would you like to add?'))
	for i in range(addnumber):
		taskname = input('what is the name of your task?')
		taskname = taskname.capitalize().strip()
		taskpriority = input('What priority is this task, High, Mediumn or Low?')
		taskpriority = taskpriority.capitalize().strip()
		timecreated = datetime.datetime.now()
		task = {
			"id": str(uuid.uuid4()),
			"name": taskname,
			"priority": taskpriority,
			"created": timecreated.strftime("%Y - %m - %d %H: %m: %s"),
			"completed": False
			}
		tasks.append(task)
	menu()
#view tasks
def taskview():
	for i, task in enumerate(tasks):
		#add this too top print(f"=Your Tasks=")
		print(f"===\nTask {task['id']}\n Name: {task['name']}\n Priority: {task['priority']}\nComplete: {task['completed']}\nTime Created: {task['created']}")
	menu()


#Mark Task As Complete
def taskcomplete():
	amount = int(input("How many tasks would you like to mark as complete?"))
	for a, task in enumerate(tasks):
		print(f"Task ID: {task['id']}\nName: {task['name']}\nPriority: {task['priority']}\nComplete: {task['completed']}\nTime Created: {task['created']}")
	for p in range(amount):
		mark = input('Please enter the ID of the task you would like to mark as complete')
		for task in tasks:
			if task['id'] == mark:
				task['completed'] = True
	menu()


def save():
	print("saving tasks")
	with open("tasks.json", "w") as f:
		json.dump(tasks, f, indent=4)
	menu()
#CREATING MENU
def menu():
	print(f"Hello {user} and welcome to your task manager.\n")
	menuoption = int(input(f"What would you like to do today?\n=1= Create a Task.\n=2= View your Tasks\n=3= Mark a task as complete \n=4= Save \n=5= Exit"))
	if menuoption == 1:
		addtask()
	elif menuoption == 2:
		taskview()
	elif menuoption == 3:
		taskcomplete()
	elif menuoption == 5:
		exit()
	elif menuoption == 4:
		save()
	else:
		print('Invalid option, please select 1, 2, 3, 4')
		menu()

menu()
