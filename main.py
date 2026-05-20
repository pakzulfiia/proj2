import flet as ft
from db import main_db

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column()

    filter_type = 'all'

    def load_tasks():
        task_list.controls.clear() #  всегда очищать перед добавлением
        tasks = main_db.get_tasks(filter_type=filter_type)
        if not tasks: 
            task_list.controls.append(ft.Text("Список задач пуст",color=ft.Colors.PURPLE_900))
        else:
            for task_id, task_text, complited in tasks:
                task_list.controls.append(view_tasks(
                    task_id=task_id, 
                    task_text=task_text,
                    complited=complited
                    ))

    
    def view_tasks(task_id, task_text, complited=None):

        check_box = ft.Checkbox(
            value=bool(complited), 
            on_change=lambda e: toggle_task(task_id=task_id, is_complited=e.control.value))
        
        def enable_edit(e):
            if task_field.read_only == True:
                task_field.read_only = False
            else:
                task_field.read_only = True

        def save_task(e):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True

        def delete_task_db(e):
            main_db.delete_task(task_id=task_id)
            task_list.controls.remove(task_row)


        delete_btn = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_task_db)
        saved_btn = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_task)
        task_field = ft.TextField(read_only=True, value=task_text, expand=True)
        edit_btn = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)

        task_row = ft.Row([check_box, task_field, edit_btn, saved_btn, delete_btn])
        return task_row

    def toggle_task(task_id, is_complited):
        print(is_complited)
        main_db.update_complited(
            task_id=task_id,
            complited=is_complited
        )


    def add_task_db(e):
        if task_input.value:
            task = task_input.value
            task_id = main_db.add_task(task=task)
            print(f'Задача {task} добавлена - его id {task_id}')
            task_list.controls.append(view_tasks(task_id=task_id, task_text=task))
            task_input.value = " "


    task_input = ft.TextField(label="Enter task: ", expand=True, on_submit=add_task_db)
    task_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_task_db)

    send_task = ft.Row([task_input, task_button])

    
    def thememode(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK

        else:
            page.theme_mode = ft.ThemeMode.LIGHT

    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    def delete_complited(e):
        main_db.delete_complited_task()
        load_tasks()

    def set_filter(filter_value):
        nonlocal filter_type 
        filter_type = filter_value
        load_tasks()

    delete_complited_btn = ft.ElevatedButton('Delete complited', on_click=delete_complited, 
                                             icon=ft.Icons.DELETE, icon_color=ft.Colors.PINK_900)

    filter_btns = ft.Row([
        ft.ElevatedButton('All tasks', on_click=lambda e: set_filter('all'), 
                          icon=ft.Icons.ALL_INBOX, icon_color=ft.Colors.BLACK_87),
        ft.ElevatedButton('Uncomplited', on_click=lambda e: set_filter('uncomplited'), 
                          icon=ft.Icons.WATCH, icon_color=ft.Colors.YELLOW_300),
        ft.ElevatedButton('Complited', on_click=lambda e: set_filter('complited'), 
                          icon=ft.Icons.CHECK_BOX, icon_color=ft.Colors.GREEN_900)
    ], alignment=ft.MainAxisAlignment.SPACE_AROUND)

    page.add(send_task, filter_btns, delete_complited_btn, theme_btn, task_list)
    load_tasks()

if __name__ == "__main__":
    main_db.init_db()
    ft.run(main, view=ft.AppView.WEB_BROWSER)