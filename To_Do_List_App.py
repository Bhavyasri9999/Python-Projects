# create an empty list to store tasks and status

to_do_list = []

#Function to add a new task

def add_task():
    task = input("Enter a Task: ")
    to_do_list.append({"Task": task, "Status": "Pending"})
    print("Task Added Successfully!\n")

#Function to view tasks

def view_task():
   print("Your To Do List : ")
   if len(to_do_list) == 0:
      print("No Pending Tasks!")
   else:
      for index, task in enumerate(to_do_list, 1):
        print(f"{index} : {task['Task']} - {task['Status']}")
print("\n")

#Function to remove a task
def delete_task():
   if len(to_do_list) == 0:
      print("List is Empty!")
   else:
      try:
        search_index = int(input("Enter the task number you want to remove : ")) - 1
        if 0 <= search_index < len(to_do_list):
           removed_task = to_do_list.pop(search_index)
           print(f"Task Removed : {removed_task['Task']}")

        else:
         print("Invalid Task Number!")
      except ValueError:
         print("Invalid Task Number! Try Again!!")

#Function to mark as done
def Mark_done():
   if len(to_do_list) == 0:
      print("List is Empty!")
   else:
      try:
        search_index = int(input("Enter the task number you want to Mark Done : ")) - 1
        if 0 <= search_index < len(to_do_list):
           to_do_list[search_index]["Status"] = "Done"
           print(f"Task {to_do_list[search_index]['Task']} has been done!")
        else:
         print("Invalid Task Number!")
      except ValueError:
         print("Invalid Task ! Try Again!!")


#Function to display menu
def menu():

    while(True):
     print("\n--- TO DO LIST ---")
     print("1. Add All Tasks")
     print("2. View All Task")
     print("3. Delete Task")
     print("4. Mark Task as Completed")
     print("5. Exit")

     choice = input("Enter Your Choice: ")
     
     if choice == "1":
        add_task()
     elif choice == "2":
        view_task()
     elif choice == "3":
        delete_task()
     elif choice == "4":
        Mark_done()
     elif choice == "5":
        print("Exiting the Application....")
        exit()
     else:
        print("Invalid Choice! Try Again!!!")

menu()
        

















