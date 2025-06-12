import multiprocessing

WORKER_PER_CORE = 1
STARTING_PORT = 7001


def get_padding(mul) -> str:
    return mul * "  "


def get_django_targets() -> str:
    targets = ''
    cores = multiprocessing.cpu_count()
    workers_per_core = (WORKER_PER_CORE * 2) + 1
    default_web_concurrency = workers_per_core * cores
    t_port = STARTING_PORT
    for i in range(default_web_concurrency):
        targets += get_padding(5) + f'- "web:{t_port}"\n'
        t_port += 1
    return targets


def get_django_job() -> str:
    job_name = get_padding(1) + '- job_name: "django"\n'
    static_configs = get_padding(2) + 'static_configs:\n'
    targets = get_padding(3) + '- targets:\n'
    job = job_name + static_configs + targets + get_django_targets()
    return job


def load_base_config() -> str:
    with open('base_prom_config.yaml', 'r') as file:
        text = file.read()
    return text


def generate_prom_config() -> None:
    base = load_base_config()
    config = base + "\n" + get_django_job()
    with open('./prometheus/config/prometheus.yaml', 'w') as file:
        file.write(config)


if __name__ == '__main__':
    generate_prom_config()
