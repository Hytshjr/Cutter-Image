import tkinter as tk
from tkinter import messagebox as MessageBox


class HtmlEntrys:
    """The windows for make the html file"""

    def __init__(self, cuts_amount, send_user_input= None):
        self.__send_user_input_to_html_file = send_user_input
        self.__level_column_per_inputs = 0
        self.__cuts_amount = cuts_amount
        self.__amount_of_legal = None
        self.__window = None
        self.__disct_input = {}


    @property
    def level_column_per_inputs(self):
        """give the value of legal_amount in int"""

        return self.__level_column_per_inputs


    @property
    def amount_of_legal(self):
        """give the value of legal_amount in int"""

        return self.__amount_of_legal


    @property
    def cuts_amount(self):
        """give the value of private intance"""

        return self.__cuts_amount


    @property
    def window(self):
        """give the value of legal_amount in int"""

        return self.__window


    @property
    def disct_input(self):
        """give the value of legal_amount in int"""

        return self.__disct_input


    def init_windows(self):
        """Init the window for do html"""

        self.__create_window_for_user()
        self.__add_element_to_legal_amount()


    def __add_style_to_input(self, input_field, row, column):
        style, position = self.__set_parameters_style()
        input_field.grid(position, row=row, column=column)
        input_field.config(style)


    def __set_parameters_style(self):
        style = {
            'width':20,
            'bg':'#DCDCDC',
            'border':0
        }

        position = {
            'padx':8,
            'pady':8
        }

        return style, position


    def __create_window_for_user(self):
        self.__window = tk.Toplevel()
        self.__window.title('Number of legal')
        self.__window.config(bg='#808080', width=200)


    def __add_element_to_legal_amount(self):
        input_amount = tk.StringVar()
        input_amount.set('1')
        amount_of_legal = tk.Entry(self.window, textvariable=input_amount)
        self.__set_amount_of_legal(amount_of_legal)
        self.__add_style_to_input(amount_of_legal, row=0, column=0)

        text = 'Generate inputs'
        legal_button = tk.Button(self.window, text=text, command=self.__generate_inputs_for_links)
        self.__add_style_to_input(legal_button, row=0, column=1)


    def __set_amount_of_legal(self, amount_of_legal):
        self.__amount_of_legal =  amount_of_legal


    def __generate_inputs_for_links(self):
        value_amount_of_legal = self.__validate_value_amount_of_legal()
        if value_amount_of_legal is None:
            return

        cuts_amount = self.__cuts_amount
        self.disct_input['links_image'] = self.__add_inputs_per_column(cuts_amount, 0)
        self.disct_input['links_web'] = self.__add_inputs_per_column(cuts_amount, 1)
        self.disct_input['legals'] = self.__add_inputs_per_column(value_amount_of_legal, 2)
        self.__add_button_save_value_user_input(cuts_amount+2)


    def __validate_value_amount_of_legal(self):
        try:
            value_amount_of_legal = int(self.amount_of_legal.get())
            return value_amount_of_legal
        except ValueError:
            error = 'Enter only whole numbers.'
            show_error(error)
            return None


    def __add_inputs_per_column(self, amount_inputs, column):
        list_inputs = []
        column = self.level_column_per_inputs
        for box_content in range(amount_inputs):
            row = box_content + 1
            entry_field = tk.Entry(self.window, textvariable=tk.StringVar())
            self.__add_style_to_input(entry_field, row=row, column=column)
            list_inputs.append(entry_field)

        self.__update_level_column_per_inputs()
        return list_inputs


    def __update_level_column_per_inputs(self):
        self.__level_column_per_inputs += 1


    def __add_button_save_value_user_input(self, cuts_amount_total):
        button = tk.Button(self.window, text='Make HTML', command=self.__send_user_input_html_file)
        self.__add_style_to_input(button, row=cuts_amount_total, column=2)


    def __user_input_cleaned(self, list_user_input):
        list_user_input_cleaned = []
        for user_input in list_user_input:
            value = user_input.get()
            if value != "":
                list_user_input_cleaned.append(value)

        return list_user_input_cleaned


    def __send_user_input_html_file(self):
        links_image = self.__user_input_cleaned(self.disct_input['links_image'])
        links_web = self.__user_input_cleaned(self.disct_input['links_web'])
        legals = self.__user_input_cleaned(self.disct_input['legals'])
        user_input_cleaned = (links_image, links_web, legals) #be careful with the order
        self.__send_user_input_to_html_file(user_input_cleaned)



def show_error(message, note_user=None):
    """Show the error that we passed"""

    MessageBox.showwarning("Error", f"Error: {message} \n{note_user}")