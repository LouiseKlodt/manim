#!/usr/bin/env python

from manimlib.imports import *

class Intro(Scene):
    def construct(self):
        self.intro()
        self.long_division()

    def intro(self):
        title = TextMobject("Long Division")
        sub = TextMobject("You've been doing it wrong all along...")

        self.play(Write(title), run_time = 2)
        self.play(ApplyMethod(title.move_to, UP), run_time = 2)
        self.play(Write(sub), run_time = 2)

        self.wait()

        self.play(FadeOut(title), FadeOut(sub), run_time = 2)

    def long_division(self):
        hline = Line(color=RED)
        vline = Line(LEFT, DOWN + LEFT, color=RED)
        self.play(Write(hline), Write(vline))
