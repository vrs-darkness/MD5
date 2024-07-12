# MD5 and Salted MD5 Algorithm

## Introduction to Hashing

Hashing is a process of converting an input (or 'message') into a fixed-size string of bytes, typically using a hash function. It is used in various applications such as data integrity verification, digital signatures, and password storage.

### Properties of a Good Hash Function:
1. **Deterministic**: The same input will always produce the same output.
2. **Fast Computation**: Hashing the input should be quick.
3. **Pre-image Resistance**: It should be computationally infeasible to reverse the hash function.
4. **Small Changes Impact**: A small change in input should produce a significantly different hash.
5. **Collision Resistance**: It should be infeasible to find two different inputs with the same hash.

## MD5 Algorithm

MD5 (Message Digest Algorithm 5) is a widely used cryptographic hash function that produces a 128-bit (16-byte) hash value. It is commonly used to check data integrity but is not suitable for security-sensitive applications due to its vulnerabilities.

### MD5 Algorithm Steps:
1. **Padding**: Add padding to the original message so that its length is 64 bits shy of a multiple of 512.
2. **Append Length**: Append the original message length as a 64-bit integer.
3. **Initialize MD Buffer**: Initialize a 128-bit buffer with specific constants.
4. **Process Message in 512-bit Chunks**: Process the message in 512-bit chunks using the buffer.
5. **Output**: The buffer is transformed into the final hash value.

### Limitations of MD5:
- **Collision Vulnerability**: It is possible to find two different messages with the same hash value.
- **Not Suitable for Cryptographic Security**: Due to its vulnerabilities, it is not recommended for cryptographic purposes.

## Salted MD5 Algorithm

Salting is a technique used to add extra data (salt) to the input of the hash function to ensure unique hash values for identical inputs, enhancing security. This is especially useful in password hashing to protect against rainbow table attacks.

### Salted MD5 Steps:
1. **Generate a Salt**: Create a random value to use as a salt.
2. **Combine Input and Salt**: Append the salt to the original message.
3. **Hash the Combined Input**: Use the MD5 algorithm to hash the combined input.
4. **Store the Salt and Hash**: Store both the salt and the hash for verification purposes.



### Instructions to Run the Code
1. Clone the Repository:
```bash
git clone https://github.com/vrs-darkness/MD5.git
cd MD5
```
2. #####  Run the Script:
Execute the script using Python:
```bash
python3 MD5.py
```
### Resources
  - [Research Papers](https://github.com/vrs-darkness/MD5/tree/main/Research_Papers)
  - [Dataset](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials)
    
### Additonal Information:
  - Currently works are being done over other ways of Generating / re-constructing the same Hash.
  Happy Learning!!
    
 
                                                 
