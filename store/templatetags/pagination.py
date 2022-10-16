from django import template

register = template.Library()

@register.inclusion_tag('include/pagination.html')
def pagination(page_obj, distance):
    current_page = page_obj.number
    page_range = page_obj.paginator.page_range
    start_point, end_point = 1, page_range[-1]
    if current_page - distance > 1:
        start_point = current_page - distance
    if current_page + distance < page_range[-1]:
        end_point = current_page + distance
    return {
        'page_obj': page_obj,
        'page_range': range(start_point, end_point + 1)
    }