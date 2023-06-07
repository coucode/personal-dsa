/*
Implement a prototype service to detect a user's location based on their IP addresses. 

The IP addresses belonging to the IPv4 space are conventionally represented by four octets, "a.b.c.d" such as 
127.10.20.30. To keep it simple, these IP addresses are 
classified into 5 different regions indexed from 1 to 5 on the basis of the order of the bits in the first octet

Broadly, the IP addresses are categorized as follows: 
1. 0.0.0.0 - 127.255.255.255
2. 128.0.0.0 - 191.255.255.255
3. 192.0.0.0 - 223.255.255.255
4. 224.0.0.0 - 239.255.255.255
5. 240.0.0.0 - 255.255.255.255

Given a list of strings, ip_addresses of size n, representing possible IPv4 Addresses, for each address determine if it is a valid IP or not
and classify it into one of the 5 classes. Retrun an array of n integers that represent the index of the regions for the corresponding
IP addresses. Represent an invalid IP as -1.
*/


function getRegions(ip_addresses) {
  let answer = Array(ip_addresses.length).fill(null)
  for (let i = 0; i < ip_addresses.length; i++) {
    let octets = ip_addresses[i].split('.')
    for (let j = 0; j < octets.length; j++) {
      let current = octets[j]
      if (current < 0 || current > 255) {
        answer[i] = -1
        break
      }
      if (j === 0) {
        if (current >= 0 && current <= 127) {
          answer[i] = 1
        } else if (current >= 128 && current <= 191) {
          answer[i] = 2
        } else if (current >= 192 && current <= 223) {
          answer[i] = 3
        } else if (current >= 224 && current <= 239) {
          answer[i] = 4
        } else if (current >= 240 && current <= 255) {
          answer[i] = 5
        }
      }
    }
  }
  return answer
}
