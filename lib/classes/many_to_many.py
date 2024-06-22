# File: classes/many_to_many.py

class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass  # Title is immutable

    @staticmethod
    def get_all_articles():
        return Article.all


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_articles = {}
        for article in self.articles():
            author = article.author
            if author not in author_articles:
                author_articles[author] = 0
            author_articles[author] += 1
        return [author for author, count in author_articles.items() if count > 2] or None

    @staticmethod
    def top_publisher():
        if not Article.all:
            return None
        magazine_article_counts = {}
        for article in Article.all:
            magazine = article.magazine
            if magazine not in magazine_article_counts:
                magazine_article_counts[magazine] = 0
            magazine_article_counts[magazine] += 1
        top_magazine = max(magazine_article_counts, key=magazine_article_counts.get)
        return top_magazine if magazine_article_counts[top_magazine] > 0 else None


class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass  # Name is immutable

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = list(set(article.magazine.category for article in self.articles()))
        return topics if topics else None
