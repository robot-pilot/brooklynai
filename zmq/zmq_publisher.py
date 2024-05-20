import zmq
import time

context = zmq.Context()

# send messages on 5555
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://*:5555")
time.sleep(1)

# receive messages on 5556
receiver = context.socket(zmq.SUB)
receiver.connect("tcp://localhost:5556")
receiver.setsockopt_string(zmq.SUBSCRIBE, '')

def send_numbers(a: int, b:int) -> None:
	"""send numners to maths
	
	Args:
		a (int): first int to add
		b (int): second int to add
	"""

	publisher.send_string(f"{a} {b}")
	print(f"Sent numbers: {a} {b}")

def receive_sum():
	"""receives the sum and prints
	"""
	print("hello")
	try:
		print('yo')
		sum_result = receiver.recv_string(flags=zmq.NOBLOCK)
		print(f"Received sum: {sum_result}")
		return sum_result
	except zmq.Again:
		print("No sum yet")
		return None

if __name__ == "__main__":
	while True:
		a, b = 3, 5
		send_numbers(a, b)
		time.sleep(1)
		while True:
			print('hi')
			sum_result = receive_sum()
			print(sum_result)
			if sum_result is not None:
				break
			time.sleep(1)
		time.sleep(5)
