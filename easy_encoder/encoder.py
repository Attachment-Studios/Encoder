# Encoder Extensions

# modules
import random

# classes
class Encoder:
	def __init__(self, *args, **options):
		self.decoded = options['decoded_chars'] if 'decoded_chars' in options else ''
		self.encoded = options['encoded_chars'] if 'encoded_chars' in options else ''

		self.process = options['process'] if 'process' in options else ''

		self.token_limit = options['token_limit'] if 'token_limit' in options else 5
		self.min_data_length = options['min_data_length'] if 'min_data_length' in options else 5
	
	def encode(self, data:str) -> str:
		if len(data) < self.min_data_length:
			return None
		
		encoded_data = data

		for instruction in self.process.split(';'):
			if len(instruction) > 0:
				if instruction[0] == "N":
					partial_data = ""
					for char in encoded_data:
						if char in self.decoded:
							partial_data += self.encoded[self.decoded.index(char)]
						else:
							partial_data += char
					encoded_data = partial_data
				if instruction[0] == "R":
					encoded_data = encoded_data[::-1]
				if instruction[0] == "S":
					args = instruction.split('[')
					if len(args) == 1:
						pass
					else:
						args = args[1].split(':')
						if len(args) < 2:
							pass
						else:
							encoded_data = encoded_data[int(args[1]):] + encoded_data[int(args[0]):int(args[1])]
		
		return encoded_data
	
	def decode(self, data:str) -> str:
		if len(data) < self.min_data_length:
			return None
		
		decoded_data = data

		for instruction in self.process.split(';')[::-1]:
			if len(instruction) > 0:
				if instruction[0] == "N":
					partial_data = ""
					for char in decoded_data:
						if char in self.encoded:
							partial_data += self.decoded[self.encoded.index(char)]
						else:
							partial_data += char
					decoded_data = partial_data
				if instruction[0] == "R":
					decoded_data = decoded_data[::-1]
				if instruction[0] == "S":
					args = instruction.split('[')
					if len(args) == 1:
						pass
					else:
						args = args[1].split(':')
						if len(args) < 2:
							pass
						else:
							decoded_data = decoded_data[-(int(args[1]) - int(args[0])):] + decoded_data[:-(int(args[1]) - int(args[0]))]
		
		return decoded_data

	def token(self, data:str) -> str:
		if len(data) < self.min_data_length:
			return None
		
		token = data

		token = self.encode(data)[-self.token_limit:]
		token = self.encode(token)
		
		return token
	
	def random_encode_chars(self):
		encoded_set = self.decoded[:1]
		for char in self.decoded[1:]:
			index = random.randint(0, len(encoded_set) - 1)
			encoded_set = encoded_set[:index] + char + encoded_set[index:]
		
		return encoded_set

	def random_process(self):
		process = ""
		ins = [
			'N',
			'S',
			'R'
		]
		length = random.randint(3, 15)

		for _ in range(length):
			instruction = ins[random.randint(0, len(ins) - 1)]
			args = []

			if instruction == "S":
					args.append(random.randint(0, 3))
					args.append(random.randint(args[-1], args[-1] + 5))

			partial_args = []
			for arg in args:
				partial_args.append(str(arg))

			args = partial_args
			
			process += f"{instruction}[{':'.join(args)};"

		return process

