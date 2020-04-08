def false_compliment(self):
        friend = self.friends[0]
        bubble = SpeechBubble(
            height = 1.25, width = 4.5, direction = RIGHT,
            fill_opacity = 0,
        )
        content = TextMobject("The beat was consistent.")
        content.scale(0.75)
        bubble.add_content(content)
        VGroup(bubble, content).next_to(friend, LEFT, SMALL_BUFF)
        VGroup(bubble, content).to_edge(UP, SMALL_BUFF)

        self.play(
            friend.change_mode, "maybe",
            ShowCreation(bubble),
            Write(content)
        )
        self.change_pi_creature_with_guitar("happy")
        self.wait()
        self.play(*list(map(FadeOut, [bubble, content])))

        self.bubble = bubble