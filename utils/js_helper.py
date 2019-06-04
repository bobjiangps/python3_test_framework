class JSHelper:

    @property
    def scroll_into_view(self):
        return "arguments[0].scrollIntoView(true);"

    @property
    def scroll_up_to_top_of_page(self):
        return "window.scrollTo(0, 0);"

    @property
    def scroll_down_to_bottom_of_page(self):
        return "window.scrollBy(0,document.body.scrollHeight);"
