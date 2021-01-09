import pickle
def store_data():
    emp1={'name':'Rob','age':50}
    emp2={'name':'Ken','age':52}
    db={}
    db['emp1']=emp1
    db['emp2'] = emp2
    dbfile=open('empfile','ab')
    pickle.dump(db,dbfile)
    dbfile.close()

def load_data():
    dbfile=open('empfile','rb')
    db=pickle.load(dbfile)
    for keys in db:
        print(keys,' = >',db[keys])
    dbfile.close()

if __name__ == '__main__':
    store_data()
    load_data()
