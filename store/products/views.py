from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db.models import Count
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext as _

from django_filters.views import FilterView

from store.comments.forms import CommentForm
from store.qas.forms import QuestionForm, AnswerForm
from store.cart.forms import CartAddProductForm
from .models import Product, Category
from .mixins import SortMixin
from .filters import ProductFilter


class ProductListView(SortMixin, FilterView):
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 10
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = Product.objects.active_with_stock_info()
        return self.get_sorted_queryset(queryset)


class CategoryListView(SortMixin, FilterView):
    template_name = 'products/category_list.html'
    context_object_name = 'products'
    paginate_by = 10
    filterset_class = ProductFilter

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=category_slug)
        queryset = category.products.active_with_stock_info()
        return self.get_sorted_queryset(queryset)


class ProductDetailView(generic.DetailView):
    template_name = 'products/detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        product_slug = self.kwargs.get('slug')
        return Product.objects.with_related_info(product_slug)

    def get_object(self):
        product = super().get_object()

        ip_address = self.request.user.ip_address
        if ip_address not in product.hits.all():
            product.hits.add(ip_address)

        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product = self.object
        tags = product.category.values_list('id', flat=True)
        similar_products = Product.objects.active_with_stock_info()\
            .filter(category__in=tags)\
            .exclude(id=product.id)\
            .annotate(same_tags=Count('category'))\
            .order_by('-same_tags', '-created')[:4]

        context['comment_form'] = CommentForm()
        context['question_form'] = QuestionForm()
        context['answer_form'] = AnswerForm()
        context['add_to_cart_form'] = CartAddProductForm()
        context['similar_products'] = similar_products
        context['add_to_wishlist'] = product.favorites.all()
        return context


@require_POST
@login_required
def product_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user not in product.favorites.all():
        product.favorites.add(request.user)
        messages.success(request, _('The product successfully added to favorite.'))
    else:
        product.favorites.remove(request.user)
        messages.success(request, _('The product successfully removed from favorite.'))

    return redirect(product.get_absolute_url())


class WishListView(LoginRequiredMixin, generic.ListView):
    template_name = 'products/wish_list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        user = self.request.user
        queryset = Product.objects.active_with_stock_info()
        queryset = queryset.filter(favorites=user)
        return queryset



