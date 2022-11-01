class Publication():
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f'Publication {self.name}')


class Book(Publication):
    def __init__(self, name, author, number_of_pages):
        super().__init__(name)
        self.author = author
        self.number_of_pages = number_of_pages

    def print_information(self):
        super().print_information()
        print(f'was written by the author {self.author} and has {self.number_of_pages} pages')


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f'was edited by a chief editor {self.chief_editor}')


p1 = Book('Compartment No. 6', 'Rosa Liksom', 192)
p1.print_information()
p2 = Magazine('Donald Duck', 'Aki Hyyppä')
p2.print_information()
