def rearrange_name(s):
    if ',' in s:
        place=s.find(',')
        firstname=s[place+2:]
        lastname=s[:place]
        return firstname + " " + lastname
    return s
st=input("Enter Lastname, Firstname: ")
print(rearrange_name(st))
