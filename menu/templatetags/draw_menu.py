from django import template

from menu.models import MenuItem



register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(title, item_selected=None):
    '''Tag for drawing menu'''
    menu_items = MenuItem.objects.filter(
        menu__title = title, parent=None
    ).prefetch_related('child_items', 'child_items__child_items')
    try:
        return {'menu_items': menu_items}
    except TemplateSyntaxError:
        msg = ('Did not match any of the menu item!')
        raise template.TemplateSyntaxError(msg)