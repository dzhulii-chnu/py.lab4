articles = [
    {'title': ' Functional Python 101 ', 'content': '...', 'tags': ['python', 'functional', 'PYTHON']},
    {'title': 'Async in Python', 'content': '...', 'tags': ['python', 'async']},
    {'title': 'Decorators Explained', 'content': '', 'tags': ['python', 'decorators']},
    {'title': '  Data Science Basics', 'content': '...', 'tags': ['data', 'pandas', 'numpy', 'data']},
]

def has_content(article):
    return bool(article.get('content'))


def extract_fields(article):
    return article['title'], article['tags']


def normalize_tags(tags):
    return sorted(set(map(str.lower, tags)))

def clean_article(pair):
    title, tags = pair
    return {
        'clean_title': title.strip(),
        'unique_tags': normalize_tags(tags),
    }

def normalize_data(articles):
    filtered = filter(has_content, articles)
    extracted = map(extract_fields, filtered)
    cleaned = map(clean_article, extracted)
    return sorted(cleaned, key = lambda a: len(a['unique_tags']), reverse = True)

print(normalize_data(articles))