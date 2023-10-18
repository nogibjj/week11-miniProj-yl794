import sqlite3
import click

def Create(cursor):
    # Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL
        )
    """)

def Update(cursor):
    cursor.execute("INSERT INTO users (username) VALUES ('Lucy')")
    cursor.execute("INSERT INTO users (username) VALUES ('Alice')")

def Delete(cursor):
    cursor.execute("DELETE from users where username = 'Lucy'")

def Read(cursor):
    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()
    return users

@click.command()
@click.argument("db")
def command_line_tool(db):
    '''
        user guide for this command line tool
    '''
    click.echo("Welcome")
    conn = sqlite3.connect("db")
    cursor = conn.cursor()
    Create(cursor)
    Update(cursor)
    Delete(cursor)
    conn.commit()
    users = Read(cursor)
    for user in users:
        click.echo(user)
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    command_line_tool()
