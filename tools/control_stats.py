# === Imports ===
import os
from tools import load_json, save_json

# === Data File Paths

current_folder = os.path.dirname(__file__)
user_path = os.path.abspath(os.path.join(current_folder, "../data", "user.json"))

# === Functions ===

def increase_level(xp):
  user_data = load_json(user_path)
  current_level = int(user_data.get("level", 0))
  new_level = current_level + int(xp)
  user_data["level"] = new_level
  save_json(user_path, user_data)
  return new_level

def increase_tips(tips):
  user_data = load_json(user_path)
  current_tips = int(user_data.get("tips", 0))
  new_tips = max(0, current_tips + int(tips))
  user_data["tips"] = new_tips
  save_json(user_path, user_data)
  return new_tips

def decrease_tips(tips):
  user_data = load_json(user_path)
  current_tips = int(user_data.get("tips", 0))
  new_tips = max(0, current_tips - int(tips))
  user_data["tips"] = new_tips
  save_json(user_path, user_data)
  return new_tips