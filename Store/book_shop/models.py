from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 4️⃣ Окуучу (читатель)
class Reader(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.full_name


# 5️⃣ Китепти алуу (карызга алуу)
class Borrow(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.reader} → {self.book}"


# 6️⃣ Басмакана (издательство)
class Publisher(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


# 7️⃣ Китеп дүкөнү (же филиал)
class LibraryBranch(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.name
