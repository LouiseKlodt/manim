#!/usr/bin/env python

from manimlib.imports import *

class Intro(Scene):
    def construct(self):
        #self.intro()
        self.long_division()

    def intro(self):
        title = TextMobject("Long Division")
        sub = TextMobject("You've been doing it wrong all along...")

        self.play(Write(title), run_time = 2)
        self.play(ApplyMethod(title.move_to, UP), run_time = 2)
        self.play(FadeIn(sub), run_time = 2)

        self.wait()

        self.play(FadeOut(title), FadeOut(sub), run_time = 2)

    def long_division(self):
        """Animates the classical long division approach."""
        title = TextMobject("Classic approach")
        self.play(FadeIn(title))
        self.play(ApplyMethod(title.move_to, 3*UP))

        el = Elbow(width = 1)
        numerator = TexMobject("134")
        denominator = TexMobject("8")

        el.flip()
        numerator.move_to(el.get_center())
        group = VGroup(el, numerator)
        denominator.next_to(group, direction=LEFT)

        self.play(Write(group), Write(denominator))

        #numerator[0].set_color(color = RED)

        self.play(ApplyMethod(numerator[0].set_color, RED))

        # color first digit red of 134
