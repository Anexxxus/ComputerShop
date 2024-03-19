# ComputerShop
ComputerShop (Telegram bot + Python + PosgtreSQL)
Before you start working, you need to create an empty database in PgAdmin, then clicking on this database, you need to click "Restore", then enter ComputerShop.sql
To run the program in Python, you need to install such libraries as:
pip insall psycopg2, pyqt5, qt-material, python-docx, telebot.
Immediately I say that images in the program do not work, I have to manually write the path in PgAdmin through the console. Examples:

    — Update the record for the product 'HP Pavilion Laptop' by adding an image
    UPDATE Товары 
    SET Изображение = CAST(encode(pg_read_binary_file('C:/Program 
    Files/PostgreSQL/16/Products/hp pavilion.jpg'), 'escape') AS bytea)
    WHERE Наименование = 'Ноутбук HP Pavilion';
    
    UPDATE Товары 
    SET Изображение = CAST(encode(pg_read_binary_file('C:/Program Files/PostgreSQL/16/Products/iphon13.jpg'), 'escape') AS bytea)
    WHERE Наименование = 'Смартфон iPhone 13';

Before we start to populate the images into the database, we need to move the image data into the PostgreSQL folder, here is an example: C:/Program Files/PostgreSQL/16/Products/iphon13.jpg
Then create a Telegram bot via https://t.me/BotFather , copy the api and paste it into the code, as well as change the data to connect the database under yourself.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Перед тем как начать работу, нужно создать в PgAdmin пустую базу данных, после чего нажав на эту базу данных, нужно нажать "Восстановить", после чего заносите ComputerShop.sql
Для работы программы на Python, нужно установить такие библиотеки как:
pip insall psycopg2, pyqt5, qt-material, python-docx, telebot.
Сразу говорю, что изображения в программе не работаю, приходится вручную прописывать путь в PgAdmin через консоль. Примеры:

     — Обновляем запись для товара 'Ноутбук HP Pavilion', добавляя изображение
    UPDATE Товары 
    SET Изображение = CAST(encode(pg_read_binary_file('C:/Program 
    Files/PostgreSQL/16/Products/hp pavilion.jpg'), 'escape') AS bytea)
    WHERE Наименование = 'Ноутбук HP Pavilion';
    
    UPDATE Товары 
    SET Изображение = CAST(encode(pg_read_binary_file('C:/Program Files/PostgreSQL/16/Products/iphon13.jpg'), 'escape') AS bytea)
    WHERE Наименование = 'Смартфон iPhone 13';

Перед началом чтобы заносить изображения в базу данных, нужно перенести данные изображения в папку с PostgreSQL, вот пример: C:/Program Files/PostgreSQL/16/Products/iphon13.jpg
Далее создаете телеграм бота через https://t.me/BotFather , копируете api и вставляете в код, так же меняете данные к подключения базе данных под себя
