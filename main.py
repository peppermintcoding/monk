from pyray import (
    VIOLET,
    WHITE,
    begin_drawing,
    clear_background,
    close_window,
    draw_text,
    end_drawing,
    init_window,
    window_should_close,
)

init_window(800, 450, "Hello")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_text("Hello world", 190, 200, 20, VIOLET)
    end_drawing()
close_window()
