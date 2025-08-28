# === Imports ===
import os, re
from tools import divider, line_breaks, h1, h2, h3, h4, invalid_msg, success_msg, load_json, save_json, decrease_tips

# === Data File Paths

current_folder = os.path.dirname(__file__)
shop_rewards_path = os.path.abspath(os.path.join(current_folder, "../data", "shop_rewards.json"))
user_path = os.path.abspath(os.path.join(current_folder, "../data", "user.json"))

def shop_rewards():
  while True:
    exit_to_main = False
    exit_to_top = False
        
    user_data = load_json(user_path)
    shop = load_json(shop_rewards_path)
    
    tips = user_data["tips"]
    rewards = user_data["rewards"]
    
    divider(2)
    line_breaks(1)
    h1("Shop Rewards")
    line_breaks(1)
    
    h3("Status")
    print(f"Tips: {tips}")
    line_breaks(1)
    
    divider(1)
    for i, (category, items) in enumerate(shop.items(), start=1):
      print(f"{i}: {category}")
      line_breaks(1)
      for key, item in items.items():
        print(f"{key}: {item['icon'] + ' - ':<4}{item['cost']}")
      line_breaks(2)
    divider(1)
    
    while True:
      choice = input("What would you like to purchase? (ex. 1a, 3b)\n('b' to go back)\n>> ").strip().lower()
      
      formatted = re.fullmatch(r'(\d+)\s*([a-z0-9]+)', choice)
      
      if not choice:
        invalid_msg("Input cannot be empty")
        continue
      if choice in {"b", "back"}:
        exit_to_main = True
        break
      
      if not formatted:
        invalid_msg("Incorrect format.")
        continue
      
      cat_num = int(formatted.group(1))
      item_key = formatted.group(2)
      
      categories = list(shop.keys())
      
      if not (1 <= cat_num <= len(categories)):
        invalid_msg("Category number out of range.")
        continue
      
      cat_name = categories[cat_num - 1]
      
      if item_key not in shop[cat_name]:
        invalid_msg("Item number out of range.")
        continue
      
      while True:
        item_data = shop[cat_name][item_key]
        chosen_item = item_data["icon"]
        item_price = item_data["cost"]
        
        divider(1)
        answer = input(f"Purchase {chosen_item} for {item_price} tips? (y/n): ").strip().lower()
        
        if not answer:
          invalid_msg("Input cannot be empty.")
          continue
        elif answer == "n":
          exit_to_top = True
          break
        elif answer == "y":
          if tips < item_price:
            invalid_msg("Sorry, not enough tips.")
            exit_to_top = True
            break
          else:            
            rewards[cat_name.lower()].append(chosen_item)
            save_json(user_path, user_data)
            
            decrease_tips(item_price)
            
            divider(1)
            success_msg(f"{chosen_item} was added to your shop!")
            divider(1)
            
            exit_to_top = True
            break
        else:
          invalid_msg()
          continue
        
      if exit_to_top:
        break
    if exit_to_main:
      break

      