from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.orm import declarative_base, sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
# class Programmer(base):
#     __tablename__ = "Programmer"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     gender = Column(String)
#     nationality = Column(String)
#     famous_for = Column(String)

# create a class-based model for the "Games" table
class Games(base):
    __tablename__ = "Games"
    id = Column(Integer, primary_key=True)
    game_name = Column(String)
    release_year = Column(Integer)
    console_name = Column(String)
    category = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Programmer table
# ada_lovelace = Programmer(
#     first_name = "Ada",
#     last_name = "Lovelace",
#     gender = "F",
#     nationality = "British",
#     famous_for = "First Programmer" 
# )

# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="M",
#     nationality="British",
#     famous_for="Modern Computing"
# )

# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="F",
#     nationality="American",
#     famous_for="COBOL language"
# )

# margaret_hamilton = Programmer(
#     first_name="Margaret",
#     last_name="Hamilton",
#     gender="F",
#     nationality="American",
#     famous_for="Apollo 11"
# )

# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="M",
#     nationality="American",
#     famous_for="Microsoft"
# )

# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="M",
#     nationality="British",
#     famous_for="World Wide Web"
# )

# daniel_harris = Programmer(
#     first_name="Daniel",
#     last_name="Harris",
#     gender="M",
#     nationality="British",
#     famous_for="Beginner Coder"
# )

# creating records for our Games table
call_of_duty = Games(
    game_name = "Call of Duty 4",
    release_year = "2007",
    console_name = "Microsoft Xbox 360",
    category = "Shooter"
)

fifa = Games(
    game_name = "Fifa 2019",
    release_year = "2018",
    console_name = "Microsoft Xbox One",
    category = "Sports"
)

gears_of_war = Games(
    game_name = "Gears of War 2",
    release_year = "2008",
    console_name = "Microsoft Xbox 360",
    category = "Shooter"
)

mario_kart = Games(
    game_name = "Mario Kart Double Dash",
    release_year = "2003",
    console_name = "Nintendo Gamecube",
    category = "Racing"    
)

pokemon = Games(
    game_name = "Pokemon Gold",
    release_year = "1999",
    console_name = "Nintendo Gameboy Color",
    category = "RPG" 
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(daniel_harris)

# add each instance of our games to our session
session.add(call_of_duty)
session.add(fifa)
session.add(gears_of_war)
session.add(mario_kart)
session.add(pokemon)

# updating a single record
# programmer = session.query(Programmer).filter_by(id=8).first()
# programmer.famous_for = "World President"

# commit our session to the database
session.commit()

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
# uniqueid = input("Enter a id: ")
# programmer = session.query(Programmer).filter_by(id=uniqueid).first()
# defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.id)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

# query the database to find all Programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )

# query the database to find all Games
games = session.query(Games)
for game in games:
    print(
        game.id,
        game.game_name,
        game.release_year,
        game.console_name,
        game.category,
        sep=" | "
    )