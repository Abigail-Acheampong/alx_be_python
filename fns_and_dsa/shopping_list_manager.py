def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to manage the shopping list"""
    shopping_list= []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            #Add on item to the shopping list
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"{item} is added to the shopping list.")
            pass
        
        elif choice == '2':
            #Remove item from the shopping list
            item = input("Enter the item to add: ").strip()
            shopping_list.remove(item)
            print(f"{item} is removed from the shopping list.")
            pass

        elif choice == '3':
            print("The content of the shopping list") 
            print(shopping_list)
            pass

        elif choice == '4':
            print("Goodbye") 
            break
        
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()