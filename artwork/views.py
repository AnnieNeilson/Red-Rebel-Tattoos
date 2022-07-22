from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.messages import constants as messages
from .models import Post
from .forms import CommentForm, ContactForm, BookingForm



class HomePage(generic.TemplateView):
    template_name = 'index.html'


class BookingPage(View):
    template_name = 'booking.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "booking.html",
            {
                "booking_form": BookingForm(),
            },)

    def post(self, request, *args, **kwargs):
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.save() 
        booking_form = BookingForm()
        return render(request, 'booking_successful.html',)


class ContactPage(View):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "contact.html",
            {
                "contact_form": ContactForm(),
            },)

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save() 
        contact_form = ContactForm()
        return render(request, 'contact_successful.html',)


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'artwork.html'
    paginate_by = 9


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


