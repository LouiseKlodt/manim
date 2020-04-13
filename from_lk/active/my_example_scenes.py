#!/usr/bin/env python

from manimlib.imports import *

# class FirstExample(Scene):
#     def construct(self):
#         circle = Circle()
#         #self.play(ShowCreation(circle))
#         #self.add(circle)
#         self.play(ShowCreation(circle))

class Intro(Scene):
    def construct(self):
        title = TextMobject("Long Division")
        title.to_edge(UP)

        sub_title = TextMobject("You've been doing it wrong all along")

        VGroup(title, sub_title).arrange(DOWN)

        self.play(
            Write(title, run_time = 4)
        )
        self.play(
            FadeIn(sub_title, run_time = 4)
        )


class OldMethod(Scene):
    def construct(self):
        line = Line(LEFT, RIGHT, color = RED, stroke_width = 7)

        vline = Line(LEFT, RIGHT - 2, color = RED, stroke_width = 7)

        self.play(Write(line))
        self.play(Write(vline))
