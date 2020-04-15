def setup_surface(self):
        axes = self.axes
        k = self.k

        # Parameters for surface function
        initial_As = [2] + [
            0.8 * random.choice([-1, 1]) / n
            for n in range(1, 20)
        ]
        A_trackers = Group(*[
            ValueTracker(A)
            for A in initial_As
        ])

        def get_As():
            return [At.get_value() for At in A_trackers]

        omegas = [n / 2 for n in range(0, 10)]

        def func(x, t):
            return np.sum([
                np.prod([
                    A * np.cos(omega * x),
                    np.exp(-k * omega**2 * t)
                ])
                for A, omega in zip(get_As(), omegas)
            ])

        # Surface and graph
        surface = always_redraw(
            lambda: self.get_surface(axes, func)
        )
        t_tracker = ValueTracker(0)
        graph = always_redraw(
            lambda: self.get_time_slice_graph(
                axes, func, t_tracker.get_value(),
            )
        )

        surface.suspend_updating()
        graph.suspend_updating()

        self.surface_func = func
        self.surface = surface
        self.graph = graph
        self.t_tracker = t_tracker
        self.A_trackers = A_trackers
        self.omegas = omegas