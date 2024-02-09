import tkinter as tk

class HtmlEntrys:
    def __init__(self) -> None:
        self.main = ""
        self.editor = ""


    def init_windows(self):
        # Init the window for do html
        self._create_window()
        self._add_element()
        self._add_style()


    def _create_window(self):
        # Create the window for make the html
        self.main = tk.Toplevel()
        self.main.title('Number of legal')
        self.main.config(bg='#808080', width=200)


    def _add_element(self):
        # Place for set the how legals there are
        self.num_legal = tk.StringVar()
        self.num_legal.set('1')
        self.entry_legal = tk.Entry(self.main, textvariable=self.num_legal)
        self.button_save = tk.Button(self.main, text='Generate entrys', command=self.generate_entrys)


    def _add_style(self):
        # Add style for entrys
        style, position = self._set_parameters()
        self.entry_legal.grid(position, column=0)
        self.entry_legal.config(style)
        self.button_save.grid(position, column=1)
        self.button_save.config(style, fg='black')


    def _set_parameters(self):
        # Set parameters for style and position
        style = {
            'width':20,
            'bg':'#DCDCDC',
            'border':0
        }

        position = {
            'row':0,
            'padx':10,
            'pady':10
        }

        return style, position


    def generate_entrys(self):
        # Generate entrys for values that user put
        cuts_total = len(self.editor.save_imgs)
        num_legal = int(self.num_legal.get())
        self.values_img = self._add_entrys(cuts_total, 0)
        self.values_link = self._add_entrys(cuts_total, 1)
        self.values_legal= self._add_entrys(num_legal, 2)
        self._add_button(cuts_total+2)



    def _add_entrys(self, num_cuts, column):
        # Add entrys that numbers of cuts
        values = []
        for box_content in range(num_cuts):
                entry_val= tk.StringVar() #Guarda lo que ingresa en el campo
                entry_field = tk.Entry(self.main, textvariable=entry_val)
                entry_field.config(width=20, bg='#DCDCDC', border=0)
                entry_field.grid(row=box_content+1, column=column, padx=5, pady=5)
                values.append(entry_val)
        return values


    def _add_button(self, cuts_total):
        # Add button for do HTML final
        self.button_save = tk.Button(self.main, text='Make HTML')
        self.button_save.grid(row=cuts_total, column=0, columnspan=3, padx=5, pady=5)
        self.button_save.config(width=20)

