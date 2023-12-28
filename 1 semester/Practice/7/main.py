import csv


def get_book(name: str, reader: csv.reader) -> list:
    results = []
    for row in reader:
        if name in row[1].lower():
            results.append(row)
    return results


def get_totals_mk1(books: list) -> list:
    books_totals = []
    for book in books:
        isbn, total = book[0], int(book[3])*float(book[4])
        books_totals.append((isbn, total))
    return books_totals


def get_totals_mk2(books: list, min_total: float, increase: float) -> list:
    books_totals = []
    for book in books:
        isbn, total = book[0], int(book[3])*float(book[4])
        if total < min_total:
            total += increase
        books_totals.append((isbn, total))
    return books_totals


with open('books.csv', 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    books = get_book('python', r)
    totals_1 = get_totals_mk1(books)
    totals_2 = get_totals_mk2(books, 200, 100)
