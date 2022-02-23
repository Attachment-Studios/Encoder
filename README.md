# Manual for Encoder Extension

## Product Information
```yaml
Name: EasyEncoder
Version: 2
Creator: Attachment Aditya
```

## License
```
MIT License

Copyright (c) 2022 Attachment Studios

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## About
This package is used for encoding and decoding texts with more safety.
It is simple to use and implement.

## How To Use
1. Import the library.
	> This step can be done manually as wished.
2. Set up the encoder in python file, where you will be using it.
	1. Create an instance of the class which will be used.
	2. Add customizations to the instance.
		1. `decoded_chars`(default=`''`, type=`str`)
		2. `encoded_chars`(default=`''`, type=`str`)
		3. `process`(default=`''`, type=`str`)
3. Use the encoder.
	1. Encoder instance will have some functions that can be used.

## Process
### Definations
- `N`: Normal Interchange: Swaps encoded characters and decoded characters for data.
- `S`: Stack Characters: Slices characters from data and moves to last.
- `R`: Reverse: Flips the data.

### Format
Process to be written in following order:

1. `Instruction`(letter)
2. `Arguments`
	1. Argument starts with `[` character.
	2. Separate arguments with `:` character.
3. `Ending`('`;`' character)

### Notes
- Process should be `One Liner`(in only one line).
- Process is one of the most important part and is suggested to be kept as `hidden` as possible.
- Process should be always `string`.
- Process needs to be ended with a `;`(semi-colon) character.
- First letter of each instruction(`instruction defination character`) is case sensitive.

## Example
### `Directory System`
```
-/(ROOT)
 |-main.py
 |-encoder.py
```

### `main.py`
```python
from encoder import Encoder
import os

enc = Encoder(
	decoded_chars = 'abcdefghijklmnopqrstuvwxyz',
	encoded_chars = os.getenv('ENCODED_CHARS'),
	process = os.getenv('PROCESS')
)

data = 'this is a test'

token = enc.token(data)
encoded_data = enc.encode(data)
decoded_data = enc.decode(encoded_data)

print(f'Data: {data}')
print(f'Token: {token}')
print(f'Encoded Data: {encoded_data}')
print(f'Decoded Data: {decoded_data}')
```

### `Console`
```yaml
Data: this is a test
Token: j ms 
Encoded Data: tlzziol ol q z
Decoded Data: this is a test
```

### `Environment Variables`
```yaml
ENCODED_CHARS: 'hzkjwegfuimloybcvqxpsrdtna'
PROCESS: 'R;N;S[0:3;R;'
```

## Encoder Engine
### Configuration
1. `decoded_chars`
	- type: `str`
	- default: `''`
	- usage: The collection of characters that can be encoded.
	- secret: `optional`
2. `encoded_chars`
	- type: `str`
	- default: `''`
	- usage: The collection of encoded characters with respect to decoded characters.
	- secret: `recommended`
3. `process`
	- type: `str`
	- default: `''`
	- usage: The algorithm to be followed to encode data.
	- secret: `recommended`
4. `token_limit`
	- type: `int`
	- default: 5
	- usage: Number of characters in final token.
5. `min_data_length`
	- type: `int`
    - default: 5
    - usage: Sets minimum length for data.

### Functions
1. `encode(data:str)`
	- usage: Encodes `[data]`.
	- returns: `encoded data`
	- return type: `str`
	- `[data]`: Input value to generate encoded data.
2. `decode(data:str)`
	- usage: Decodes `[data]`.
	- returns: `decoded data`
	- return type: `str`
	- `[data]`: Input value to decode.
3. `token(data:str)`
	- usage: Tokenizes `[data]`.
	- returns: `token`
	- return type: `str`
	- `[data]`: Input value to generate token.
4. `random_encode_chars()`
	- usage: Creates a random `encoded_chars` set from given value of `decoded_chars`.
	- returns: `encoded_chars`
	- return type: `str`
5. `random_process()`
	- usage: Creates a random `process`.
	- returns: `process`
	- return type: `str`

## Modules Required
1. `random`
	- type: `default`(Built In with Python)

