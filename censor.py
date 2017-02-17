'''
To add something to the list, run simple_encode(something), and paste
the results into blacklist.
'''
blacklist = None

def filter_strings(string_list):
  return [x for x in string_list if string_is_clean(x)]

def string_is_clean(sentence):
  for encoded_word in blacklist:
    if simple_decode(encoded_word).lower() in sentence.lower():
      return False

  return True

def simple_decode(x):
  return ''.join([chr(int(number)) for number in x.split('.')])

def simple_encode(x):
  output = []

  for char in x:
    output.append(str(ord(char)))

  return '.'.join(output)

blacklist = [
  '115.101.101.45.116.104.114.111.117.103.104',
  '100.105.115.97.98.105.108.105.116.121',
  '120.45.114.97.116.101.100',
  '98.97.108.108.115',
  '97.101.111.108.117.115',
  '97.104.111.108.101',
  '97.110.97.108',
  '97.110.97.108.112.114.111.98.101',
  '97.110.105.108.105.110.103.117.115',
  '97.110.117.115',
  '97.114.101.111.108.97',
  '97.114.101.111.108.101',
  '97.114.105.97.110',
  '97.114.121.97.110',
  '97.115.115',
  '97.115.115.98.97.110.103',
  '97.115.115.98.97.110.103.101.100',
  '97.115.115.98.97.110.103.115',
  '97.115.115.101.115',
  '97.115.115.102.117.99.107',
  '97.115.115.102.117.99.107.101.114',
  '97.115.115.104.97.116',
  '97.115.115.32.104.111.108.101',
  '97.115.115.104.111.108.101.115',
  '97.115.115.109.97.115.116.101.114',
  '97.115.115.109.117.110.99.104',
  '97.115.115.119.105.112.101',
  '97.115.115.119.105.112.101.115',
  '97.122.97.122.101.108',
  '97.122.122',
  '98.97.98.101',
  '98.97.98.101.115',
  '98.97.108.108.115.97.99.107',
  '98.97.110.103',
  '98.97.110.103.101.114',
  '98.97.114.102',
  '98.97.115.116.97.114.100',
  '98.97.115.116.97.114.100.115',
  '98.97.119.100.121',
  '98.101.97.110.101.114',
  '98.101.97.114.100.101.100.99.108.97.109',
  '98.101.97.115.116.105.97.108.105.116.121',
  '98.101.97.116.99.104',
  '98.101.97.116.101.114',
  '98.101.97.118.101.114',
  '98.101.101.114',
  '98.101.101.121.111.116.99.104',
  '98.101.111.116.99.104',
  '98.105.97.116.99.104',
  '98.105.103.116.105.116.115',
  '98.105.103.32.116.105.116.115',
  '98.105.109.98.111',
  '98.105.116.99.104',
  '98.105.116.99.104.101.100',
  '98.105.116.99.104.101.115',
  '98.105.116.99.104.121',
  '98.108.111.119.32.106.111.98',
  '98.108.111.119',
  '98.108.111.119.106.111.98',
  '98.108.111.119.106.111.98.115',
  '98.111.100',
  '98.111.100.105.108.121',
  '98.111.105.110.107',
  '98.111.108.108.111.99.107',
  '98.111.108.108.111.99.107.115',
  '98.111.108.108.111.107',
  '98.111.110.101',
  '98.111.110.101.100',
  '98.111.110.101.114',
  '98.111.110.101.114.115',
  '98.111.110.103',
  '98.111.111.98',
  '98.111.111.98.105.101.115',
  '98.111.111.98.115',
  '98.111.111.98.121',
  '98.111.111.103.101.114',
  '98.111.111.107.105.101',
  '98.111.111.116.101.101',
  '98.111.111.116.105.101',
  '98.111.111.116.121',
  '98.111.111.122.101',
  '98.111.111.122.101.114',
  '98.111.111.122.121',
  '98.111.115.111.109',
  '98.111.115.111.109.121',
  '98.111.119.101.108',
  '98.111.119.101.108.115',
  '98.114.97',
  '98.114.97.115.115.105.101.114.101',
  '98.114.101.97.115.116',
  '98.114.101.97.115.116.115',
  '98.117.103.103.101.114',
  '98.117.107.107.97.107.101',
  '98.117.108.108.115.104.105.116',
  '98.117.108.108.32.115.104.105.116',
  '98.117.108.108.115.104.105.116.115',
  '98.117.108.108.115.104.105.116.116.101.100',
  '98.117.108.108.116.117.114.100.115',
  '98.117.110.103',
  '98.117.115.116.121',
  '98.117.116.116',
  '98.117.116.116.32.102.117.99.107',
  '98.117.116.116.102.117.99.107',
  '98.117.116.116.102.117.99.107.101.114',
  '98.117.116.116.102.117.99.107.101.114',
  '98.117.116.116.112.108.117.103',
  '99.97.99.97',
  '99.97.104.111.110.101',
  '99.97.109.101.108.116.111.101',
  '99.97.114.112.101.116.109.117.110.99.104.101.114',
  '99.97.119.107',
  '99.101.114.118.105.120',
  '99.104.105.110.99',
  '99.104.105.110.99.115',
  '99.104.105.110.107',
  '99.104.105.110.107',
  '99.104.111.100.101',
  '99.104.111.100.101.115',
  '99.108.105.109.97.120',
  '99.108.105.116',
  '99.108.105.116.111.114.105.115',
  '99.108.105.116.111.114.117.115',
  '99.108.105.116.115',
  '99.108.105.116.116.121',
  '99.111.99.97.105.110',
  '99.111.99.97.105.110.101',
  '99.111.99.107',
  '99.111.99.107.98.108.111.99.107',
  '99.111.99.107.104.111.108.115.116.101.114',
  '99.111.99.107.107.110.111.99.107.101.114',
  '99.111.99.107.115',
  '99.111.99.107.115.109.111.107.101.114',
  '99.111.99.107.115.117.99.107.101.114',
  '99.111.99.107.32.115.117.99.107.101.114',
  '99.111.105.116.97.108',
  '99.111.109.109.105.101',
  '99.111.110.100.111.109',
  '99.111.111.110',
  '99.111.111.110.115',
  '99.111.114.107.115.117.99.107.101.114',
  '99.114.97.98.115',
  '99.114.97.99.107',
  '99.114.97.99.107.101.114',
  '99.114.97.99.107.119.104.111.114.101',
  '99.114.97.112',
  '99.114.97.112.112.121',
  '99.117.109',
  '99.117.109.109.105.110',
  '99.117.109.109.105.110.103',
  '99.117.109.115.104.111.116',
  '99.117.109.115.104.111.116.115',
  '99.117.109.115.108.117.116',
  '99.117.109.115.116.97.105.110',
  '99.117.110.105.108.105.110.103.117.115',
  '99.117.110.110.105.108.105.110.103.117.115',
  '99.117.110.110.121',
  '99.117.110.116',
  '99.117.110.116',
  '99.117.110.116.102.97.99.101',
  '99.117.110.116.104.117.110.116.101.114',
  '99.117.110.116.108.105.99.107',
  '99.117.110.116.108.105.99.107.101.114',
  '99.117.110.116.115',
  '100.97.103.111',
  '100.97.103.111.115',
  '100.97.109.109.105.116',
  '100.97.109.110',
  '100.97.109.110.101.100',
  '100.97.109.110.105.116',
  '100.105.99.107',
  '100.105.99.107.98.97.103',
  '100.105.99.107.100.105.112.112.101.114',
  '100.105.99.107.102.97.99.101',
  '100.105.99.107.102.108.105.112.112.101.114',
  '100.105.99.107.104.101.97.100',
  '100.105.99.107.104.101.97.100.115',
  '100.105.99.107.105.115.104',
  '100.105.99.107.114.105.112.112.101.114',
  '100.105.99.107.115.105.112.112.101.114',
  '100.105.99.107.119.101.101.100',
  '100.105.99.107.119.104.105.112.112.101.114',
  '100.105.99.107.122.105.112.112.101.114',
  '100.105.100.100.108.101',
  '100.105.107.101',
  '100.105.108.100.111',
  '100.105.108.100.111.115',
  '100.105.108.105.103.97.102',
  '100.105.108.108.119.101.101.100',
  '100.105.109.119.105.116',
  '100.105.110.103.108.101',
  '100.105.112.115.104.105.112',
  '100.111.110.103',
  '100.111.111.102.117.115',
  '100.111.111.115.104',
  '100.111.112.101.121',
  '100.111.117.99.104.101',
  '100.111.117.99.104.101.98.97.103',
  '100.111.117.99.104.101.98.97.103.115',
  '100.111.117.99.104.101.121',
  '100.114.117.110.107',
  '100.117.109.97.115.115',
  '100.117.109.98.97.115.115',
  '100.117.109.98.97.115.115.101.115',
  '100.117.109.109.121',
  '100.121.107.101',
  '100.121.107.101.115',
  '101.106.97.99.117.108.97.116.101',
  '101.110.108.97.114.103.101.109.101.110.116',
  '101.114.101.99.116',
  '101.114.101.99.116.105.111.110',
  '101.114.111.116.105.99',
  '101.115.115.111.104.98.101.101',
  '101.120.116.97.99.121',
  '101.120.116.97.115.121',
  '102.97.99.107',
  '102.97.103',
  '102.97.103.103',
  '102.97.103.103.101.100',
  '102.97.103.103.105.116',
  '102.97.103.103.111.116',
  '102.97.103.111.116',
  '102.97.103.115',
  '102.97.105.103',
  '102.97.105.103.116',
  '102.97.110.110.121.98.97.110.100.105.116',
  '102.97.114.116',
  '102.97.114.116.107.110.111.99.107.101.114',
  '102.97.116',
  '102.101.108.99.104',
  '102.101.108.99.104.101.114',
  '102.101.108.99.104.105.110.103',
  '102.101.108.108.97.116.101',
  '102.101.108.108.97.116.105.111',
  '102.101.108.116.99.104',
  '102.101.108.116.99.104.101.114',
  '102.105.115.116.101.100',
  '102.105.115.116.105.110.103',
  '102.105.115.116.121',
  '102.108.111.111.122.121',
  '102.111.97.100',
  '102.111.110.100.108.101',
  '102.111.111.98.97.114',
  '102.111.114.101.115.107.105.110',
  '102.114.101.101.120',
  '102.114.105.103.103',
  '102.114.105.103.103.97',
  '102.117.98.97.114',
  '102.117.99.107',
  '102.117.99.107.97.115.115',
  '102.117.99.107.101.100',
  '102.117.99.107.101.100',
  '102.117.99.107.101.114',
  '102.117.99.107.102.97.99.101',
  '102.117.99.107.105.110',
  '102.117.99.107.105.110.103',
  '102.117.99.107.110.117.103.103.101.116',
  '102.117.99.107.110.117.116',
  '102.117.99.107.111.102.102',
  '102.117.99.107.115',
  '102.117.99.107.116.97.114.100',
  '102.117.99.107.117.112',
  '102.117.99.107.119.97.100',
  '102.117.99.107.119.105.116',
  '102.117.100.103.101.112.97.99.107.101.114',
  '102.117.107',
  '102.118.99.107',
  '102.120.99.107',
  '103.97.101',
  '103.97.105',
  '103.97.110.106.97',
  '103.97.121',
  '103.97.121.115',
  '103.101.121',
  '103.102.121',
  '103.104.97.121',
  '103.104.101.121',
  '103.105.103.111.108.111',
  '103.108.97.110.115',
  '103.111.97.116.115.101',
  '103.111.100.97.109.110',
  '103.111.100.97.109.110.105.116',
  '103.111.100.100.97.109',
  '103.111.100.100.97.109.109.105.116',
  '103.111.100.100.97.109.110',
  '103.111.108.100.101.110.115.104.111.119.101.114',
  '103.111.110.97.100',
  '103.111.110.97.100.115',
  '103.111.111.107',
  '103.111.111.107.115',
  '103.114.105.110.103.111',
  '103.115.112.111.116',
  '103.116.102.111',
  '103.117.105.100.111',
  '104.97.110.100.106.111.98',
  '104.97.114.100.32.111.110',
  '104.101.98.101',
  '104.101.101.98',
  '104.101.108.108',
  '104.101.109.112',
  '104.101.114.111.105.110',
  '104.101.114.112',
  '104.101.114.112.101.115',
  '104.101.114.112.121',
  '104.105.116.108.101.114',
  '104.105.118',
  '104.111.98.97.103',
  '104.111.109.101.121',
  '104.111.109.111',
  '104.111.109.111.101.121',
  '104.111.110.107.121',
  '104.111.111.99.104',
  '104.111.111.107.97.104',
  '104.111.111.107.101.114',
  '104.111.111.114',
  '104.111.111.116.99.104',
  '104.111.111.116.101.114',
  '104.111.111.116.101.114.115',
  '104.111.114.110.121',
  '104.117.109.112',
  '104.117.109.112.101.100',
  '104.117.109.112.105.110.103',
  '104.117.115.115.121',
  '104.121.109.101.110',
  '105.110.98.114.101.100',
  '105.110.99.101.115.116',
  '105.110.106.117.110',
  '106.97.99.107.97.115.115',
  '106.97.99.107.104.111.108.101',
  '106.97.99.107.111.102.102',
  '106.97.112',
  '106.97.112.115',
  '106.101.114.107.101.100',
  '106.101.114.107.111.102.102',
  '106.105.115.109',
  '106.105.122',
  '106.105.122.109',
  '106.105.122.122',
  '106.105.122.122.101.100',
  '106.117.110.107.105.101',
  '106.117.110.107.121',
  '107.105.107.101',
  '107.105.107.101.115',
  '107.105.108.108',
  '107.105.110.107.121',
  '107.107.107',
  '107.108.97.110',
  '107.110.111.98.101.110.100',
  '107.111.111.99.104',
  '107.111.111.99.104.101.115',
  '107.111.111.116.99.104',
  '107.114.97.117.116',
  '107.121.107.101',
  '108.97.98.105.97',
  '108.101.99.104',
  '108.101.112.101.114',
  '108.101.115.98.105.97.110.115',
  '108.101.115.98.111',
  '108.101.115.98.111.115',
  '108.101.122',
  '108.101.122.98.105.97.110',
  '108.101.122.98.105.97.110.115',
  '108.101.122.98.111',
  '108.101.122.98.111.115',
  '108.101.122.122.105.101',
  '108.101.122.122.105.101.115',
  '108.101.122.122.121',
  '108.109.97.111',
  '108.109.102.97.111',
  '108.111.105.110',
  '108.111.105.110.115',
  '108.117.98.101',
  '108.117.115.116.121',
  '109.97.109.115',
  '109.97.115.115.97',
  '109.97.115.116.101.114.98.97.116.101',
  '109.97.115.116.101.114.98.97.116.105.110.103',
  '109.97.115.116.101.114.98.97.116.105.111.110',
  '109.97.115.116.117.114.98.97.116.101',
  '109.97.115.116.117.114.98.97.116.105.110.103',
  '109.97.115.116.117.114.98.97.116.105.111.110',
  '109.97.120.105',
  '109.101.110.115.101.115',
  '109.101.110.115.116.114.117.97.116.101',
  '109.101.110.115.116.114.117.97.116.105.111.110',
  '109.101.116.104',
  '109.111.102.111',
  '109.111.108.101.115.116',
  '109.111.111.108.105.101',
  '109.111.114.111.110',
  '109.111.116.104.101.114.102.117.99.107.97',
  '109.111.116.104.101.114.102.117.99.107.101.114',
  '109.111.116.104.101.114.102.117.99.107.105.110.103',
  '109.116.104.101.114.102.117.99.107.101.114',
  '109.116.104.114.102.117.99.107.101.114',
  '109.116.104.114.102.117.99.107.105.110.103',
  '109.117.102.102',
  '109.117.102.102.100.105.118.101.114',
  '109.117.114.100.101.114',
  '109.117.116.104.97.102.117.99.107.97.122',
  '109.117.116.104.97.102.117.99.107.101.114',
  '109.117.116.104.101.114.102.117.99.107.101.114',
  '109.117.116.104.101.114.102.117.99.107.105.110.103',
  '109.117.116.104.114.102.117.99.107.105.110.103',
  '110.97.100',
  '110.97.100.115',
  '110.97.107.101.100',
  '110.97.112.97.108.109',
  '110.97.112.112.121',
  '110.97.122.105',
  '110.97.122.105.115.109',
  '110.101.103.114.111',
  '110.105.103.103.97',
  '110.105.103.103.97.104',
  '110.105.103.103.97.115',
  '110.105.103.103.97.122',
  '110.105.103.103.101.114',
  '110.105.103.103.101.114',
  '110.105.103.103.101.114.115',
  '110.105.103.103.108.101',
  '110.105.103.108.101.116',
  '110.105.109.114.111.100',
  '110.105.110.110.121',
  '110.105.112.112.108.101',
  '110.111.111.107.121',
  '110.121.109.112.104.111',
  '111.112.105.97.116.101',
  '111.112.105.117.109',
  '111.114.97.108',
  '111.114.97.108.108.121',
  '111.114.103.97.110',
  '111.114.103.97.115.109',
  '111.114.103.97.115.109.105.99',
  '111.114.103.105.101.115',
  '111.114.103.121',
  '111.118.97.114.121',
  '111.118.117.109',
  '111.118.117.109.115',
  '112.97.100.100.121',
  '112.97.107.105',
  '112.97.110.116.105.101',
  '112.97.110.116.105.101.115',
  '112.97.110.116.121',
  '112.97.115.116.105.101',
  '112.97.115.116.121',
  '112.99.112',
  '112.101.99.107.101.114',
  '112.101.100.111',
  '112.101.100.111.112.104.105.108.101',
  '112.101.100.111.112.104.105.108.105.97',
  '112.101.100.111.112.104.105.108.105.97.99',
  '112.101.101',
  '112.101.101.112.101.101',
  '112.101.110.101.116.114.97.116.101',
  '112.101.110.101.116.114.97.116.105.111.110',
  '112.101.110.105.97.108',
  '112.101.110.105.108.101',
  '112.101.110.105.115',
  '112.101.114.118.101.114.115.105.111.110',
  '112.101.121.111.116.101',
  '112.104.97.108.108.105',
  '112.104.97.108.108.105.99',
  '112.104.117.99.107',
  '112.105.108.108.111.119.98.105.116.101.114',
  '112.105.109.112',
  '112.105.110.107.111',
  '112.105.115.115',
  '112.105.115.115.101.100',
  '112.105.115.115.111.102.102',
  '112.109.115',
  '112.111.108.97.99.107',
  '112.111.108.108.111.99.107',
  '112.111.111.110',
  '112.111.111.110.116.97.110.103',
  '112.111.114.110',
  '112.111.114.110.111',
  '112.111.114.110.111.103.114.97.112.104.121',
  '112.111.116',
  '112.111.116.116.121',
  '112.114.105.99.107',
  '112.114.105.103',
  '112.114.111.115.116.105.116.117.116.101',
  '112.114.117.100.101',
  '112.117.98.101',
  '112.117.98.105.99',
  '112.117.98.105.115',
  '112.117.110.107.97.115.115',
  '112.117.110.107.121',
  '112.117.115.115',
  '112.117.115.115.105.101.115',
  '112.117.115.115.121',
  '112.117.115.115.121.112.111.117.110.100.101.114',
  '112.117.116.111',
  '113.117.101.97.102',
  '113.117.101.101.102',
  '113.117.101.101.102',
  '113.117.101.101.114',
  '113.117.101.101.114.111',
  '113.117.101.101.114.115',
  '113.117.105.99.107.121',
  '113.117.105.109',
  '114.97.99.121',
  '114.97.112.101',
  '114.97.112.101.100',
  '114.97.112.101.114',
  '114.97.112.105.115.116',
  '114.97.117.110.99.104',
  '114.101.99.116.97.108',
  '114.101.99.116.117.109',
  '114.101.99.116.117.115',
  '114.101.101.102.101.114',
  '114.101.101.116.97.114.100',
  '114.101.105.99.104',
  '114.101.116.97.114.100',
  '114.101.116.97.114.100.101.100',
  '114.101.118.117.101',
  '114.105.109.106.111.98',
  '114.105.116.97.114.100',
  '114.116.97.114.100',
  '114.117.109',
  '114.117.109.112',
  '114.117.109.112.114.97.109.109.101.114',
  '114.117.115.107.105',
  '115.97.100.105.115.109',
  '115.97.100.105.115.116',
  '115.99.97.103',
  '115.99.97.110.116.105.108.121',
  '115.99.104.105.122.111',
  '115.99.104.108.111.110.103',
  '115.99.114.101.119',
  '115.99.114.101.119.101.100',
  '115.99.114.111.103',
  '115.99.114.111.116',
  '115.99.114.111.116.101',
  '115.99.114.111.116.117.109',
  '115.99.114.117.100',
  '115.99.117.109',
  '115.101.97.109.97.110',
  '115.101.97.109.101.110',
  '115.101.100.117.99.101',
  '115.101.109.101.110',
  '115.101.120',
  '115.101.120.117.97.108',
  '115.104.97.109.101.100.97.109.101',
  '115.104.105.116',
  '115.104.105.116.101',
  '115.104.105.116.101.97.116.101.114',
  '115.104.105.116.102.97.99.101',
  '115.104.105.116.104.101.97.100',
  '115.104.105.116.104.111.108.101',
  '115.104.105.116.104.111.117.115.101',
  '115.104.105.116.115',
  '115.104.105.116.116',
  '115.104.105.116.116.101.100',
  '115.104.105.116.116.101.114',
  '115.104.105.116.116.121',
  '115.104.105.122',
  '115.105.115.115.121',
  '115.107.97.103',
  '115.107.97.110.107',
  '115.108.97.118.101',
  '115.108.101.97.122.101',
  '115.108.101.97.122.121',
  '115.108.117.116',
  '115.108.117.116.100.117.109.112.101.114',
  '115.108.117.116.107.105.115.115',
  '115.108.117.116.115',
  '115.109.101.103.109.97',
  '115.109.117.116',
  '115.109.117.116.116.121',
  '115.110.97.116.99.104',
  '115.110.105.112.101.114',
  '115.110.117.102.102',
  '115.111.100.111.109',
  '115.111.117.115.101',
  '115.111.117.115.101.100',
  '115.112.101.114.109',
  '115.112.105.99',
  '115.112.105.99.107',
  '115.112.105.107',
  '115.112.105.107.115',
  '115.112.111.111.103.101',
  '115.112.117.110.107',
  '115.116.101.97.109.121',
  '115.116.102.117',
  '115.116.105.102.102.121',
  '115.116.111.110.101.100',
  '115.116.114.105.112',
  '115.116.114.111.107.101',
  '115.116.117.112.105.100',
  '115.117.99.107',
  '115.117.99.107.101.100',
  '115.117.99.107.105.110.103',
  '115.117.109.111.102.97.98.105.97.116.99.104',
  '116.97.109.112.111.110',
  '116.97.114.100',
  '116.97.119.100.114.121',
  '116.101.97.98.97.103.103.105.110.103',
  '116.101.97.116',
  '116.101.114.100',
  '116.101.115.116.101',
  '116.101.115.116.101.101',
  '116.101.115.116.101.115',
  '116.101.115.116.105.99.108.101',
  '116.101.115.116.105.115',
  '116.104.114.117.115.116',
  '116.104.117.103',
  '116.105.110.107.108.101',
  '116.105.116',
  '116.105.116.102.117.99.107',
  '116.105.116.105',
  '116.105.116.115',
  '116.105.116.116.105.101.102.117.99.107.101.114',
  '116.105.116.116.105.101.115',
  '116.105.116.116.121',
  '116.105.116.116.121.102.117.99.107',
  '116.105.116.116.121.102.117.99.107.101.114',
  '116.111.107.101',
  '116.111.111.116.115',
  '116.114.97.109.112',
  '116.114.97.110.115.115.101.120.117.97.108',
  '116.114.97.115.104.121',
  '116.117.98.103.105.114.108',
  '116.117.114.100',
  '116.117.115.104',
  '116.119.97.116',
  '116.119.97.116.115',
  '117.103.108.121',
  '117.110.100.105.101.115',
  '117.110.119.101.100',
  '117.114.105.110.97.108',
  '117.114.105.110.101',
  '117.116.101.114.117.115',
  '117.122.105',
  '118.97.103',
  '118.97.103.105.110.97',
  '118.97.108.105.117.109',
  '118.105.97.103.114.97',
  '118.105.114.103.105.110',
  '118.105.120.101.110',
  '118.111.100.107.97',
  '118.111.109.105.116',
  '118.111.121.101.117.114',
  '118.117.108.103.97.114',
  '118.117.108.118.97',
  '119.97.100',
  '119.97.110.103',
  '119.97.110.107',
  '119.97.110.107.101.114',
  '119.97.122.111.111',
  '119.101.100.103.105.101',
  '119.101.101.100',
  '119.101.101.110.105.101',
  '119.101.101.119.101.101',
  '119.101.105.110.101.114',
  '119.101.105.114.100.111',
  '119.101.110.99.104',
  '119.101.116.98.97.99.107',
  '119.104.105.116.101.121',
  '119.104.105.122',
  '119.104.111.114.97.108.105.99.105.111.117.115',
  '119.104.111.114.101',
  '119.104.111.114.101.97.108.105.99.105.111.117.115',
  '119.104.111.114.101.100',
  '119.104.111.114.101.102.97.99.101',
  '119.104.111.114.101.104.111.112.112.101.114',
  '103.101.110.105.116.97.108',
  '119.104.111.114.101.104.111.117.115.101',
  '119.104.111.114.101.115',
  '119.104.111.114.105.110.103',
  '119.105.103.103.101.114',
  '119.111.109.98',
  '119.111.111.100.121',
  '119.111.112',
  '119.116.102',
  '120.120.120',
  '121.101.97.115.116.121',
  '121.111.98.98.111',
  '102.42.42.107.105.110.103',
  '122.111.111.112.104.105.108.101',
  '109.117.115.108.105.109',
  '106.101.119',
  ]
