print("NAME: Haneesh M")
print("USN:1AY24AI038")
print("SECTION:M")
class Kangaroo:
    def __init__(self, pouch_contents=None):
        if pouch_contents is None:
            self.pouch_contents = []
        else:
            self.pouch_contents = list(pouch_contents)  
    def put_in_pouch(self, item):
        self.pouch_contents.append(item)
    def __str__(self):
        contents = ', '.join(str(item) for item in self.pouch_contents)
        return f"Kangaroo with pouch contents: [{contents}]"
kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch("wallet")
kanga.put_in_pouch("keys")
kanga.put_in_pouch(roo)
print(kanga)

