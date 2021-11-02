from configure import Button, Label, Frame, Entry, LabelFrame


class SuggestionView(Frame):
    def __init__(self, callback_user, callback_add_suggestion, callback_view_suggestion):
        super(SuggestionView, self).__init__()
        self.callback_add_sug = callback_add_suggestion
        self.callback_list_sug = callback_view_suggestion
        self.callback_user = callback_user








