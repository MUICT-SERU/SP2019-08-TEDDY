###NPI Pattern on line 51-75
def show_lighthouses_on_number_line(self):

        self.number_line = NumberLine(
            x_min = 0,
            color = WHITE,
            number_at_center = 1.6,
            stroke_width = 1,
            numbers_with_elongated_ticks = list(range(1,5)),
            numbers_to_show = list(range(1,5)),
            unit_size = 2,
            tick_frequency = 0.2,
            line_to_number_buff = LARGE_BUFF,
            label_direction = UP,
        )

        self.number_line.label_direction = DOWN

        self.number_line_labels = self.number_line.get_number_mobjects()
        self.add(self.number_line,self.number_line_labels)
        self.wait()

        origin_point = self.number_line.number_to_point(0)

        self.default_pi_creature_class = Randolph
        randy = self.get_primary_pi_creature()

        randy.scale(0.5)
        randy.flip()
        right_pupil = randy.pupils[1]
        randy.next_to(origin_point, LEFT, buff = 0, submobject_to_align = right_pupil)



        light_indicator = LightIndicator(radius = INDICATOR_RADIUS,
            opacity_for_unit_intensity = OPACITY_FOR_UNIT_INTENSITY,
            color = LIGHT_COLOR)
        light_indicator.reading.scale(0.8)

        bubble = ThoughtBubble(direction = RIGHT,
                            width = 2.5, height = 3.5)
        bubble.next_to(randy,LEFT+UP)
        bubble.add_content(light_indicator)
        self.wait()
        self.play(
            randy.change, "wave_2",
            ShowCreation(bubble),
            FadeIn(light_indicator)
        )

        light_sources = []


        euler_sum_above = TexMobject("1", "+", "{1\over 4}", 
            "+", "{1\over 9}", "+", "{1\over 16}", "+", "{1\over 25}", "+", "{1\over 36}")

        for (i,term) in zip(list(range(len(euler_sum_above))),euler_sum_above):
            #horizontal alignment with tick marks
            term.next_to(self.number_line.number_to_point(0.5*i+1),UP,buff = 2)
            # vertical alignment with light indicator
            old_y = term.get_center()[1]
            new_y = light_indicator.get_center()[1]
            term.shift([0,new_y - old_y,0])
            


        for i in range(1,NUM_CONES+1):
            light_source = LightSource(
                opacity_function = inverse_quadratic(1,AMBIENT_SCALE,1),
                num_levels = NUM_LEVELS,
                radius = AMBIENT_RADIUS,
            )
            point = self.number_line.number_to_point(i)
            light_source.move_source_to(point)
            light_sources.append(light_source)

        self.wait()
        for ls in light_sources:
            self.add_foreground_mobject(ls.lighthouse)

        light_indicator.set_intensity(0)

        intensities = np.cumsum(np.array([1./n**2 for n in range(1,NUM_CONES+1)]))
        opacities = intensities * light_indicator.opacity_for_unit_intensity

        self.remove_foreground_mobjects(light_indicator)


        # slowly switch on visible light cones and increment indicator
        for (i,light_source) in zip(list(range(NUM_VISIBLE_CONES)),light_sources[:NUM_VISIBLE_CONES]):
            indicator_start_time = 1.0 * (i+1) * SWITCH_ON_RUN_TIME/light_source.radius * self.number_line.unit_size
            indicator_stop_time = indicator_start_time + INDICATOR_UPDATE_TIME
            indicator_rate_func = squish_rate_func(
                smooth,indicator_start_time,indicator_stop_time)
            self.play(
                SwitchOn(light_source.ambient_light),
                FadeIn(euler_sum_above[2*i], run_time = SWITCH_ON_RUN_TIME,
                    rate_func = indicator_rate_func),
                FadeIn(euler_sum_above[2*i - 1], run_time = SWITCH_ON_RUN_TIME,
                    rate_func = indicator_rate_func),
                # this last line *technically* fades in the last term, but it is off-screen
                ChangeDecimalToValue(light_indicator.reading,intensities[i],
                    rate_func = indicator_rate_func, run_time = SWITCH_ON_RUN_TIME),
                ApplyMethod(light_indicator.foreground.set_fill,None,opacities[i],
                    rate_func = indicator_rate_func, run_time = SWITCH_ON_RUN_TIME)
            )

            if i == 0:
                self.wait()
                # move a copy out of the thought bubble for comparison
                light_indicator_copy = light_indicator.copy()
                old_y = light_indicator_copy.get_center()[1]
                new_y = self.number_line.get_center()[1]
                self.play(
                    light_indicator_copy.shift,[0, new_y - old_y,0]
                )

            self.wait()

        self.wait()

        # quickly switch on off-screen light cones and increment indicator
        for (i,light_source) in zip(list(range(NUM_VISIBLE_CONES,NUM_CONES)),light_sources[NUM_VISIBLE_CONES:NUM_CONES]):
            indicator_start_time = 0.5 * (i+1) * FAST_SWITCH_ON_RUN_TIME/light_source.radius * self.number_line.unit_size
            indicator_stop_time = indicator_start_time + FAST_INDICATOR_UPDATE_TIME
            indicator_rate_func = squish_rate_func(#smooth, 0.8, 0.9)
                smooth,indicator_start_time,indicator_stop_time)
            self.play(
                SwitchOn(light_source.ambient_light, run_time = FAST_SWITCH_ON_RUN_TIME),
                ChangeDecimalToValue(light_indicator.reading,intensities[i-1],
                    rate_func = indicator_rate_func, run_time = FAST_SWITCH_ON_RUN_TIME),
                ApplyMethod(light_indicator.foreground.set_fill,None,opacities[i-1])
            )


        # show limit value in light indicator and an equals sign
        limit_reading = TexMobject("{\pi^2 \over 6}")
        limit_reading.move_to(light_indicator.reading)

        equals_sign = TexMobject("=")
        equals_sign.next_to(randy, UP)
        old_y = equals_sign.get_center()[1]
        new_y = euler_sum_above.get_center()[1]
        equals_sign.shift([0,new_y - old_y,0])

        self.play(
            FadeOut(light_indicator.reading),
            FadeIn(limit_reading),
            FadeIn(equals_sign),
        )

            

        self.wait()