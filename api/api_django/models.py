from django.db import models

from users.models import Customer, User
from django.utils import timezone

# from textblob import TextBlob
# from googletrans import Translator
# from transformers import pipeline


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    video = models.FileField(upload_to="videos/", null=True, blank=True)
    image = models.ImageField(upload_to='products_images/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="products"
    )
    pub_date = models.DateField(auto_now_add=True)
    stock = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    products = models.ManyToManyField(
        Product, related_name="orders"
    )  # Исправлено на "products"
    pub_date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.ForeignKey("Discount", on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")  # Поле для промокода

    def __str__(self):
        return f"Заказ {self.id} от {self.user}, количество товаров: {self.products.count()}"
    
    def apply_discount(self):
        if self.discount and self.discount.is_active:
            discount_amount = (self.total_price * self.discount.discount_percentage) / 100
            self.total_price -= discount_amount
        else:
            return self.total_price


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_orders")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


# def analyze_sentiment(text):
#     # Переводим текст на английский для лучшего анализа
#     translator = Translator()
#     translated_text = translator.translate(text, src="ru", dest="en").text

#     # Анализируем переведенный текст
#     blob = TextBlob(translated_text)
#     sentiment = (
#         blob.sentiment.polarity
#     )  # Полярность текста от -1 (негативный) до 1 (позитивный)
#     return sentiment


# sentiment_analyzer = pipeline(
#     "sentiment-analysis", model="blanchefort/rubert-base-cased-sentiment"
# )


# Модель ProductReview
class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )  # Привязываем к продукту
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="product_reviews"
    )  # Связь с клиентом
    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]
    )  # Оценка от 1 до 5
    comment = models.TextField()  # Текст отзыва
    sentiment = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания отзыва
    video = models.FileField(upload_to="video_review/", null=True, blank=True)
    image = models.ImageField(upload_to='review_images/', null=True, blank=True)

    def __str__(self):
        return f"Отзыв на {self.product.name} от {self.customer.user.username}"

#     def analyze_sentiment(self):
#         """
#         Метод для анализа настроения отзыва. Использует модель sentiment-analysis
#         для оценки текста отзыва.

#         Возвращает:
#         - 1, если отзыв положительный
#         - -1, если отзыв отрицательный
#         - 0, если отзыв нейтральный

#         Метод анализирует поле `comment`, получая результат с помощью предварительно
#         обученной модели, которая возвращает метку настроения (POSITIVE/NEGATIVE/NEUTRAL)
#         и соответствующий балл.
#         """
#         if isinstance(self.comment, str):
#             result = sentiment_analyzer(self.comment)
#             sentiment_label = result[0]["label"]
#             score = result[0]["score"]

#             if sentiment_label == "POSITIVE" and score > 0.6:
#                 return "POSITIVE"
#             elif sentiment_label == "NEGATIVE" and score > 0.6:
#                 return "NEGATIVE"
#             else:
#                 return "NEUTRAL"

#     def save(self, *args, **kwargs):
#         if not isinstance(self.comment, str):
#             self.comment = str(self.comment)
#         self.sentiment = str(self.analyze_sentiment())

#         super(ProductReview, self).save(*args, **kwargs)


class Discount(models.Model):
    code = models.CharField(max_length=50, unique=True)  # Промокод
    discount_percentage = models.PositiveIntegerField()  # Процент скидки
    valid_from = models.DateField()  # Изменено на DateField
    valid_to = models.DateField()    # Изменено на DateField
    is_active = models.BooleanField(default=True)  # Активность промокода

    def __str__(self):
        return f"{self.code} - {self.discount_percentage}%"

    def get_discount_percentage(self):
        """
        Проверяет, действителен ли промокод, и возвращает скидку.
        Если промокод не действителен, возвращает None.
        """
        now = timezone.now()
        if self.is_active and self.valid_from <= now <= self.valid_to:
            return self.discount_percentage
        return None
    
class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchase_history")
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    purchase_date = models.DateTimeField(auto_now_add=True)