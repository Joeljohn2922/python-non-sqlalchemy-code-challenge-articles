class Article: 

    all = [] 

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title 
        Article.all.append(self)
    
    @property 
    def title(self): 
        return self._title 
    
    @title.setter 
    def title(self, title): 
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, '_title'):
            self._title = title 
    
    @property 
    def author(self): 
        return self._author 
    
    @author.setter 
    def author(self, new_author): 
        if isinstance(new_author, Author):
            self._author = new_author 
    
    @property 
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str)and 0 < len(new_name) and not hasattr(self, "_name"):
            self._name = new_name


        
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self): 
        return list({article.magazine for article in self.articles()})
        

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list({article.magazine.category for article in self.articles()})

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
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name 
    
    @property 
    def category(self): 
        return self._category 
    
    @category.setter 
    def category(self, new_category): 
        if isinstance(new_category, str) and 0 < len(new_category):
            self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})


    def article_titles(self):
        if not self.articles():
            return None
        return [articles.title for articles in self.articles()]

    def contributing_authors(self):
        author_counts = {} 
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        
        if contributing_authors:
            return contributing_authors 
        else:
             None