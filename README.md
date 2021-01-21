# Телфонный справочник: ТЗ


В данной работе необходимо реализовать простой телефонный справочник.
Телефонным справочником является файл, хранящийся на жестком диске, который содержит информацию, соотносящую идентификатор человека (например, имя) с некоторыми данными о нем: номер телефона, дата рождения и т.д.
Необходимо разработать программу, которая будет предоставлять консольный интерфейс для работы с этим файлом.
Каждая запись в справочнике должна обладать следующими полями:
 - Имя (только латинские буквы, цифры и пробелы, первая буква – заглавная)
 - Фамилия (только латинские буквы, цифры и пробелы, первая буква – заглавная)
NB: Пара (Имя, Фамилия) является уникальным идентификатором записи в справочнике.
 - Номер телефона (состоит из 11 цифр без знака +) NB: При заполнении обязательна проверка на корректность номера и автозамена «+7» в начале номера на «8».
 - Дата рождения (полная – число, месяц и год). Поле является опциональным, т.е. его заполнение не обязательно, оно может оставаться пустым. NB: При заполнении обязательна проверка на корректность даты.
Консольный интерфейс:
 - Под консольным интерфейсом понимается следующее: в интерпретаторе/командной строке/терминале запускается на выполнение программа (скрипт), которая предлагает пользователю конечный набор команд для работы со справочником.
 - При вводе определенной команды (например, «добавить новую запись») программа выполняет соответствующие действия, необходимые для реализации этой команды.
2
 - После выполнения введенной команды программа снова предлагает пользователю выбрать команду и ожидает ввода.
 - Программа должна заканчивать свое выполнение только после ввода специальной команды (например, «quit»).
Требования к программе:
1) При запуске программы (скрипта), она должна считывать содержимое телефонного справочника из файла, хранящего на жестком диске. Файл может как содержать записи (в корректном виде), так и быть пустым.
2) При завершении работы программы и/или при завершении выполнении команды, изменяющей справочник, все изменения в справочнике должны быть сохранены в файл (тот, из которого справочник считывается в начале).
3) Минимальный набор поддерживаемых команд для работы со справочником:
 - Просмотр всех записей справочника: вывод всего справочника так, чтобы было читабельно.
 - Поиск по справочнику. Поиск может осуществляться по любому из полей, а также по нескольким полям одновременно (например, найти запись с именем «А» и фамилией «Б»). В результате поиска должны быть выведены найденные записи со значением полей.
 - Добавление новой записи. NB: Обязательна проверка на то, что такая запись не содержится в справочнике (по уникальному идентификатору). Если такая запись уже содержится в справочнике, сообщить об этом пользователю и предложить: изменить существующую запись, изменить (Имя, Фамилия) новой записи или вернуться к выбору команды. NB: При вводе Имени и Фамилии обязательна автозамена первой буквы на заглавную.
 - Удаление записи из справочника по Имени и Фамилии
 - Изменение любого поля в определенной записи справочника
 - Вывод возраста человека (записи) по Имени и Фамилии
4) Если пользователь неправильно ввел команду, программа должна проинформировать его о некорректном вводе и вернуться в состояние ожидания ввода команды.
5) Ни одна операция не должна заканчиваться ошибкой или вылетом программы при поступлении любых входных данных – либо операция должна быть корректно обработана, либо должно быть выведено сообщение об ошибке (желательно информативное), и программа возвращена в состояние ожидания ввода.
3
В случае идеального выполнения всех обязательных требований ставится оценка 7.
Дополнительные баллы можно получить за следующие пункты:
 - Качественный и понятный для чтения код; Удобный интерфейс для взаимодействия, в котором довольно просто ориентироваться.
 - Наличие объясняющей документации к программе: описание реализованных функций и возможностей программы, примеры использования (в формате .docx, .pdf или .pptx; docstring в исходном коде).
 - Реализация дополнительных возможностей программы:
o Возможность добавления несколько номеров телефона для одной записи с категоризацией: мобильный, рабочий, домашний и т.д.
o Удаление по номеру телефона. NB: обязательна проверка на наличие нескольких записей с таким номером. Предоставить выбор пользователю, какую именно запись или несколько удалить.
o Поиск и вывод записей по дате рождения (день и месяц, год не учитывается).
o Просмотр всех записей (только поля Имя и Фамилия), у которых день рождения в ближайший месяц (30 дней).
o Просмотр всех записей, которые старше / младше / ровно N лет (N задаётся пользователем).
o Дополнительные возможности программы и расширение функционала. От добавления новых полей и функций работы с ними, до графического интерфейса и использования базы данных для хранения словаря.
Успешное выполнение первых 2-х пунктов оценивается в 0.5 балла за каждый пункт. Реализация дополнительных возможностей программы оценивается в 1 балл за каждый пункт, кроме последнего – ваши личные идеи будут оценены в зависимости от сложности задачи и качества реализации.
Important
Вместе с кодом и документацией необходимо подготовить текстовый файл (docx, pdf, html) с примерами работы программы (ввод и вывод) для каждого сценария и каждого выполненного задания. Также необходимо приложить файл-справочник, использованный в примерах. Эти примеры будут использованы для тестирования вашей программы. Задания, для которых не будет примеров, будут считаться невыполненными.
4
Советы:
1) Постарайтесь везде сделать проверки на корректность любых вводимых данных.
2) Формат хранения файла-справочника может быть любой удобный вам, главное – наличие вышеобозначенных функций из списка обязательных и дополнительных.
3) Желательно, чтобы программа была «разговорчивой»: гораздо приятнее, когда пользователь понимает, какого ввода от него ждут на каждом шаге. Такой вариант выглядит неплохо:
Но так понятнее и удобнее: