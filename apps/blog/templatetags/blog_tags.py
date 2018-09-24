from django import template
from django.db.models import Count
from blog.models import Category, Post

register = template.Library()


@register.assignment_tag
def get_all_categories():
    """ Make this return all categories for authenticated users and only public cats for anonymouse users """
    cats = Category.objects.all()
    return cats


@register.assignment_tag
def get_used_categories():
    """ Get a list of categories that are being used """
    return Category.objects.annotate(post_count=Count('posts')).filter(post_count__gt=0)


@register.assignment_tag
def get_used_public_categories():
    """ Get a list of categories that are used on 'public' blog posts """
    return Category.objects.annotate(post_count=Count('posts')).filter(posts__status=Post.PUBLISHED_STATUS).filter(post_count__gt=0)


@register.assignment_tag()
def get_latest_public_posts(num):
    return Post.objects.latest_public().order_by('-is_featured', '-publish_date')[:num]


