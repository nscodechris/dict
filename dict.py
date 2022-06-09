import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="dict",
   user="postgres",
   password="Cvmillan10!?"
)

def read_dict(conn):
    # returns a list of all the words in dict
    #
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_word(conn, word, translation):
    # adding words to the dict
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(conn, ID):
    # delete words from dict
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(conn):
    # saving the changes thas has been done
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close()

def main():
    while True: ## REPL - Read Execute Program Loop
        print("Welcome")
        print("Commands: \n--list\n--add\n--delete\n--quit!")
        cmd = input("Command: ")
        if cmd == "list":
            for i, wd, trans in read_dict(conn):
                print(f"{i}: {wd} - {trans}")
        elif cmd == "add":
            name = input("  Word: ")
            phone = input("  Translation: ")
            add_word(conn, name, phone)
        elif cmd == "delete":
            ID = input("  ID: ")
            delete_word(conn, ID)
        elif cmd == "quit":
            save_dict(conn)
            exit()


main()

