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
        title = TextMobject("Classical approach")
        self.play(FadeIn(title))
        self.play(ApplyMethod(title.move_to, 2.4*UP))

        el = Elbow(width = 1)
        numerator = TexMobject("1", "3", "4")
        denominator = TexMobject("8")

        el.flip()
        numerator.move_to(el.get_center())
        group = VGroup(el, numerator)
        denominator.next_to(group, direction=LEFT)

        self.play(Write(group), Write(denominator))

        self.play(ApplyMethod(numerator[0].set_color, RED))

        self.play(ApplyMethod(numerator[1].set_color, RED))

        by_two = TexMobject(r"8 \times 2 = 16")

        by_two.next_to(group, direction=2*RIGHT + 2*UP)

        self.play(Write(by_two))

        one = TexMobject("1")
        one.match_x(numerator[1])
        one.next_to(el, UP)
        self.play(Write(one))

        eight = TexMobject("8")
        eight.match_x(one)
        eight.next_to(numerator, DOWN)
        self.play(Write(eight))

        hbar = Line()
        #hbar.match_x(eight)
        hbar.next_to(eight, DOWN).scale(0.4)
        self.play(Write(hbar))

        five = TexMobject("5")
        five.match_x(eight)
        five.next_to(hbar, DOWN)
        self.play(Write(five))

        four = TexMobject("4")
        four.match_x(numerator[2])
        four.match_y(five)

        l_dashed = DashedLine(numerator[2].get_bottom(), four.get_top(), buff=SMALL_BUFF)

        self.play(Write(four), Write(l_dashed))

















        # color first digit red of 134
