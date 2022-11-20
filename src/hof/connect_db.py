def connect(server):
    print("Connect: " + server)
    def query(sql):
        print(sql) # run somthing...
        return
    return query

if __name__ == "__main__":
    query = connect("mysql://host:3306")
    users = query("SELECT ID FROM USER;")
    query("UPDATE USER SET NAME='Alice' WHERE ID=1;")

    query = connect("postgresql://user@host")
    users = query("SELECT ID FROM USER;")
