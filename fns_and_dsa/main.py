from shopping_list_manager import display_menu

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
        
        elif choice == '2':
            #Remove item from the shopping list
            item = input("Enter the item to add: ").strip()
            shopping_list.remove(item)
            print(f"{item} is removed from the shopping list.")

        elif choice == '3':
            print("The content of the shopping list") 
            print(shopping_list)

        elif choice == '4':
            print("Goodbye") 
            break
        
        else:
            print("Invalid choice. Please try again")

if __name__=="__main__":
    main()