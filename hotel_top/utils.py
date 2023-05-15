menu = [{'title': "Home",            'url_name': 'main_page_path', 'for_s_user':False},
        {'title': "Search the room", 'url_name': 'search_path',    'for_s_user':False},
        {'title': "Reviews",         'url_name': 'review_path',    'for_s_user':False},
        {'title': "Inquiry",         'url_name': 'inquiry_path',    'for_s_user':False}
        ]

staff_menu = [{'title': "Staff Home", 'url_name': 'main_page_staff', 'for_s_user':False},
              {'title': "Inquiries",  'url_name': 'inquiries',       'for_s_user':False},
              {'title': "Bookings",   'url_name': 'booking_staff',   'for_s_user':False},
    #          {'title': "Favorites", 'url_name': 'inquiries', 'for_s_user':False}
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu 
        return context