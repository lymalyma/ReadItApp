from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView
from .forms import BookForm, ReviewForm
# from django.http import HttpResponse # we can remove it cause we dont use it now.
from .models import Author, Book #We now import Author too!
# Create your views here.

def list_books(request):
	"""
	List the books that have reviews
	"""

	books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')

	context = {
		'books': books,
	}

	return render(request, "list.html", context)



class AuthorList(View):
	def get(self, request):
		authors = Author.objects.annotate(
			published_books = Count('books')
		).filter(
			published_books__gt = 0
		)
		context = {'authors': authors, }

		return render(request, 'authors.html', context)


class BookDetail(DetailView):
	model = Book
	template_name = 'book.html'


class AuthorDetail(DetailView):
	model = Author
	template_name = 'author.html'



class ReviewList(View):
	"""
	List all of the books that we want to review.
	"""

	"""
	define a get method
	"""
	def get(self, request):
		books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')

		context = {
			'books': books,
			'form': BookForm,
		}

		return render(request, "list-to-review.html", context)

	def post(self, request):
		form = BookForm(request.POST)
		books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')

		if form.is_valid:
			form.save()
			return redirect('review_books')

		context = {
			'form': form,
			'books': books,
		}

		return render(request, "list-to-review.html", context)




def review_book(request, pk):
	"""
	Review an individual book
	"""
	book = get_object_or_404(Book, pk=pk)

	if request.method == "POST":
		form = ReviewForm(request.POST)
		if form.is_valid(): #this is a django built-in method for the form
			book.is_favourite = form.cleaned_data['is_favourite']
			book.review = forms.cleaned_data['review']
			book.save()

			return redirect('review_books')

		#Process the form
	else:
		# render empty form.
		form = ReviewForm


	context = {
		'book': book,
		'form': form,
	}

	return render(request, "review-book.html", context)
