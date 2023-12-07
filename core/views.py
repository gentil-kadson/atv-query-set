from django.shortcuts import render
from django.db.models import Count
from .models import Book, Author, Tag, Review, Profile

def query_examples(request):
    # Consulta simples com filter
    books_by_title = Book.objects.filter(title__icontains='teste')

    # Consulta com lookup para buscar autores por nome
    authors_by_name = Author.objects.filter(name__icontains='nome do autor')

    # Consulta many-to-many (livros com uma determinada tag)
    books_with_tag = Book.objects.filter(tags__name='nome da tag')

    # Consulta com relacionamento reverso (todos os livros de um autor)
    books_of_author = Book.objects.filter(author__name='nome do autor')

    # Consulta agregada (por exemplo, número de livros de um autor)
    num_books_of_author = Book.objects.filter(author__name='nome do autor').count()

    # Envie todas as consultas para o template
    context = {
        'books_by_title': books_by_title,
        'authors_by_name': authors_by_name,
        'books_with_tag': books_with_tag,
        'books_of_author': books_of_author,
        'num_books_of_author': num_books_of_author,
    }

    return render(request, 'core/teste1.html', context)

def respostas_exercicio(request):
    livros_por_autor = Book.objects.filter(author__name='João Felipe Cardoso')

    livros_com_tag_especifica = Book.objects.filter(tags__name='Ciência')

    autores_com_palavra_especifica_bio = Author.objects.filter(bio__icontains='Aliquam')

    livors_com_avaliacoes_altas = Book.objects.filter(reviews__rating__gte=4)

    usuarios_com_website_especifico = Profile.objects.filter(website='http://pereira.com/')

    livros_sem_avaliacoes = Book.objects.filter(reviews__rating__isnull=True)

    autores_numero_livros_ordem = Author.objects.annotate(qtde_livros=Count('books')).order_by('-qtde_livros')

    livros = Book.objects.all()
    livros_resumo_longo = []
    for livro in livros:
        palavras = livro.summary.split(' ')
        if len(palavras) > 150:
            livros_resumo_longo.append({ "title": livro.title, "qtde_palavras": len(palavras) })

    avaliacoes_livro_autor_especifico = Review.objects.filter(book__author__name='João Felipe Cardoso')

    context = { "livros_por_autor": livros_por_autor, 
               "livros_com_tag_especifica": livros_com_tag_especifica, "autores_com_palavra_especifica_bio": autores_com_palavra_especifica_bio,
                "livros_com_avaliacoes_altas": livors_com_avaliacoes_altas,
                "usuarios_com_website_especifico": usuarios_com_website_especifico,
                "livros_sem_avaliacoes": livros_sem_avaliacoes,
                 "autores_numero_livros_ordem": autores_numero_livros_ordem,
                  "livros_resumo_longo": livros_resumo_longo,
                   "avaliacoes_livro_autor_especifico": avaliacoes_livro_autor_especifico }
    return render(request, 'core/respostas.html', context)