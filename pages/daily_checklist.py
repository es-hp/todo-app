# === Imports ===
import os
from tools import divider, line_breaks, h1, h2, h3, h4, invalid_msg, success_msg, create_new_form, load_json, save_json, increase_level, increase_tips, decrease_tips

# === Data File Paths

current_folder = os.path.dirname(__file__)
dailies_data_path = os.path.abspath(os.path.join(current_folder, "../data", "dailies_data.json"))
user_path = os.path.abspath(os.path.join(current_folder, "../data", "user.json"))

# === Daily Checklist Page ===
def daily_checklist():
  while True:
    exit_to_top = False
    
    user_data = load_json(user_path)
    
    level = user_data["level"]
    tips = user_data["tips"]
    
    divider(2)
    line_breaks(1)
    h1("Dailies")
    line_breaks(1)
    
    h3("Status")
    print(f"Level: {level}")
    print(f"Tips: {tips}")
    line_breaks(2)
    
    # Import data
    dailies = load_json(dailies_data_path)
    
    # Create table
    headers = ["ID"] + list(dailies[0].keys())
    
    status_map = {True: "✓", False: " "}
    difficulty_map = {1: "● ○ ○ ○ ○", 2: "● ● ○ ○ ○", 3: "● ● ● ○ ○", 4: "● ● ● ● ○", 5: "● ● ● ● ●"}
    priority_map = {"low": "🟢", "med": "🟡", "high": "🔴"}
    
    col_widths = []
    for h in headers:
      if h == headers[0]:
        col_widths.append(len(headers[0])+2)
      else:
        max_length = max(len(str(row[h])) for row in dailies)
        col_widths.append(max(len(h), max_length) + 4)
    
    daily_rows = []
    if not dailies:
      print("(No daily tasks currently.)")
    else:      
      for i, row in enumerate(dailies, start=1):
        daily_task_row = f"{str(i)+'.':<{col_widths[0]}}"
        daily_task_row += f"{str(row['Task']):<{col_widths[1]}}"
        daily_task_row += f"{difficulty_map[row['Difficulty']]:<{col_widths[2]}}"
        daily_task_row += f"{priority_map[row['Priority']]:<{col_widths[3]}}"
        daily_task_row += f"{status_map[row['Completed']]:<{col_widths[4]}}"
        
        if row["Completed"]: # Grey completed rows
          daily_task_row = f"\033[90m{daily_task_row}\033[0m"
        
        daily_rows.append(daily_task_row)
    
    max_row_length = max(len(r) for r in daily_rows)
    
    # Column Headers
    print("".join(f"{h:<{w}}" for h, w in zip(headers, col_widths)))
    print("-"*max_row_length) # Dynamic visual divider
    
    # Daily Task List
    for r in daily_rows:
      print(r)    
    line_breaks(2)
    
    # User input line
    choice = input("What would you like to do: \n1 = Create New Task \n2 = Edit Existing Task \n3 = Mark Task Complete \n4 = Delete Task \n('b' to go back to Main Menu)\n>> ").lower().strip()
    
    # Daily Task questions to use in all cases
    create_new_questions = [
      ("Enter task name: ", "task", ()),
      ("Enter difficulty (1-5): ", "difficulty", ("1", "2", "3", "4", "5")),
      ("Enter priority (low, med, high): ", "priority", ("low", "med", "high")),
    ]
    
    # 1. Create New Task
    if choice == "1":
      line_breaks(2)
      h2("Create New Daily Task")
      print("(Type 'b' anytime to go back to previous.)\n")
      
      # Questions and user inputs
      new_task_data = create_new_form(create_new_questions)
      
      new_task = new_task_data["task"]
      new_difficulty = new_task_data["difficulty"]
      new_priority = new_task_data["priority"]

      # Confirm create new task      
      while True:
        line_breaks(1)
        h4("Confirm new daily task:")
        print(f"{'- Task:':<16}{new_task}")
        print(f"{'- Difficulty:':<16}{difficulty_map[new_difficulty]}")
        print(f"{'- Priority:':<16}{priority_map[new_priority]}")
        
        confirm = input("\nSave? (y/n): ").lower().strip()
        
        if not confirm:
          invalid_msg("Input cannot be empty.")
        elif confirm == "n":
          print("\nTask discarded.")
          continue
        elif confirm == "y":
          # Update the JSON file
          dailies.append({"Task": new_task, "Difficulty": new_difficulty, "Priority": new_priority, "Completed": False})
          save_json(dailies_data_path, dailies)
          success_msg("Daily task added successfully!")
          break
        else:
          invalid_msg()
          continue
    
    # 2. Edit Existing Task
    if choice == "2":      
      if not dailies:
        divider()
        line_breaks()
        print("(No Task to edit.)")
        continue
      while True:
        divider()
        line_breaks()
        h2("Edit Daily Task")
        
        options = input(f"\nWhich task do you want to edit? (1-{len(dailies)})\n('b' to go back to Dailies)\n>> ").lower().strip()
         
        if options in {"b", "back"}:
          break
        
        elif not options:
          invalid_msg("Input cannot be empty.")
          continue
          
        elif 1 <= int(options) <= len(dailies):
          daily_task_index = int(options) - 1
          
          while True:
            # Show current task details
            divider()
            h4("Daily Task To Edit:")
            
            d = dailies[daily_task_index]
            data = [
            ("Task", d["Task"]),
            ("Difficulty", difficulty_map[d["Difficulty"]]),
            ("Priority", priority_map[d["Priority"]]),
            ]
            for key, value in data:
              print(f"{'- ' + key +':':<14} {value}")
              
            line_breaks(1)
            divider()
          
            # Edit options
            editable_keys = [key for key, _ in data]
            
            edit_options = "".join(f"\n{i} = {key}" for i, key in enumerate(editable_keys, start=1))
            choice = input(f"\nWhat would you like to edit: {edit_options}\n('b' to choose a different task)\n('e'to exit)\n>> ").lower().strip()
            
            if choice in {"b", "back"}:
              break
            
            elif choice in {"e", "exit"}:
              exit_to_top = True
              break
            
            elif not choice:
              invalid_msg("Input cannot be empty.")
              continue
            
            # Edit daily task name
            elif choice == "1":  
              line_breaks(1)
              while True:
                task_input_data = create_new_form([create_new_questions[0]])
                if not task_input_data:
                  break
                task_input = task_input_data["task"]
                dailies[daily_task_index]["Task"] = task_input
                
                save_json(dailies_data_path, dailies)
                  
                line_breaks(1)
                success_msg("Daily task edited successfully!")
                break
              
            # Edit difficulty
            elif choice == "2":
              line_breaks(1)
              while True:
                difficulty_input_data = create_new_form([create_new_questions[1]])
                if not difficulty_input_data:
                  break
                difficulty_input = difficulty_input_data["difficulty"]
                dailies[daily_task_index]["Difficulty"] = difficulty_input
                
                save_json(dailies_data_path, dailies)
                  
                line_breaks(1)
                success_msg("Difficulty edited successfully!")
                break
              
            # Edit priority
            elif choice == "3":
              line_breaks(1)
              while True:
                priority_input_data = create_new_form([create_new_questions[2]])
                if not priority_input_data:
                  break
                priority_input = priority_input_data["priority"]
                dailies[daily_task_index]["Priority"] = priority_input
                
                save_json(dailies_data_path, dailies)
                  
                line_breaks(1)
                success_msg("Priority edited successfully!")
                break
            
            # # Edit completed
            # elif choice == "4":
            #   line_breaks(1)
            #   while True:
            #     completed_status = dailies[daily_task_index]["Completed"]
            #     status_text = "Completed" if completed_status else "Incomplete"
            #     print(f"Current task status: {status_text}")
            #     line_breaks(1)
                
            #     new_status = "incomplete" if completed_status else "completed"
            #     choice = input(f"Change to {new_status}? (y/n): ").strip().lower()
                
            #     if not choice:
            #       invalid_msg("Input cannot be empty.")
            #     elif choice == "n":
            #       break
            #     elif choice == "y":
            #       dailies[daily_task_index]["Completed"] = not completed_status
            #       save_json(dailies_data_path, dailies)
            #       line_breaks(1)
            #       success_msg("Task status edited successfully!")
            #       break
            #     else:
            #       invalid_msg()
                  
            else:
              invalid_msg()
          if exit_to_top:
            break
        else:
          invalid_msg()
      if exit_to_top:
        continue
    
    # 3. Mark Task Complete
    if choice == "3":   
      if not dailies:
        divider()
        line_breaks()
        print("(No Task to edit.)")
        continue
      while True:
        divider()        
        options = input(f"\nComplete which task? (Task ID)\n('b' to go back to Dailies)\n>> ").lower().strip()
         
        if options in {"b", "back"}:
          break
        
        elif not options:
          invalid_msg("Input cannot be empty.")
          continue
          
        elif 1 <= int(options) <= len(dailies):
          daily_task_index = int(options) - 1
          
          if dailies[daily_task_index]["Completed"] == False:
            task = dailies[daily_task_index]["Task"]
            
            line_breaks(1)
            choice = input(f"Do you want to mark this task as complete? (y/n)\nTask: {task}\n>> ").strip().lower()
            
            if choice == "n":
              break
            elif choice == "y":
              dailies[daily_task_index]["Completed"] = True
              
              save_json(dailies_data_path, dailies)
              
              tip_by_difficulty = {1: 5, 2: 10, 3: 15, 4: 20, 5: 25}
              
              difficulty = dailies[daily_task_index]["Difficulty"]
              tip_amount = tip_by_difficulty.get(difficulty, 0)
              
              if tip_amount:
                increase_tips(tip_amount)
                
                line_breaks(1)
                success_msg("Marked complete!")
                print(f"👍 You got {tip_amount} tips!")
                break
            else:
              invalid_msg()
              continue
          else:
            line_breaks(1)
            print("Task already completed.")
            continue
          
        else:
          invalid_msg()
    
    # 4. Delete Task
    if choice == "4":
      if not dailies:
        divider()
        line_breaks()
        print("(No Task to edit.)")
        continue
      while True:
        divider()        
        options = input(f"\nDelete which task? (1-{len(dailies)})\n('b' to go back to Dailies)\n>> ").lower().strip()
         
        if options in {"b", "back"}:
          break
        
        elif not options:
          invalid_msg("Input cannot be empty.")
          continue
          
        elif 1 <= int(options) <= len(dailies):
          daily_task_index = int(options) - 1
          
          while True:
            divider(1)
            h4("Confirm delete daily task:")

            d = dailies[daily_task_index]
            data = [
            ("Task", d["Task"]),
            ("Difficulty", difficulty_map[d["Difficulty"]]),
            ("Priority", priority_map[d["Priority"]]),
            ("Completed", status_map[d["Completed"]])
            ]
            for key, value in data:
              print(f"{'- ' + key +':':<14} {value}")              
              
            line_breaks(1)
            divider()
            
            choice = input("Delete task? (y/n): ").strip().lower()
            
            if choice == "n":
              break
            
            elif choice == "y":
              removed = dailies.pop(daily_task_index)
          
              save_json(dailies_data_path, dailies)
              success_msg(f"Successfully removed {removed["Task"]}")
              exit_to_top = True
              break
            else:
              invalid_msg()
              continue
          if exit_to_top:
            break
        else:
          invalid_msg()
    if choice == "b":
      return      