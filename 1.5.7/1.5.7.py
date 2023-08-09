class Graph():
    def __init__(self, data):
        self.data = list(data)
        self.is_show = True
    
    def set_data(self, data):
        self.data = list(data)

    def show_table(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print(" ".join(self.data))
    
    def show_graph(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print("Графическое отображение данных: ", " ".join(self.data))
    def show_bar(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            string_data = " ".join(map(str, self.data))
            print(f"Столбчатая диаграмма: {string_data}")

    def set_show(self, fl_show=True):
        self.is_show = fl_show


# data_graph = list(map(int, input().split()))
data_graph = [8, 11, 10, -32, 0, 7, 18]


gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()