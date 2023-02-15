CREATE DATABASE library;
USE library;

/*Creating member relation*/
CREATE TABLE IF NOT EXISTS Member( 
	ID			VARCHAR(10)		NOT NULL,
    name		VARCHAR(100)	NOT NULL,
    faculty 	VARCHAR(50)		NOT NULL,
    phoneNo		VARCHAR(15)		NOT NULL,
    email		VARCHAR(100)	NOT NULL,
    PRIMARY KEY (ID));
    
/*Creating book relation*/
CREATE TABLE IF NOT EXISTS Book(
	accessionNo	VARCHAR(16)		NOT NULL,
    title		VARCHAR(100)	NOT NULL,
    isbn		CHAR(13)		NOT NULL,
    publisher	VARCHAR(100),
    pubDate		YEAR,
    PRIMARY KEY (accessionNo));
    
/*Creating loan relation*/
CREATE TABLE IF NOT EXISTS Loan(
	accessionNo	VARCHAR(16)		NOT NULL,
    borrowDate 	DATE			NOT NULL,
    dueDate		DATE			NOT NULL,
    memberID	VARCHAR(10)		NOT NULL,
    PRIMARY KEY	(accessionNo, memberID),
    FOREIGN KEY (accessionNo) REFERENCES Book(accessionNo) ON DELETE CASCADE
														   ON UPDATE CASCADE,
	FOREIGN KEY (memberID) REFERENCES Member(ID) ON DELETE CASCADE
												 ON UPDATE CASCADE);

/*Creating reservation relation*/
CREATE TABLE IF NOT EXISTS Reservation(
	accessionNo VARCHAR(16)		NOT NULL,
    reserveDate	DATE 			NOT NULL,
	memberID	VARCHAR(10)		NOT NULL,
    PRIMARY KEY	(accessionNo, memberID),
    FOREIGN KEY (accessionNo) REFERENCES Book(accessionNo) ON DELETE CASCADE
														   ON UPDATE CASCADE,
	FOREIGN KEY (memberID) REFERENCES Member(ID) ON DELETE CASCADE
												 ON UPDATE CASCADE);

/*Creating returns relation*/
CREATE TABLE IF NOT EXISTS returns(
	returnDate  date			NOT NULL,
    accessionNo VARCHAR(16)		NOT NULL,
    memberID	VARCHAR(10)		NOT NULL,
    PRIMARY KEY (accessionNo, memberID));

/*Creating fine relation*/
CREATE TABLE IF NOT EXISTS Fine(
	paymentDate DATE 			NOT NULL,
    amount 		INT 			NOT NULL,
    memberID	VARCHAR(10)		NOT NULL,
    PRIMARY KEY (memberID), 
	FOREIGN KEY (memberID) REFERENCES Member(ID) ON DELETE CASCADE
												 ON UPDATE CASCADE);

/*Creating authors relation*/
CREATE TABLE IF NOT EXISTS Authors(
	 accessionNo VARCHAR(16)		NOT NULL,
     author 	 VARCHAR(100) 		NOT NULL,
     PRIMARY KEY (accessionNo),
     FOREIGN KEY (accessionNo) REFERENCES Book(accessionNo) ON DELETE CASCADE
														    ON UPDATE CASCADE);
								
/* Initialising database with the 9 members into the member relation */
INSERT IGNORE INTO Member(ID, name, faculty, phoneNo, email) VALUES

("A101A","Hermione Granger","Science",33336663,"flying@als.edu"),
("A201B","Sherlock Holmes","Law",44327676,"elementarydrw@als.edu"),
("A301C","Tintin","Engineering",14358788,"luvmilu@als.edu"),
("A401D","Prinche Hamlet","FASS",16091609,"tobeornot@als.edu"),
("A5101E","Willy Wonka","FASS",19701970,"choco1@als.edu"),
("A601F","Holly Golightly","Business",55548008,"diamond@als.edu"),
("A701G","Raskolnikov","Law",18661866,"oneaxe@als.edu"),
("A801H","Patrick Bateman","Business",38548544,"mice@als.edu"),
("A901I","Captain Ahab","Science",18511851,"wwhale@als.edu");

/* Initialising database with the 50 books into the book relation */
INSERT IGNORE INTO Book(accessionNo, title, isbn, publisher, pubDate) VALUES

