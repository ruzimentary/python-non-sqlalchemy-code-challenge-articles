class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception('Author must be an instance of the Author class')

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception('Magazine must be an instance of the Magazine class')

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            raise AttributeError('Title is immutable once set')
        if not isinstance(title, str):
            raise TypeError('Title must be a string')
        if not (5 <= len(title) <= 50):
            raise ValueError('Title must be between 5 and 50 characters')
        self._title = title


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise AttributeError('Name may not be changed')
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError('Name must be a non-empty string')

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        result = []
        for article in Article.all:
            if article.author is self and article.magazine not in result:
                result.append(article.magazine)
        return result

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        result = list(set([article.magazine.category for article in Article.all if article.author is self]))
        return result if result else None


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError('Name must be between 2 and 16 characters')

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError('Category cannot be empty')

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine is self]))

    def article_titles(self):
        result = [article.title for article in Article.all if article.magazine is self]
        return result if result else None

    def contributing_authors(self):
        all_authors = [article.author for article in self.articles()]
        contributors = []
        for author in set(all_authors):
            if all_authors.count(author) > 2:
                contributors.append(author)
        return list(contributors) if contributors else None

    @classmethod
    def top_publisher(cls):
        all_articles_by_magazine = [article.magazine for article in Article.all]
        highest_total = [None, 0]
        for magazine in set(all_articles_by_magazine):
            if all_articles_by_magazine.count(magazine) > highest_total[1]:
                highest_total = [magazine, all_articles_by_magazine.count(magazine)]
        return highest_total[0]
