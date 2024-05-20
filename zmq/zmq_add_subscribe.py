import zmq
import time

context = zmq.Context()

# receive on socket 5555

subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://localhost:5555")
subscriber.setsockopt_string(zmq.SUBSCRIBE, '')

# send on socket 5556
sender = context.socket(zmq.PUB)
sender.bind("tcp://*:5556")
time.sleep(1)

def add_numners_and_return() -> None:
	"""adds numbers from publisher and returns sum
	"""
	while True:
		message = subscriber.recv_string()
		a, b = map(int, message.split())
		sum_result = a + b
		print(f"Received numbers: {a}, {b}")
		print(f"Sum: {sum_result}")
		sender.send_string(f"{sum_result}")
		print(f"Sent result: {sum_result}")

if __name__ == "__main__":
	add_numners_and_return()
