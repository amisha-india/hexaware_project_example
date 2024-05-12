import pyodbc

server_name = "Amarjeet\SQLEXPRESS"
database_name = "HexawareMoviesDB"
 
 
conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

print("Welcome to the movies app")
print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()  
cursor.execute("Select 1")
print("Database connection is successful 🎊")
 
class MovieServies:
    def read_movies():
        cursor.execute("Select * from Movies")
    # movies = cursor.fetchall() # Get all data
    # for movie in movies:
    #     print(movie)
 
    # Get data one row at a time
    for row in cursor:
        print(row)
    for row in cursor:
        print(row)
    
# Task 1
# Get the data from the user
# Clue: Use arguments
def create_movie(title, year, director_id):
    cursor.execute(
        "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
        # ("Oppenheimer", 2023, 1),
        (title, year, director_id)
    )
    # conn.commit()  # Permanent storing | If no commit then no data
if __name__ == "__main__":
    title=input("Enter movie title: ")
    year=input("enter the year: ")
    director_id=input("Enter the director Id:")
    MovieServies.create_movie(title, year, director_id)
    MovieServies.read_movies()
 
# Task 2
# Delete a movie from the db by getting the id from user
# Task 2
# Delete a movie from the db by getting the id from user
def delete_movie(id):
    cursor.execute("DELETE FROM Movies WHERE MovieId = ?", (id,))
    conn.commit()
    print("Movie deleted successfully.")
#Task 4 updation 
def update_movie(id):
    cursor.execute("UPDATE FROM Movies SET title = ? , year=?,director_id=? WHERE MovieId = ?", (title,year,director_id,id),)
    conn.commit()
    print("Movie updated successfully.")

 
if __name__ == "__main__":
    while True:#task 5 put in loop
        print("1. Create a movie")
        print("2. Delete a movie")
        print("3. Read movies")
        print("4.Udate movies")
        print("5. Exit")
        choice = input("Enter your choice: ")
#task3 
        if choice == "1":
            name = input("Enter the movie name: ")
            year = int(input("Enter the year: "))
            director_id = int(input("Enter the director ID: "))
            create_movie(name, year, director_id)
        elif choice == "2":
            MovieId = int(input("Enter the MovieId: "))
            delete_movie(MovieId)
        elif choice == "3":
            MovieServies.read_movies()
        elif choice == "4":
            MovieServies.read_movies()
            MovieId = int(input("Enter the MovieId"))
            title = input("Enter the movie title to change: ")
            year = int(input("Enter the movie year to change: "))
            director_id = int(input("Enter the movie director_id to change: "))
            MovieServies.update_movie(MovieId,title,year,director_id)
        else:
            print("Invalid choice. Please enter a valid option.")
            break
    MovieServies= MovieServies()