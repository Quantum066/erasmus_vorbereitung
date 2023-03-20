import sqlite3

# Connect
database = sqlite3.connect("vertretungsplan.db")

# Create a cursor
cursor = database.cursor()

# Create a table
cursor.execute("""
    create table stundenplan 
    (
	    Wochentag				varchar(2),
        Stunde					int unsigned not null,
        StundeRot				int unsigned not null,
    
        Primary Key (StundeRot)
    )
    """)

cursor.execute("""
    create table stunde
    (
	    Klasse				int unsigned not null,
        LehrerID			int unsigned not null,
        Teil				char not null,
        Raum				int unsigned not null,
        Fach				varchar(15) not null,
    
        primary key	(Raum)
    )
    """)

cursor.execute("""
    create table lehrer
    (
	    LehrerID			int unsigned not null auto_increment,
        LehrerName			varchar(50) not null,
        VertretungsStunde	int unsigned not null,
    
        primary key (LehrerID)
    )
    """)

cursor.execute("""
    create table klasse
    (
	    SchuelerZahl			int unsigned not null,
        KlassenLeiter			int unsigned not null,
        SecondKlassenLeiter		int unsigned not null,
        Zimmer					int unsigned not null,
    
        primary key (Zimmer),
        foreign key (KlassenLeiter) lehrer(LehrerID),
        foreign key (SecondKlassenleiter) lehrer(LehrerID)
    )
    """)

cursor.execute("""
    create table fachzulehrer
    (
	    LehrerID				int unsigned not null, 
        Fach					varchar(15),
    
        foreign key (LehrerID) lehrer(LehrerID)
    )
    """)

# commit the command
database.commit()

# close connection
database.close()