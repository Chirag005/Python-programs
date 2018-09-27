names={"john":86.5,"jack":91.2,"jill":84.5,"harry":72.1,"joe":80.5}
items=[(v,k) for k,v in names.items()]
items.sort()
items.reverse()
items=[(k,v) for v,k in items]
print(items[0:3])
alist=names.values()
average=float(sum(alist)/len(alist))
print('average is:%.2f '%(average))
