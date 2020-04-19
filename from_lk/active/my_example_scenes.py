#!/usr/bin/env python

from manimlib.imports import *

class Intro(Scene):
    def construct(self):
        #self.intro()
        self.fix_long_division()

    def intro(self):
        title = TextMobject("Long Division")
        sub = TextMobject("You've been doing it wrong all along...")

        self.play(Write(title), run_time = 2)
        self.play(title.move_to, UP, run_time = 2)
        self.play(FadeIn(sub), run_time = 2)

        self.wait()

        self.play(FadeOut(title), FadeOut(sub), run_time = 2)

    def fix_long_division(self):
        # setup mobjects
        title = TextMobject("Classical approach")
        el = Elbow(width = 1)
        numr = TexMobject("1", "3", "4")
        denom = TexMobject("8")
        soln = TexMobject("1", "6", ".", "7", "5")
        #tail = TexMobject("8", "54", "48", "60", "56", "40", "40", "0")
        tail_1 = TexMobject("5", "4")
        tail_2 = TexMobject("4", "8")
        tail_3 = TexMobject("6", "0")
        tail_4 = TexMobject("5", "6")
        tail_5 = TexMobject("4", "0")
        tail_6 = TexMobject("0")
        mult_table = TexMobject(r"2 \times 8 = 16 \\ 3 \times 8 = 24 \\ 4 \times 8 = 32 \\ 5 \times 8 = 40 \\ 6 \times 8 = 48 \\ 7 \times 8 = 56")

        # arrange mobjects
        el.flip()
        numr.move_to(el.get_center())
        denom.next_to(el, direction=LEFT)
        soln.next_to(el, direction=UP)
        mult_table.to_edge(RIGHT).scale(0.8)

        # grouping
        group = VGroup(el, numr, denom)

        group.move_to(2.4*UP)

        # arrange tail
        head = TexMobject("8")
        head.match_x(numr[1])
        head.next_to(numr, DOWN)

        underline = Line()
        underline.match_width(tail_1)
        underline.next_to(head, DOWN, MED_SMALL_BUFF, aligned_edge = RIGHT)
        head.add(underline)

        tail_1.align_to(head, direction=LEFT, alignment_vect=LEFT )
        #tail_1.match_x(head)
        tail_1.next_to(head, aligned_edge=LEFT, direction=DOWN+RIGHT*head.get_width()*2)
        tail_2.next_to(tail_1, aligned_edge=LEFT, direction=DOWN)

        underline2 = underline.copy()
        underline2.next_to(tail_2, DOWN, MED_SMALL_BUFF, aligned_edge = RIGHT)
        tail_2.add(underline2)

        tail_3.next_to(tail_2, aligned_edge=LEFT, direction=DOWN)
        tail_3.align_to(tail_2[1], direction=LEFT, alignment_vect=RIGHT )
        tail_4.next_to(tail_3, aligned_edge=LEFT, direction=DOWN)

        underline3 = underline.copy()
        underline3.next_to(tail_4, DOWN, MED_SMALL_BUFF, aligned_edge = RIGHT)
        tail_4.add(underline3)

        tail_5.next_to(tail_4, aligned_edge=LEFT, direction=DOWN)
        tail_5.align_to(tail_4[1], direction=LEFT, alignment_vect=RIGHT )
        tail_5_cp = tail_5.copy()
        tail_5_cp.next_to(tail_5, aligned_edge=LEFT, direction=DOWN)

        underline4 = underline.copy()
        underline4.next_to(tail_5_cp, DOWN, MED_SMALL_BUFF, aligned_edge = RIGHT)
        tail_5_cp.add(underline4)

        tail_6.next_to(tail_5_cp, aligned_edge=LEFT, direction=DOWN)
        tail_6.align_to(tail_5_cp[1], direction=LEFT, alignment_vect=RIGHT )

        soln.match_x(numr[1])
        soln.next_to(el, UP)
        group.add(soln)

        # animations
        #self.play(FadeIn(title))
        #self.play(ApplyMethod(title.move_to, 2.4*UP))



        self.play(Write(group))
        #self.play(Write(mult_table))
        self.play(Write(head), Write(tail_1), Write(tail_2), Write(tail_3),
        Write(tail_4), Write(tail_5), Write(tail_5_cp), Write(tail_6))



        self.wait(10)





    def long_division(self):
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

        by_two.next_to(group, direction=4*RIGHT + 2*UP)

        self.play(Write(by_two))

        one = TexMobject("1")
        one.match_x(numerator[1])
        one.next_to(el, UP)
        self.play(Write(one))

        eight = TexMobject("8")
        eight.match_x(one)
        eight.next_to(numerator, DOWN)
        self.play(Write(eight))

        hbar = Line(numerator[0].get_left(),numerator[2].get_left())#.match_y(numerator[0], LEFT)
        #hbar.next_to(eight, DOWN)#.match_x(numerator[0]).scale(1.5)
        hbar.shift(numerator[0].get_height() * DOWN * 3)
        self.play(Write(hbar)) #, run_time=0.3)

        five = TexMobject("5")

        five.next_to(hbar, DOWN).match_x(eight)
        self.play(Write(five))

        #self.wait(10)
        #return
        four = TexMobject("4")
        four.match_x(numerator[2])
        four.match_y(five)

        l_dashed = DashedLine(numerator[2].get_bottom(), four.get_top(), buff=SMALL_BUFF)

        self.play(Write(l_dashed))

        self.play(Write(four))

        by_six = TexMobject(r"8 \times 6 = 48")
        by_six.next_to(by_two, DOWN)
        self.play(Write(by_six))

        by_seven = TexMobject(r"8 \times 7 = 56")
        by_seven.next_to(by_six, DOWN)
        self.play(Write(by_seven))

        self.play(ApplyMethod(by_seven.set_color, RED))
        self.play(ApplyMethod(by_six.set_color, GREEN))

        one = TexMobject("1")
        one.match_x(numerator[1])
        one.next_to(el, UP)
        self.play(Write(one))

        self.wait(10)













        # color first digit red of 134
