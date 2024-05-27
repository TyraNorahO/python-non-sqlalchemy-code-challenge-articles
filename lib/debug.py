#!/usr/bin/env python3
from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def magazines(self):
        return list(set(article.magazine for article in self._articles if article.magazine))

    def topic_areas(self):
        magazines = self.magazines()
        return list(set(magazine.category for magazine in magazines))

    def __str__(self):
        return f"Author: {self._name}"

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        return article

    def articles(self):
        return self._articles

    def contributors(self):
        authors = [article.author for article in self._articles if article.author]
        return list(set(authors))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = self.contributors()
        return [author for author in authors if sum(1 for article in author.articles() if article.mag