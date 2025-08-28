from tools.ui_format import invalid_msg

def create_new_form(questions):
  # questions = [ (prompt, key, conditions, completed) ]
  inputs = {}
  current_question = 0

  while current_question < len(questions):
    prompt, key, conditions = questions[current_question]
    user_input = input(prompt).strip()

    if user_input.lower() in {"b", "back"}:
      if current_question == 0:
        return None
      else:
        current_question -= 1  # Move back one step
      continue

    if not user_input:
      invalid_msg("Input cannot be empty.")
      continue
      
    if conditions and user_input.lower() not in conditions:
      invalid_msg("Valid input necessary.")
      continue
    
    if key == "difficulty":
      inputs[key] = int(user_input)
    elif key == "priority":
      inputs[key] = user_input.lower()
    else:    
      inputs[key] = user_input
      
    current_question += 1  # Move forward

  return inputs