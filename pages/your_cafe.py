# === Imports ===
import os
from pages.shop_rewards import shop_rewards
from tools import divider, line_breaks, h1, h2, h3, h4, invalid_msg, load_json

# === Data File Paths

current_folder = os.path.dirname(__file__)
dailies_data_path = os.path.abspath(os.path.join(current_folder, "../data", "dailies_data.json"))
user_path = os.path.abspath(os.path.join(current_folder, "../data", "user.json"))

def your_cafe():
  while True:
    user_data = load_json(user_path)
    
    tips = user_data["tips"]
    rewards = user_data["rewards"]
    
    divider(2)
    line_breaks(1)
    h1("Your Cafe")
    line_breaks(1)
    
    h3("Status")
    print(f"Tips: {tips}")
    line_breaks(1)
    
    employees = rewards.get("employees", [])
    drinks = rewards.get("drinks", [])
    food = rewards.get("food", [])
    furniture = rewards.get("furniture", [])
    
    divider(1)
    print(f"Employees: {' '.join(employees)}")
    line_breaks(1)
    print(f"Drinks: {' '.join(drinks)}")
    line_breaks(1)
    print(f"Food: {' '.join(food)}")
    line_breaks(1)
    print(f"Furniture: {' '.join(furniture)}")
    divider(1)
    
    choice = input("What would you like to do?"
                  "\n1 = Refresh"
                  "\n2 = Go to Shop"
                  "\n('b' to go back to Main Menu)"
                  "\n>> ").strip().lower()
    
    if choice == "b":
      return
    
    # 1. Refresh
    elif choice == "1":
      continue
    
    # # 2. Remove
    # elif choice == "2":
    #   line_breaks(1)
    #   divider()
    #   line_breaks(1)
    #   choice = input("Remove from which category?"
    #         "\n1 = Employees"
    #         "\n2 = Drinks"
    #         "\n3 = Food"
    #         "\n4 = Furniture"
    #         "('b' to go back)"
    #         ">> ")
    #   if choice == "b":
    #     continue
    #   elif choice == "1":
    #     while True:
    #       line_breaks(2)
    #       print(f"Employees: {' '.join(f'{i} = {e}' for i, e in enumerate(employees, 1))}")
    #       line_breaks(1)
    #       choice = input(f"Remove which employee? (1-{len(employees)}): ")
          
    #       if not choice:
    #         invalid_msg("Input cannot be empty.")
    #         continue
    #       elif choice in {"b", "back"}:
    #         break
    #       elif 1 <= int(choice) <= len(employees):
    #         index = int(choice) - 1
    #         employees.pop(index)
    #         break
    #       else:
    #         invalid_msg()
    #         divider(1)
    #   else:
    #     invalid_msg()
    
    # 2. Go to Shop
    elif choice == "2":
      shop_rewards()
      break
    
    else:
      invalid_msg()
      continue
