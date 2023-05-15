menu = [{'title': "Home", 'url_name': 'main_page_path', 'for_s_user':False},
        {'title': "Search the room", 'url_name': 'search_path', 'for_s_user':False},
       {'title': "Reviews", 'url_name': 'client_reviews', 'for_s_user':True},
       {'title': "Inquiries", 'url_name': 'inquiries', 'for_s_user':False}
        ]
menu_staff = [{'title': "Home", 'url_name': 'main_page_staff', 'for_s_user':True},
        {'title': "Bookings", 'url_name': 'booking_staff', 'for_s_user':True},
          {'title': "Reviews", 'url_name': 'reviews_staff', 'for_s_user':True},
        {'title': "Incoming inquiries", 'url_name': 'inquiries', 'for_s_user':True}
        ]
class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu 
        return context