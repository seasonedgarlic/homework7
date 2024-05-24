my_dict = {'first' : 111, 'second' : 222, 'third' : 333}
print('Dict: ' + str(my_dict))
print('Existing value: ' + str(my_dict['first']) + '; '
      'Not existing value: ' + str(my_dict.get('fourth')))
my_dict['fourth'] = 444
my_dict['fifth'] = 555
print('Deleted value: ' + str(my_dict.pop('first')))
print('Modified dictionary: ' + str(my_dict))
my_set = {000, 99.9, 000, 'hippo'}
print('Set: ' + str(my_set))
my_set.add(45)
my_set.add((1,2,3))
my_set.remove(000)
print('Modified set: ' + str(my_set))