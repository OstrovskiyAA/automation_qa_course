data11 = ['Desktop', 'Notes', 'Commands', 'WorkSpace', 'React', 'Angular', 'Veu', 'Public', 'Private', 'Classified',
          'Word File.doc']
data22 = ['desktop', 'notes', 'commands', 'workspace', 'react', 'angular', 'veu', 'public', 'private', 'classified',
          'wordFile']

data11 = str(data11).replace(' ', '').replace('doc', '').replace('.', '').lower()
data22 = str(data22).replace(' ', '').lower()
print(str(data11).replace(' ', '').replace('doc', '').replace('.', '').lower())
print(data22)
assert data11 == data22
