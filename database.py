from sqlalchemy import create_engine, text


engine = create_engine(
    DB_CONN,
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    })

def all_movies_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM movies"))
    return result.all()

print(all_movies_from_db())

if __name__ == "__main__":
    print("Hello, World!")
