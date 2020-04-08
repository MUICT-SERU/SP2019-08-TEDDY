class AskWhyRewriteIt(TeacherStudentsScene):
    def construct(self):
        self.student_says(
            "Why?", student_index=1,
            bubble_kwargs={"height": 2, "width": 2},
        )
        self.students[1].bubble = None
        self.teacher_says(
            "One step closer\\\\to derivatives"
        )
        self.change_student_modes(
            "thinking", "thinking", "thinking",
            look_at_arg=4 * LEFT + 2 * UP
        )
        self.wait(2)