("A01","A 1984 Story",9790000000001,"Intra S.r.l.s.","2021"),
("A02","100 anos de soledad",9790000000002,"Vintage Espanol","2017"),
("A03","Brave New World",9790000000003,"Harper Perennial","2006"),
("A04","Crime and Punishment",9790000000004,"Penguin","2002"),
("A05","The Lion, The Witch and The Wardrobe",9790000000005,"Harper Collins","2002"),
("A06","Frankenstein",9790000000006,"Reader's Library Classics","2021"),
("A07","The Grapes of Wrath",9790000000007,"Penguin Classics","2006"),
("A08","The Adventures of Huckleberry Finn",9790000000008,"SeaWolf Press","2021"),
("A09","Great Expectations",9790000000009,"Penguin Classics","2002"),
("A10","Catch-22",9790000000010,"Simon & Schuster","2011"),
("A11","The Iliad",9790000000011,"Penguin Classics","1998"),
("A12","Les Miserables",9790000000012,"Signet","2013"),
("A13","Ulysses",9790000000013,"Vintage","1990"),
("A14","Lolita",9790000000014,"Vintage","1989"),
("A15","Atlas Shrugged",9790000000015,"Dutton","2005"),
("A16","Perfume",9790000000016,"Vintage","2001"),
("A17","The Metamorphosis",9790000000017,"12th Media Services","2017"),
("A18","American Psycho",9790000000018,"ROBERT LAFFONT","2019"),
("A19","Asterix the Gaul",9790000000019,"Papercutz","2020"),
("A20","Fahrenheit 451",9790000000020,"Simon & Schuster","2012"),
("A21","Foundation",9790000000021,"Bantam Spectra Books","1991"),
("A22","The Communist Manifesto",9790000000022,"Penguin Classics","2002"),
("A23","Rights of Man, Common Sense, and Other Political Writings",9790000000023,"Oxford University Press","2009"),
("A24","The Prince",9790000000024,"Independently published","2019"),
("A25","The Wealth of Nations",9790000000025,"Royal Classics","2021"),
("A26","Don Quijote",9790000000026,"Ecco","2005"),
("A27","The Second Sex",9790000000027,"Vintage","2011"),
("A28","Critique of Pure Reason",9790000000028,"Cambridge University Press","1999"),
("A29","On The Origin of Species",9790000000029,"Signet","2003"),
("A30","Philosophae Naturalis Principia Mathematica",9790000000030,"University of California Press","2016"),
("A31","The Unbearable Lightness of Being",9790000000031,"Harper Perennial Modern Classics","2009"),
("A32","The Art of War",9790000000032,"LSC Communications","2007"),
("A33","Ficciones",9790000000033,"Penguin Books","1999"),
("A34","El Amor en Los Tiempos del Colera",9790000000034,"Vintage","2007"),
("A35","Pedro Paramo",9790000000035,"Grove Press","1994"),
("A36","The Labyrinth of Solitude",9790000000036,"Penguin Books","2008"),
("A37","Twenty Love Poems and a Song of Despair",9790000000037,"Penguin Classics","2006"),
("A38","QED: The Strange Theory of Light and Matter",9790000000038,"Princeton University Press","2014"),
("A39","A Brief History of Time",9790000000039,"Bantam","1996"),
("A40","Cosmos",9790000000040,"Ballantine Books","2013"),
("A41","Calculus Made Easy",9790000000041,"St Martins Pr","1970"),
("A42","Notes on Thermodynamics and Statistics",9790000000042,"University of Chicago Press","1988"),
("A43","The Federalist",9790000000043,"Coventry House Publishing","2015"),
("A44","Second Treatise of Government",9790000000044,"Hackett Publishing Company, Inc.","1980"),
("A45","The Open Society and Its Enemies",9790000000045,"Princeton University Press","2020"),
("A46","A People's History of the United States",9790000000046,"Harper Perennial Modern Classics","2015"),
("A47","Lord of the Flies",9790000000047,"Penguin Books","2003"),
("A48","Animal farm",9790000000048,"Wisehouse Classics","2021"),
("A49","The Old Man and the Sea",9790000000049,"Scribner","1995"),
("A50","Romance of the Three Kingdoms",9790000000050,"Penguin Books","2018");

/* Initialising database with the 50 books into the authors relation */
INSERT IGNORE INTO Authors(accessionNo, author) VALUES

("A01","George Orwell"),
("A02","Gabriel Garcia Marquez"),
("A03","Aldous Huxley"),
("A04","Fyodor Dostoevsky"),
("A05","C.S. Lewis"),
("A06","Mary Shelley"),
("A07","John Steinbeck"),
("A08","Mark Twain"),
("A09","Charles Dickens"),
("A10","Joseph Heller"),
("A11","Homer"),
("A12","Victor Hugo"),
("A13","James Joyce"),
("A14","Vladimir Nabokov"),
("A15","Ayn Rand"),
("A16","Patrick Suskind"),
("A17","Franz Kafka"),
("A18","Bret Easton Ellis"),
("A19","Rene Goscinny,Albert Uderzo"),
("A20","Ray Bradbury"),
("A21","Isaac Asimov"),
("A22","Karl Marx,Friedrich Engels"),
("A23","Thomas Paine"),
("A24","Niccolo Machiavelli"),
("A25","Adam Smith"),
("A26","Miguel de Cervantes Saavedra"),
("A27","Simone de Beauvoir"),
("A28","Immanuel Kant"),
("A29","Charles Darwin"),
("A30","Isaac Newton"),
("A31","Milan Kundera"),
("A32","Sun Tzu"),
("A33","Jorge Luis Borges"),
("A34","Gabriel Garcia Marquez"),
("A35","Juan Rulfo"),
("A36","Octavio Paz"),
("A37","Pablo Neruda"),
("A38","Richard Feynman"),
("A39","Stephen Hawking"),
("A40","Carl Sagan"),
("A41","Silvanus P. Thompson,Martin Gardner"),
("A42","Enrico Fermi"),
("A43","Alexander Hamilton,James Madison,John Jay"),
("A44","John Lcke,C. B. Macpherson"),
("A45","Karl Popper"),
("A46","Howard Zinn"),
("A47","William Golding"),
("A48","George Orwell"),
("A49","Ernest Hemingway"),
("A50","Luo Guanzhong");                                