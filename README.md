# Проект по тестированию API  <a target="_blank" href="https://petstore.swagger.io//">Petstore</a>

![main page screenshot](pictures/main_page_petstore.png)

---
### Список проверок, реализованных в автотестах:
1. Создание одного питомца.
2. Поиск питомца по ID.
3. Поиск несуществующего питомца.
4. Поиск всех питомцев по указанному статусу.
5. Удаление питомца.

---

## Используемый стек технологий и инструментов

|                             Python                             |                             Pytest                             |                              Git                               |                                 Jenkins                                 |                                Allure                                 |                             Allure TestOps                             |                                 PyCharm                                  |                             Telegram                             | Requests                                                         |
|:--------------------------------------------------------------:|:--------------------------------------------------------------:|:--------------------------------------------------------------:|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|:----------------------------------------------------------------:|------------------------------------------------------------------|
| <img width="55" height="55" src="/pictures/icons/python.svg"/> | <img width="55" height="55" src="/pictures/icons/pytest.svg"/> | <img width="55" height="55" src="/pictures/icons/github.svg"/> | <img width="55" height="55" src="/pictures/icons/jenkins-original.svg"> | <img width="55" height="55" src="/pictures/icons/allure_report.png"/> | <img width="40" height="40" src="/pictures/icons/allure_testops.svg"/> | <img width="40" height="40" src="/pictures/icons/pycharm-original.svg"/> | <img width="40" height="40" src="/pictures/icons/telegram.png"/> | <img width="40" height="40" src="/pictures/icons/requests.png"/> |

## <img width="4%" title="Jenkins" src="/pictures/icons/jenkins-original.svg"> Запуск проекта в Jenkins
#### Для запуска автотестов в Jenkins
1. __Открыть проект <a href="https://jenkins.autotests.cloud/job/petstore_api_test/">в Jenkins</a>__
2. __Выбрать пункт `Build with Parameters`__
3. __Результат запуска сборки можно посмотреть в отчете Allure__

<img width="1200" src="/pictures/jenkins_report.png">

---

## <img width="4%" title="Allure report"  src="/pictures/icons/allure_report.png"> Отчет в Allure report
>__Просмотр результатов выполнения тестов в Allure report__
<img width="1200" src="/pictures/allure_report_overview.png">

>__Отчет позволяет получить общую информацию о прохождении тестов__
> <img width="1200" src="/pictures/allure_report_suites_all.png">

>__Отчет позволяет получить информацию о прохождении каждого теста__
<img width="1200" src="/pictures/allure_report_suites_one_test.png">

__Каждый тест содержит детальную информацию по всем шагам тестов, включая скриншоты страницы и видео прохождения теста.__

---


### <img width="4%" title="Allure TestOps" src="/pictures/icons/allure_testops.svg"> Интеграция с Allure TestOps
[Тест-кейсы](https://allure.autotests.cloud/launch/44144/tree/689780?treeId=0)

<img width="1200" src="/pictures/allure_test_opts.png">

---

## <img width="4%" title="Telegram" src="/pictures/icons/telegram.png"> Оповещения в Telegram
<img width="1200" src="/pictures/tg_report.png">