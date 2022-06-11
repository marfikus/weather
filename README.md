# Weather

Небольшой учебный проект по материалам [Алексея Голобурдина](https://github.com/alexey-goloburdin) и команды "Диджитализируй!":  
[Книга "Типизированный Python"](https://t.me/t0digital/151)  
[Видео](https://www.youtube.com/watch?v=dKxiHlZvULQ)

Программа читает GPS координаты (в данном случае из файла, поскольку GPS модуля у меня нет), делает запрос к сервису погоды [OpenWeather](https://openweathermap.org/api), парсит результат, выводит его в терминал и сохраняет в историю запросов.

Запускается файлом [**weather**](https://github.com/marfikus/weather/blob/master/weather), который должен быть исполняемым.  
Для работы необходим ключ доступа к API сервиса погоды, для получения которого необходино зарегистрироваться. Затем добавить файл **api_key.py**, в который поместить полученный ключ в формате: `OPENWEATHER_APP_ID = "your-api-key"`  
Или же можно немного изменить [**config.py**](https://github.com/marfikus/weather/blob/master/config.py), чтобы как-то иначе получать этот ключ.

Для запуска использовался python 3.10 без сторонних библиотек.
