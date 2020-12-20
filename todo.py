import sys
import os
import datetime

# when "add" command is executed
def add_to_todo(file_path,task):
    with open(file_path,"a") as f:
        f.write(task)
        f.write("\n")
    
    print("Added todo:",task)


# when "report" command is executed
def get_remaining_tasks_num(todo_filepath):
    with open(todo_filepath,"r") as f:
        num_of_rem_tasks = len(f.readlines())
        return num_of_rem_tasks

# when "report" command is executed
def get_done_tasks_num(done_filepath):
    #check if done.txt is empty
    if(os.stat(done_filepath).st_size != 0):
        with open(done_filepath,"r") as f:        
            num_of_done_tasks = len(f.readlines())
            return num_of_done_tasks
    else:
        return 0

# when "ls" command is executed
def print_todo_tasks(file_path):
    with open("todo.txt","r") as f:
        tasks = f.readlines()
        count = len(tasks)

        # printing tasks in opposite order 4,3,2,...
        for i in tasks[-1::-1]:
            print("["+str(count)+"]", i,end="")
            count -= 1


# when "done" command is executed
def remove_from_todo(todo_filepath, done_filepath, completed_task_number):

    #Read all lines(tasks) from todo.txt
    with open(todo_filepath,"r") as f:
        lines = f.readlines()

    completed_task = lines[completed_task_number-1] # as indexing starts from 0

    # add the completed task in done.txt
    add_to_done(done_filepath, completed_task)

    # remove the completed task from todo.txt
    del lines[completed_task_number-1]
    with open(todo_filepath,"w") as f:
        for line in lines:
            f.write(line)

    print("Marked todo #"+ str(completed_task_number), "as done.")


# helper function for remove_from_todo(); runs when "done" command is executed
def add_to_done(done_filepath, completed_task):
    date = str(datetime.datetime.now()).split(" ")[0]

    with open("done.txt","a") as f:
        f.write("x " + date + " " + completed_task)

# when "del" command is executed
def delete_task(todo_filepath, task_number):
    with open(todo_filepath,"r") as f:
        lines = f.readlines()

    del lines[task_number-1] # as indexing starts from 0
    with open(todo_filepath,"w") as f:
        for line in lines:
            f.write(line)
    print("Deleted todo #"+ str(task_number))


# Driver Code

# "Help" command
if(len(sys.argv) == 1 and str(sys.argv[0]) == 'todo.py' or str(sys.argv[1]) == 'help'):
    print("Usage :-")
    print("$ ./todo add \"todo item\"  # Add a new todo")
    print("$ ./todo ls               # Show remaining todos")
    print("$ ./todo del NUMBER       # Delete a todo")
    print("$ ./todo done NUMBER      # Complete a todo")
    print("$ ./todo help             # Show usage")
    print("$ ./todo report           # Statistics")


# "report" command
elif(len(sys.argv) !=0  and str(sys.argv[1]) == 'report'):
    num_of_todo_tasks = get_remaining_tasks_num("todo.txt")
    num_of_done_tasks = get_done_tasks_num("done.txt")
    print("Pending :",num_of_todo_tasks, "Completed :",num_of_done_tasks)


# "add" command
elif(len(sys.argv) !=0  and str(sys.argv[1]) == 'add'):
    add_to_todo("todo.txt", str(sys.argv[2]))


# "ls" command
elif(len(sys.argv) !=0  and str(sys.argv[1]) == 'ls'):
    print_todo_tasks("todo.txt")


# "done" command
elif(len(sys.argv) !=0  and str(sys.argv[1]) == 'done' and str(sys.argv[2]) != None):
    completed_task_number = int(sys.argv[2])
    done_task = remove_from_todo("todo.txt", "done.txt", completed_task_number)


# "del" command
elif(len(sys.argv) !=0  and str(sys.argv[1]) == 'del' and str(sys.argv[2]) != None):
    task_number = int(sys.argv[2])
    delete_task("todo.txt", task_number)