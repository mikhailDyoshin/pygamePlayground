def get_data_from_file(file_name: str) -> tuple[list[float], list[float], list[float]]:
    population: list[float] = []
    speed: list[float] = []
    vision: list[float] = []

    with open(file_name) as f:
        for line in f:
            p, s, v = map(float, line.split())
            population.append(p)
            speed.append(s)
            vision.append(v)

    return (population, speed, vision)
