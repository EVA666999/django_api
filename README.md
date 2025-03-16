# OrderFlow API – Управление заказами и продуктами
Этот проект представляет собой API для управления заказами и продуктами, построенное с использованием Django, Django REST Framework, и интеграцией с ИИ для генерации SQL-запросов и анализа тональности комментариев.

## Особенности

- Аутентификация пользователей (регистрация и вход с использованием JWT).
- CRUD-операции для работы с заказами, продуктами и категориями.
- Расчет общей стоимости заказов.
- Привязка продуктов к заказам и категорий к продуктам.
- Email-уведомления.
- Работа с промокодами/скидками.
- Подключение почтового сервиса.
- Интеграция с MISTRAL для генерации SQL-запросов.
- Документация API с OpenAPI (Swagger и Redoc).
- Тесты API на основе Pytest.
- Добавление фото и видео к продуктам.
- Система анализа настроения комментариев.
- Роли пользователей и система разрешений.

## Авторизация

- **POST** `/auth/users/`: Зарегистрировать нового пользователя.
- **POST** `/auth/jwt/create/`: Получить токен.
- **POST** `/auth/jwt/refresh/`: Обновить токен доступа.

## Роли пользователей

При регистрации пользователь выбирает свою роль:

- **Администратор** (`admin`) – полный доступ ко всем ресурсам. (обычный пользователь не сможет выбрать)
- **Поставщик** (`supplier`) – управление товарами и заказами.
- **Сотрудник** (`employee`) – обработка заказов и взаимодействие с клиентами.
- **Клиент** (`customer`) – оформление заказов и просмотр товаров.

## Заказы

- **GET** `/api/orders/`: Получить все заказы аутентифицированного пользователя.
- **POST** `/api/orders/`: Создать новый заказ.
- **PUT** `/api/orders/{order_id}/`: Обновить заказ по его ID.
- **DELETE** `/api/orders/{order_id}/`: Удалить заказ по его ID.

## Продукты

- **GET** `/api/products/`: Получить все продукты.
- **POST** `/api/products/`: Создать новый продукт.
- **PUT** `/api/products/{product_id}/`: Обновить продукт по его ID.
- **DELETE** `/api/products/{product_id}/`: Удалить продукт по его ID.

## Категории
- **GET** `/api/category/`: Получить все категории.
- **POST** `/api/category/`: Создать новую категорию.
- **PUT** `/api/category/{category_id}/`: Обновить категорию по её ID.
- **DELETE** `/api/category/{category_id}/`: Удалить категорию по её ID.

## Интеграция с MISTRAL

Система использует API MISTRAL для генерации SQL-запросов на основе пользовательских запросов. Например:

**Пример запроса:**

```json
{
    "message": "Выведи все продукты, у которых рейтинг больше 4 и цена меньше 20"
}
```

**Сгенерированный SQL:**

```sql
SELECT * FROM api_django_product WHERE rating > 4 AND price < 20;
```
Этот SQL-запрос будет выполнен, и пользователю вернется список подходящих продуктов.

## Добавление медиафайлов к продуктам
Каждый продукт может содержать изображение и видео:

## Анализ настроения комментариев
Каждый отзыв анализируется на предмет положительного, отрицательного или нейтрального тона.
Эта система позволяет улучшить взаимодействие пользователей с платформой и автоматизировать обработку отзывов.