import os, commands, logging

__all__=['get_config']

def get_config():
    return dict(
        VERSION=commands.getoutput("cat VERSION"),
        LOGFILE=os.path.join(log_dir(), 'log', 'sqor_sass_rest.log'),
        LOGLEVEL=logging.INFO,
        DEBUG=True,
        ATTACH_TO_ALL='0.0.0.0'
    )

def log_dir():
    #return os.get_cwd()
    return "/var/log"
