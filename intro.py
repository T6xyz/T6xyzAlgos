from manim import *

# Intro scene for T6xyzAlgos
# Created on 4/29/2024 at 9:01 pm EST
# Input: Scene s
# void (no return)
def playIntro(s):
    c2 = Circle(2, color=LIGHT_GREY, fill_opacity=0.1)
    s.play(DrawBorderThenFill(c2), run_time=0.5)

    title = Text("T6xyz", font_size=72, slant="ITALIC").shift(UP * 0.3)
    subtitle = Text("Algos", slant="ITALIC").shift(DOWN * 0.5)
    s.play(Write(title), Write(subtitle))

    a = Arc(2.2, TAU * 0.25, -TAU * 2.6 / 4, color=BLUE, stroke_width=15)
    s.play(Create(a))

    s.wait(3)