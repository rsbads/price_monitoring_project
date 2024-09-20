from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database


def refresh_table():
    for item in tree.get_children():
        tree.delete(item)
    products = database.get_all_products()
    for product in products:
        tree.insert("", "end", values=product)



def insert_product():
    product_name = entry_name.get()
    product_type = entry_type.get()
    price = entry_price.get()
    url = entry_url.get()

    if not product_name or not product_type:
        messagebox.showerror("Erro", "Nome do produto e tipo são obrigatórios")
        return

    database.insert_row(product_name, product_type, price, url)
    refresh_table()

    entry_name.delete(0, END)
    entry_type.delete(0, END)
    entry_price.delete(0, END)
    entry_url.delete(0, END)



def edit_product():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror("Erro", "Selecione um produto para editar")
        return

    product_data = tree.item(selected_item, "values")
    product_id = product_data[0]
    product_name = entry_name.get()
    product_type = entry_type.get()
    price = entry_price.get()
    url = entry_url.get()

    if not product_name or not product_type:
        messagebox.showerror("Erro", "Nome do produto e tipo são obrigatórios")
        return

    database.update_row(product_id, product_name, product_type, price, url)
    refresh_table()



def delete_product():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror("Erro", "Selecione um produto para remover")
        return

    product_data = tree.item(selected_item, "values")
    product_id = product_data[0]

    database.delete_row(product_id)
    refresh_table()


database.create_table()



root = Tk()
root.title("Monitoramento de preços")



frame = LabelFrame(root, text="Produto", padx=10, pady=10)
frame.pack(padx=10, pady=10)



label_name = Label(frame, text="Nome do produto")
label_name.grid(row=0, column=0)
entry_name = Entry(frame)
entry_name.grid(row=0, column=1)

label_type = Label(frame, text="Tipo do produto")
label_type.grid(row=1, column=0)
entry_type = Entry(frame)
entry_type.grid(row=1, column=1)

label_price = Label(frame, text="Preço (Opcional)")
label_price.grid(row=2, column=0)
entry_price = Entry(frame)
entry_price.grid(row=2, column=1)

label_url = Label(frame, text="URL do produto (Opcional)")
label_url.grid(row=3, column=0)
entry_url = Entry(frame)
entry_url.grid(row=3, column=1)



btn_add = Button(frame, text="Adicionar Produto", command=insert_product)
btn_add.grid(row=4, column=0, pady=10)

btn_edit = Button(frame, text="Editar Produto", command=edit_product)
btn_edit.grid(row=4, column=1, pady=10)

btn_delete = Button(frame, text="Remover Produto", command=delete_product)
btn_delete.grid(row=4, column=2, pady=10)



tree_frame = Frame(root)
tree_frame.pack(padx=10, pady=10)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, columns=("ID", "Nome", "Tipo", "Preço", "URL"), show="headings")
tree.pack()

tree_scroll.config(command=tree.yview)



tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Tipo", text="Tipo")
tree.heading("Preço", text="Preço")
tree.heading("URL", text="URL")

tree.column("ID", width=50)
tree.column("Nome", width=150)
tree.column("Tipo", width=100)
tree.column("Preço", width=100)
tree.column("URL", width=200)



refresh_table()

root.mainloop()
