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

class TexPlay(Scene):
    def construct(self):
        digits = TexMobject("1", "2", "3")
        self.play(DrawBorderThenFill(digits))

        digits.set_color_by_tex("1", RED)

        self.play(ApplyMethod(digits.set_color_by_tex, "1", RED))
