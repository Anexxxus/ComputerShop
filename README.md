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
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Program images
![изображение](https://github.com/Anexxxus/ComputerShop/assets/68741206/9a10fb3c-b2ef-4236-822c-45aa8dc30378)
![изображение](https://github.com/Anexxxus/ComputerShop/assets/68741206/0df8f728-785f-4330-8ce6-c8a31ad9cb4a)
![изображение](https://github.com/Anexxxus/ComputerShop/assets/68741206/824ea1d3-12de-4e8a-ac4d-3750998f8bbf)
![изображение](https://github.com/Anexxxus/ComputerShop/assets/68741206/93ebc662-d28c-45e8-826e-0675591cb2bb)
![изображение](https://github.com/Anexxxus/ComputerShop/assets/68741206/2d90d011-4a94-4ed1-99d9-770bac51f149)
![изображение](https://github.com/Anexxxus/ComputerShop/assets/68741206/26b806d3-b8cd-4ba5-8293-0526e1c996a0)
![изображение](https://github.com/Anexxxus/ComputerShop/assets/68741206/627c164f-ffda-4d99-aa9b-6eecad306c90)
![изображение](https://github.com/Anexxxus/ComputerShop/assets/68741206/a79c2f2d-e803-45ff-a078-f4c7efd0e71b)
![изображение](https://github.com/Anexxxus/ComputerShop/assets/68741206/2a904ca6-72c0-4961-af42-fde6709f9365)
![изображение](https://github.com/Anexxxus/ComputerShop/assets/68741206/01733b78-1cdd-4dde-baed-afd4c6c13aac)
![изображение](https://github.com/Anexxxus/ComputerShop/assets/68741206/a7c4f140-2c0d-418b-a8dc-67a7f1442efc)
![изображение](https://github.com/Anexxxus/ComputerShop/assets/68741206/6fa4b789-8cf1-48f6-a317-9d4887b87114)
