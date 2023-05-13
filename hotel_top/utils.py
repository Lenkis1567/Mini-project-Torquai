menu = [{'title': "Home", 'url_name': 'main_page_path', 'for_s_user':False},
        {'title': "Search the room", 'url_name': 'search_path', 'for_s_user':False},
        # {'title': "Add Director", 'url_name': 'add_director_path', 'for_s_user':True},
        # {'title': "Favorites", 'url_name': 'favorites_path', 'for_s_user':True}
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu 
        return context