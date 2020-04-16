#!/usr/bin/env python

from manimlib.imports import *

class Play(Scene):
    def construct(self):
        c = Circle()
        e = Ellipse()
        r = Rectangle()
        a = Arc(angle = 1/4 * TAU)
        asec = AnnularSector()
        an = Annulus()
        t = Triangle()

        self.play(ShowCreation(c))

        group_a = VGroup(c, e, r, a)
        group_b = VGroup(asec, an, t)
        group_a.arrange(LEFT)

        self.play(FadeIn(group_a))
        self.play(FadeOut(group_a))

        self.play(FadeIn(group_b))
        self.play(FadeOut(group_b))

        l = Line()
        el = Elbow()
        ar = Arrow()
        v = Vector(direction = LEFT)

        lgroup = VGroup(l, el, ar, v)
        lgroup.arrange(DOWN)
        self.play(FadeIn(lgroup))



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
        self.play(ApplyMethod(title.move_to, 2*UP))

        # hline = Line(color=RED)
        # vline = Line(LEFT, DOWN + LEFT, color=RED)
        el = Elbow(width = 1)
        el.flip()
        numerator = TexMobject(r"367")
        group_a = VGroup(el, numerator)
        group_a.arrange(LEFT)

        denominator = TexMobject(r"4")

        self.play(FadeIn(group_a))
