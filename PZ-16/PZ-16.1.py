#Вариант 16
"""
Создайте класс «Книга», который имеет атрибуты название, автор и количество страниц. Добавьте методы для чтения и записи книги.
"""

import json
import os

class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация класса

        Args:
            title (str): Название книги
            author (str): Автор книги
            pages (int): Количество страниц
        """
        self.title = title
        self.author = author
        self.pages = pages
    
    #валидация
    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("В названии книги должно быть не пустым.")
        self._title = value.strip()
    
    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Имя автора не должно быть пустой строкой")
        self._author = value.strip()
    
    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц быть положительным целым числом")
        self._pages = value
    
    #методы

    def to_dict(self) -> dict:
        """Превращает книгу в словарь"""
        return {
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
        }
    
    def save(self, filepath: str) -> None:
        """
        Записывает данные книги в json файл

        Args:
            filepath (str): путь к файлу для сохранения
        """
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)
    
    #методы чтения
    @classmethod
    def load(cls, filepath: str) -> "Book":
        """
        Читает книгу из json и возвращает объект Book

        Args:
            filepath (str): путь к файлу

        Returns:
            Book: загруженный объект книги
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Файл '{filepath}' не найден")
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls(
            title=data["title"],
            author=data["author"],
            pages=data["pages"],
        )
    
    def read_info(self) -> str:
        """Возвращает строковое описание книги"""
        return (
            f"Книга: {self.title}\n"
            f"Автор: {self.author}\n"
            f"Количество страниц: {self.pages}"
        )
    
    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.to_dict() == other.to_dict()
    
if __name__ == "__main__":
    book = Book(title="Мастер и Маргарита", author="Михаил Булгаков", pages=480)

    print(book.read_info())

    book.save("book.json")

    loaded = Book.load("book.json")
    print("Загруженная книга:\n",loaded.read_info())

    print(f"Книги совпадают: {book == loaded}")
    