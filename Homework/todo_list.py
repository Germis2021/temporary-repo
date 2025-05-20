#In the lecture you have seen a person_database.py

#Please write a similar application, 
#which would allow to add todos.
#Todo can have description and a date.
#After each addition it would print all todos.


todo_list = []

while True :

        description = input("Ivesk uzduoties pavadinima ")
        description_date = input("Ivesk uzduoties data (Year, month, day): ")
    

        description = {
            'description': description,
            'description_date': description_date,
            
        }

        todo_list.append(description)
        
        
        for p in todo_list:

            print("uzduociu sarasas")
            
            print(f" description: {p['description']}, iki: description_date: {p['description_date']}")

        

    