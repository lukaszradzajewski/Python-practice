import os


def get_base_url():
    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return 'http://localhost/quicksite'
    elif env.lower() == 'prod':
        return 'http://localhost/quicksite'
    else:
        raise Exception(f"Unknown environment :{env}")
