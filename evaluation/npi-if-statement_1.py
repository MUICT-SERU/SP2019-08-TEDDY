##NPI pattern on line 13, 23
def split_light_source(i, step, show_steps = True, run_time = 1):

            ls_new_loc1 = position_for_index(i,step + 1)
            ls_new_loc2 = position_for_index(i + 2**step,step + 1)

            hyp = VMobject()
            hyp1 = Line(self.lake_center,ls_new_loc1)
            hyp2 = Line(self.lake_center,ls_new_loc2)
            hyp.add(hyp2,hyp1)
            self.new_hypotenuses.append(hyp)

            if show_steps == True:
                self.play(
                    ShowCreation(hyp, run_time = run_time)
                )

            leg1 = Line(self.obs_dot.get_center(),ls_new_loc1)
            leg2 = Line(self.obs_dot.get_center(),ls_new_loc2)
            self.new_legs_1.append(leg1)
            self.new_legs_2.append(leg2)

            if show_steps == True:
                self.play(
                    ShowCreation(leg1, run_time = run_time),
                    ShowCreation(leg2, run_time = run_time),
                )

            ls1 = self.light_sources_array[i]


            ls2 = ls1.copy()
            self.add(ls2)
            self.additional_light_sources.append(ls2)

            # check if the light sources are on screen
            ls_old_loc = np.array(ls1.get_source_point())
            onscreen_old = np.all(np.abs(ls_old_loc[:2]) < 10 ** 2**step)
            onscreen_1 = np.all(np.abs(ls_new_loc1[:2][:2]) < 10 ** 2**step)
            onscreen_2 = np.all(np.abs(ls_new_loc2[:2]) < 10 ** 2**step)
            show_animation = (onscreen_old or onscreen_1 or onscreen_2)

            if show_animation:
                print("animating (", i, ",", step, ")")
                self.play(
                    ApplyMethod(ls1.move_source_to,ls_new_loc1, run_time = run_time),
                    ApplyMethod(ls2.move_source_to,ls_new_loc2, run_time = run_time),
                )
            else:
                ls1.move_source_to(ls_new_loc1)
                ls2.move_source_to(ls_new_loc1)