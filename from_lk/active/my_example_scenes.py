#!/usr/bin/env python

from manimlib.imports import *

class FirstExample(Scene):
    def construct(self):
        circle = Circle()
        #self.play(ShowCreation(circle))
        #self.add(circle)
        self.play(ShowCreation(circle))

class LongDivision(Scene):
    def construct(self):
        title = TextMobject("Long Division")
        sub = TextMobject("You've been doing it wrong all along")

        VGroup(title, sub).arrange(DOWN)

        self.play(
            FadeIn(title)
        )

        #self.wait()

        self.play(
            FadeIn(sub)
        )



    #self.wait()
