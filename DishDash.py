import tkinter as tk
from tkinter import messagebox

recipes = [
    {
            "name": "Adobo", 
            "ingredients": ["chicken", "soy sauce", "vinegar", "garlic", "bay leaf"], 
            "instructions": "\n1. Combine chicken, soy sauce, vinegar, garlic, and bay leaves in a bowl. Let it marinate for at least 30 minutes.\n2. In a pan, add the marinated chicken and bring to a boil. Reduce the heat and simmer for 30–40 minutes until the chicken is tender.\n3.Increase heat to reduce the sauce until thickened. Adjust seasoning, then serve hot."},
        {
            "name": "Menudo", 
            "ingredients": ["pork", "tomato sauce", "onion"], 
            "instructions": "\n1.Combine pork, tomato sauce, and chopped onion in a pot. Cook over medium heat for about 5 minutes.\n2.Add water to cover the pork, bring to a boil, then lower the heat and simmer for 45 minutes or until the pork is tender.\n3.Season with salt and pepper to taste, then serve hot.\n"},
        {
            "name": "Sisig",
            "ingredients": ["pork face", "onion", "chili", "mayonnaise", "calamansi"],
            "instructions": "\n1.Boil pork face until tender, then chop into small pieces and set aside.\n2.In a pan, sauté chopped onion and chili until softened, then add the pork and cook for a few minutes.\n3.Mix in mayonnaise and squeeze in calamansi juice, then serve hot.\n"
        },
        {
            "name": "Sinigang",
            "ingredients": ["pork", "sinigang mix", "tomato", "onion", "sitaw", "kangkong"],
            "instructions": "(Sitaw is optional)\n1.Boil pork with water, tomatoes, and onions until the pork is tender.\n2.Add the sinigang mix, sitaw, and simmer for a few more minutes.\n3.Add kangkong, cook for another minute, then season to taste and serve hot.\n"
        },
        {
            "name": "Chicken Fillet",
            "ingredients": ["chicken breast", "bread crumbs", "egg", "flour", "salt", "pepper"],
            "instructions": "\n1.Coat chicken breast in flour, dip in beaten egg, then coat with bread crumbs.\n2.Season with salt and pepper, then heat oil in a pan and fry the chicken until golden brown and cooked through.\n3.Drain excess oil, then serve hot."
        },
         {
        "name": "Fried Chicken",
        "ingredients": ["chicken", "flour", "egg", "bread crumbs", "seasoning"],
        "instructions": "\n1. Coat chicken in flour, dip in beaten egg, then coat with bread crumbs.\n2. Season with your choice of seasoning, then heat oil in a pan and fry the chicken until golden and crispy.\n3. Drain excess oil, then serve hot."
        },
        
        {
            "name": "Fried Rice",
            "ingredients": ["cooked rice", "garlic", "soy sauce", "egg", "vegetables"],
            "instructions": "\n1.Sauté garlic in a pan until fragrant, then add cooked rice and stir-fry. \n2.Push rice to one side, scramble an egg in the pan, then mix with rice.\n3.Add soy sauce and vegetables, cook for a few more minutes, then serve hot."
        },
        {
            "name": "Corned Beef",
            "ingredients": ["canned corned beef", "onion", "potato", "oil"],
            "instructions": "\n1.Sauté onion in oil until softened, then add cubed potatoes and cook until tender.\n2.Add canned corned beef and cook, stirring occasionally, until heated through.\n3.Serve hot."
        },
        {
            "name": "Chop Suey",
            "ingredients": ["mixed vegetables", "chicken or pork", "soy sauce", "oyster sauce", "garlic", "onion"],
            "instructions": "\n1.Sauté garlic and onion in oil, then add chicken or pork and cook until browned.\n2.Add mixed vegetables, soy sauce, and oyster sauce, then stir-fry until tender.\n3.Serve hot."
        },
        {
            "name": "Adobong Sitaw",
            "ingredients": ["string beans", "soy sauce", "vinegar", "garlic", "pork"],
            "instructions": "\n1.Sauté garlic and pork in oil, then add soy sauce and vinegar. Simmer for a few minutes.\n2.Add string beans and cook until tender, then serve hot."
        },
        {
            "name": "Egg Omelet",
            "ingredients": ["egg", "onion", "tomato", "salt", "pepper"],
            "instructions": " \n1.Whisk eggs with salt and pepper, then sauté onion and tomato in oil until soft.\n2.Pour in the eggs and cook until set, then fold and serve hot.\n"
        }
]

# Functions

def search_recipes():
    search_term = search_entry.get().lower()
    results_text.config(state=tk.NORMAL)  # Enables tne editing to modify text widget
    results_text.delete(1.0, tk.END)  # ends
    results = [
        recipe for recipe in recipes
        if search_term in recipe["name"].lower() or search_term in str(recipe["ingredients"]).lower()
    ]
    if results:
        for recipe in results:
            results_text.insert(tk.END, f"Name: {recipe['name']}\n")
            results_text.insert(tk.END, f"Ingredients: {', '.join(recipe['ingredients'])}\n")
            results_text.insert(tk.END, f"Instructions: {recipe['instructions']}\n\n")
    else:
        messagebox.showinfo("No Results", "No recipe  or ingridient was found")
    results_text.config(state=tk.DISABLED)  # so the text widget cannot be editeddd

