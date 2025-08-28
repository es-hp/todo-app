# === Imports ===
import json, os
from pages import your_cafe, daily_checklist, shop_rewards
from tools import divider, line_breaks, h1, h2, h3, h4, invalid_msg, success_msg, load_json, save_json

# === Data File Paths

current_folder = os.path.dirname(__file__)
user_path = os.path.abspath(os.path.join(current_folder, "data", "user.json"))

# === Start App ===
def start_app():
  divider(2)
  line_breaks(1)
  
  user_data = load_json(user_path)
  
  while True:
    username = input("Enter username: ").strip()
    if not username:
      invalid_msg("Please enter username.")
      continue
    
    # Save username
    user_data["username"] = username
    save_json(user_path, user_data)
    
    main_menu()
    break


# === Main Menu ===
def main_menu():
  
  user_data = load_json(user_path)
    
  username = user_data["username"]
  level = user_data["level"]
  tips = user_data["tips"]

  while True:
    divider(2)
    line_breaks(2)
    h1(f"Welcome to {username}'s cafe.")
    line_breaks(1)

    h3("Status")
    print(f"Level: {level}")
    print(f"Tips: {tips}")
    line_breaks(2)
    
    h3("Menu")
    menu_options = [
      ("1", "Daily Checklist"),
      ("2", "Your Cafe"),
      ("3", "Shop Rewards"),
      ("4", "Exit")
    ]
    for key, option in menu_options:
      print(f"{key} = {option}")
    line_breaks(2)
    
    while True:
      choice = input(f"Choose an option (1-{len(menu_options)}): ")
      
      if choice == "1":
        daily_checklist()
        break
      elif choice == "2":
        your_cafe()
        break
      elif choice == "3":
        shop_rewards()
        break
      elif choice == "4":
        line_breaks(1)
        exit_confirm = input("Are you sure you want to quit? (y/n): ").lower().strip()
        if exit_confirm == "n":
          break
        elif exit_confirm == "y":
          divider(2)
          print("Goodbye!")
          return
        else:
          invalid_msg()
      else:
          invalid_msg()
    



start_app()