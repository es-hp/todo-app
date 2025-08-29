# Coding Temple SE Assignment: Todo App [Helen Park]

To create a todo list using Python where user can add, view, delete tasks and quit the application.

## main.py

A cafe themed, gamified todo list app. User is a cafe 'owner' and earns 'tips' (in-app currency) by completing tasks. 'Tips' can be used to buy rewards to decorate and run the 'cafe'.

### start_app()

- User can enter a user name. (NOT a login/authentication page)
  - Saves user name to user.json file.

### main_menu()

- Loads user data from user.json.

  - Shows username, and stats such as level and tips (in-app currency)

- Menu gives option to open different pages (Daily Checklist, Your Cafe, Shop Rewards, Exit)

## tools

### control_stats.py

- Created custom functions for increasing level, increasing tips, and decreasing tips to be used on app pages.

### create_new_form.py

- Created a dynamic custom input generator where a list of tuples can be passed into it.
- Input validation and error handling for specific types of questions in place.
- Allows user to go back to the previous question when they input 'b' or 'back', unless it is the first question.

### file_utilities.py

- Created separate functions for opening/loading json files, and writing to json files.
  - Allows emojis to be used.

### ui_format.py

- Created custom UI components like dynamic dividers, line breaks, heading types, a generic but customizable invalid and success messages.

## pages

### daily_checklist.py

- Imports data from json file using absolute path created using os.
- Created a table with dynamic headers based on the keys from the json data.
  - Mapped task status, difficulty, and priority information to more visually clear strings that use emojis and special characters.
  - Table column widths are dynamically set based on the max length (plus 4 padding) of the content or the header, whichever is greater.
  - Completed tasks change to grey font color
- User can choose what to do from menu

- Create New Task: Uses the create_new_form and the create_new_questions list to ask user to input new task information (task, difficulty, priority).

  - Asks to confirm save, and writes changes back to json file.

- Edit Existing Task: User can choose which part of the task they would like to edit from an existing task.
- If no tasks exists, it shows a "No task to edit." message and brings you back to checklist.
- User can input the ID of which task they'd like to edit. It shows the user how many tasks there are dynamically. Number increases and decreases with how many tasks have been added/removed.
- If the user input matches the ID of an existing task, it will prompt user which part they'd like to edit.
- After editing one part, user can continue to edit the same task, or exit back to checklist.

- Mark Task Complete: User has a simple way to mark a task complete which will change "Completed" to true, adding a checkmark in the table's completed column, and making the text for that task grey.
- When a user marks a task complete, they automatically get "tips" (in-app currency).

  - The amount they receieve is based on the difficulty of the task. The amount of points is dynamically updated based on the mapping.

- Delete Task: User can choose a task to remove by ID.
  - UI will show the task and task data before user confirms delete.
  - Task removed using .pop() and saving update to json file.

### your_cafe.py

- Shows the cafe's employees, menu items, and furniture, which are rewards that can be bought with 'tips'.

### shop_rewards.py

- Data of reward items from shop_rewards.json file are loaded in to be used on page.
- Items are listed by category, which are numbered, and each item has an alphabet key.
- Users can choose which item they want to purchase by inputing the category ID and item key.
  - re.fullmatch() will compare the user input with the pattern to see if it matches. If it doesn't match the pattern the user gets an invalid message.
  - If it matches, it will then see if the first part of the pattern, the ID, matches the ID of any of the categories. If it doesn't match (ex. user inputs 5 when there are only 4 categories) then user will get an invalid message.
  - If it matches, it will then see if the second part of the pattern, the item key, matches the key of an item in the chosen category. If it doesn't match any key, it will show an invalid message.
  - Once it meets all requirements, it will show the item and cost of item for purchase confirmation.
- When user confirms purchase:
  - First, it will see if there are enough 'tips' to follow through with purchase, show a message, and exit to the top of the page.
    - If there aren't enough 'tips', it will show an error.
  - If there are, it will add that item (string/emoji) to the user.json where all rewards are stored.
  - This will update what shows on your_cafe.py.
  - It will then subtract the cost from user's 'tips' and update the user.json file again.
  - A success message will show and return user back to the top of the page with updated stats showing.
