from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

Builder.load_string("""
<MyTextField>
    text_color_normal: app.colors.black
    text_color_focus: app.colors.black
    hint_text_color_normal: app.colors.black
    hint_text_color_focus: app.colors.black
    # font_name_hint_text: app.fonts.body
    line_color_normal: app.colors.primary
    line_color_focus: app.colors.black
    icon_right_color_normal: app.colors.black
    icon_right_color_focus: app.colors.black
    input_type: "text"
    # font_name: app.fonts.subheading
    mode: "fill"
    radius: [25,0,25,0]
    size_hint_x: .8
    active_line: False
    helper_text_mode: "on_error"
    on_text: print(self.text)
    fill_color_normal: app.colors.white
""")


class MyTextField(MDTextField):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