def add_recipe():
    name = name_entry.get().strip()
    ingredients = ingredients_entry.get().strip().split(",")
    instructions = instructions_entry.get().strip()
    
    if not name or not ingredients or not instructions:
        messagebox.showerror("Error!!!!", "All fields are required!")
        return
    
    recipes.append({"name": name, "ingredients": ingredients, "instructions": instructions})
    messagebox.showinfo("Success", f"Recipe '{name}' added successfully!")
    clear_entries()

def view_all_recipes():
    results_text.config(state=tk.NORMAL)  # Enable editing to modify text widget
    results_text.delete(1.0, tk.END)  # endds
    for recipe in recipes:
        results_text.insert(tk.END, f"Name: {recipe['name']}\n")
        results_text.insert(tk.END, f"Ingredients: {', '.join(recipe['ingredients'])}\n")
        results_text.insert(tk.END, f"Instructions: {recipe['instructions']}\n\n")
    results_text.config(state=tk.DISABLED)  # so the text widge cannot be edited (2)

def clear_entries():
    name_entry.delete(0, tk.END)
    ingredients_entry.delete(0, tk.END)
    instructions_entry.delete(0, tk.END)


# GUI setup
root = tk.Tk()
root.title("DishDash - Digital Kitchen Assistant (brat)")
root.geometry("900x700")
root.configure(bg="#39FF14")  # BRAT inspired background

# Styles
title_font = ("Arial", 18, "bold")
label_font = ("Arial", 12)
button_font = ("Arial", 10, "bold")

# Title
title_label = tk.Label(root, text="DishDash - Digital Kitchen Assistant (brat)", font=title_font, bg="#39FF14", fg="#333")
title_label.pack(pady=10)

# Frames      
main_frame = tk.Frame(root, bg="#39FF14")   

main_frame.pack(expand=True, fill="both")

search_frame = tk.Frame(main_frame, bg="#f5f5f5", bd=2, relief=tk.SOLID, padx=10, pady=10)
search_frame.pack(pady=10)

add_frame = tk.Frame(main_frame, bg="#f5f5f5", bd=2, relief=tk.SOLID, padx=10, pady=10)
add_frame.pack(pady=10)

result_frame = tk.Frame(main_frame, bg="#f5f5f5", bd=2, relief=tk.SOLID, padx=10, pady=10)
result_frame.pack(pady=10)

# Search Recipe Section
tk.Label(search_frame, text="Search Recipe", font=label_font, bg="#f5f5f5", fg="#555").grid(row=0, column=0, columnspan=2)
tk.Label(search_frame, text="Search (Recipe or Ingredients): ", font=label_font, bg="#f5f5f5").grid(row=1, column=0, sticky=tk.W)
search_entry = tk.Entry(search_frame, width=30)
search_entry.grid(row=1, column=1, pady=5)

tk.Button(search_frame, text="Search", font=button_font, bg="#2196F3", fg="white", command=search_recipes).grid(row=2, column=0, pady=5)
tk.Button(
    search_frame, 
    text="View All Recipes", 
    font=button_font, 
    bg="#FF5722", 
    fg="white", 
    command=view_all_recipes
).grid(row=2, column=1, pady=5)


# Add Recipe Section
tk.Label(add_frame, text="Add Recipe", font=label_font, bg="#f5f5f5", fg="#555").grid(row=0, column=0, columnspan=2)
tk.Label(add_frame, text="Name:", font=label_font, bg="#f5f5f5").grid(row=1, column=0, sticky=tk.W)
name_entry = tk.Entry(add_frame, width=30)
name_entry.grid(row=1, column=1, pady=5)

tk.Label(add_frame, text="Ingredients:", font=label_font, bg="#f5f5f5").grid(row=2, column=0, sticky=tk.W)
ingredients_entry = tk.Entry(add_frame, width=30)
ingredients_entry.grid(row=2, column=1, pady=5)

tk.Label(add_frame, text="Instructions:", font=label_font, bg="#f5f5f5").grid(row=3, column=0, sticky=tk.W)
instructions_entry = tk.Entry(add_frame, width=30)
instructions_entry.grid(row=3, column=1, pady=5)

tk.Button(add_frame, text="Add Recipe", font=button_font, bg="#4CAF50", fg="white", command=add_recipe).grid(row=4, column=0, columnspan=2, pady=5)


# Text widget for displaying recipes
results_text = tk.Text(result_frame, width=80, height=15)
results_text.pack(padx=10, pady=10)
results_text.config(state=tk.DISABLED)

# Run the GUI
root.mainloop()
        