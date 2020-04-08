##PI pattern on line 2-12 (indentation)
def get_random_score(self):
    score = 1
    radius = 1
    while True:
        point = np.random.uniform(-1, 1, size=2)
        hit_radius = get_norm(point)
        if hit_radius > radius:
            return score
        else:
            score += 1
            radius = np.sqrt(radius**2 - hit_radius**2)