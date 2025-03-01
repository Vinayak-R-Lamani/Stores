import mysql.connector 

from db_connection import conn , cursor


class Store:
    def __init__(self, cursor):
        self.cursor = cursor
    
    def get_all_stores(self):
        table_name = "hi"
        self.cursor.execute("show tables")
        tables = [table[0] for table in self.cursor.fetchall()]
        for i,table in enumerate(tables):
            table = table.replace("_", " ").title()
            print(f"{i+1}  {table}")
            
        print("Select a Store to fill the data")
        store_id = int(input("Enter the store id: "))
        
        for i in range(len(tables)):
                table_name = tables[store_id - 1]
        return table_name
    
    
    def insert_data(self, table):
        cid = int(input("Enter the customer id: "))
        name = input("Enter the customer name: ")
        items_bought = input("Enter the items bought: ")
        price = float(input("Enter the price: "))
        purchase_time = input("Enter the purchase time(HH:MI:SS):  ")
        purchase_date = input("Enter the purchase date(YYYY-MM-DD):")
        
        sql = f"""
        INSERT INTO {table} (cid, customer_name, items_bought, price, purchase_time, purchase_date)
        VALUES ({cid}, '{name}', '{items_bought}', {price}, '{purchase_time}', '{purchase_date}');
        """
        cursor.execute(sql)
        conn.commit()
        print("Data inserted successfully")
        
    def print_all_data(self, table):
        sql = f"SELECT * FROM {table}"
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            print(row)

    
def main():
    store = Store(cursor)  
    print("Welcome to the store data filling system")
    option = input("Please select the option: \n1. Fill data\n2. View data\n")
    if option == "2":
        table = store.get_all_stores()
        store.print_all_data(table)
    if option == "1":
        continue_procedure_data_fill = True
        while continue_procedure_data_fill:
            continue_procedure = True

            while continue_procedure:
                table = store.get_all_stores()  
                print(f"You selected {table}")
                
                store.insert_data(table) 
                
                user_input = input("Do you want to continue? (y/n): ").strip().lower()
                if user_input != "y":
                    continue_procedure = False
            user_input = input("Do you want to continue filling data for other stores? (y/n): ").strip().lower()
            if user_input != "y":
                continue_procedure_data_fill = False
                
        else:
            print("Thank you for using the system")
if __name__ == "__main__":
    main()
    
