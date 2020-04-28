try:
    import queue  # Python3
except ImportError:
    import Queue as queue  # Python 2

#Instantiate a queue for the handler/listener
slack_queue = queue.Queue(-1)
